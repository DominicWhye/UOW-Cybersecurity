
import sys
import hashlib
from pathlib import Path
import bisect

# ------------------ Utility: hashing ------------------
def md5_hex(s: str) -> str:
    return hashlib.md5(s.encode('utf-8', errors='ignore')).hexdigest()

# ------------------ Reduction function R ------------------
# Maps a hex hash string + column index to an index in [0, n_passwords)
# We vary the slice offset by column to reduce collisions across columns.
def reduction_index(hash_hex: str, col: int, n_passwords: int) -> int:
    # Ensure lowercase hex
    h = hash_hex.lower()
    # Use a sliding 8-hex-digit window that moves with column
    window = 8
    if len(h) < window:
        # Fallback: pad if ever necessary (shouldn't happen for MD5)
        h = h.ljust(window, '0')
    start = (2 * col) % (len(h) - window + 1)
    chunk = h[start:start+window]
    try:
        val = int(chunk, 16)
    except ValueError:
        val = 0
    return val % n_passwords

# ------------------ Rainbow Table Generation ------------------
def generate_rainbow(passwords, chain_len=5):
    """
    For each unused word W0:
      H = md5(W0)
      repeat chain_len times:
        idx = R(H, col)
        W1 = passwords[idx]  # mark as used
        H = md5(W1)
      store (start=W0, final_hash=H) in table
    Returns:
      table: list of (final_hash_hex, start_word) sorted by final_hash_hex
    """
    n = len(passwords)
    used = [False] * n

    entries = []

    for i, w0 in enumerate(passwords):
        if used[i]:
            continue
        used[i] = True
        h = md5_hex(w0)
        for col in range(chain_len):
            idx = reduction_index(h, col, n)
            used[idx] = True  # mark reduced word as used
            w = passwords[idx]
            h = md5_hex(w)
        # store final
        entries.append((h, w0))

    # sort by final hash for binary search
    entries.sort(key=lambda x: x[0])
    return entries

# ------------------ Lookup Utilities ------------------
def binary_search_hash(entries, target_hash_hex):
    """entries is sorted by final_hash_hex"""
    keys = [e[0] for e in entries]
    pos = bisect.bisect_left(keys, target_hash_hex)
    if pos != len(keys) and keys[pos] == target_hash_hex:
        return entries[pos][1]  # return start word
    return None

def reconstruct_preimage(start_word, target_hash_hex, passwords, chain_len=5):
    """Walk chain from start_word to find the word that hashes to target_hash_hex"""
    h = md5_hex(start_word)
    if h == target_hash_hex:
        return start_word
    n = len(passwords)
    w = start_word
    for col in range(chain_len):
        idx = reduction_index(h, col, n)
        w = passwords[idx]
        h = md5_hex(w)
        if h == target_hash_hex:
            return w
    return None

def try_find_preimage(target_hash_hex, passwords, entries, chain_len=5):
    # 1) Check if it's exactly a chain end
    start = binary_search_hash(entries, target_hash_hex)
    if start is not None:
        pre = reconstruct_preimage(start, target_hash_hex, passwords, chain_len)
        if pre is not None:
            return pre

    # 2) Rainbow-style backtracking from different columns
    n = len(passwords)
    for i in range(chain_len - 1, -1, -1):
        h = target_hash_hex
        # Move forward from column i to the end to produce a potential chain end
        for col in range(i, chain_len):
            idx = reduction_index(h, col, n)
            w = passwords[idx]
            h = md5_hex(w)
        # Now h is a potential chain end; see if it exists
        start = binary_search_hash(entries, h)
        if start is not None:
            # Reconstruct chain from start to find the actual preimage
            pre = reconstruct_preimage(start, target_hash_hex, passwords, chain_len)
            if pre is not None:
                return pre
    return None

# ------------------ I/O and main ------------------
def is_valid_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python Rainbow.py Passwords.txt")
        sys.exit(1)

    pw_path = Path(sys.argv[1])
    if not pw_path.exists():
        print(f"Password file not found: {pw_path}")
        sys.exit(1)

    # Read passwords (keep order, strip, skip empties)
    passwords = []
    seen = set()
    with pw_path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            pw = line.rstrip("\n\r")
            if pw and pw not in seen:
                passwords.append(pw)
                seen.add(pw)

    print(f"Loaded {len(passwords)} passwords.")

    # Build rainbow table
    entries = generate_rainbow(passwords, chain_len=5)

    # Write Rainbow.txt with "start_word final_hash"
    out_path = Path("Rainbow.txt")
    with out_path.open("w", encoding="utf-8") as out:
        for final_hash, start_word in entries:
            out.write(f"{start_word}\t{final_hash}\n")

    print(f"Rainbow table lines: {len(entries)}")
    print(f"Wrote rainbow table to {out_path.resolve()}")

    # Interactive lookup
    try:
        while True:
            s = input("Enter MD5 hash to find pre-image (32 hex chars), or 'q' to quit: ").strip()
            if s.lower() == 'q':
                break
            if len(s) != 32 or not is_valid_hex(s):
                print("Invalid MD5 hash. Please input exactly 32 hex characters.")
                continue
            target = s.lower()
            pre = try_find_preimage(target, passwords, entries, chain_len=5)
            if pre is None:
                print("No pre-image found — hash not present in rainbow table.")
            else:
                print(f"Pre-image found: {pre}")
    except (EOFError, KeyboardInterrupt):
        pass

if __name__ == "__main__":
    main()
