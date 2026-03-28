Q4 - Ransomware Implementation
Author: Dominic Whye

Date: 13/02/2026

1. Underlying Concepts: Hybrid Encryption
This implementation demonstrates Hybrid Encryption, a security architecture combining symmetric and asymmetric cryptography:


Symmetric Encryption (AES-128-CBC): Used to encrypt the user's secret file (my_secrets.txt).  To ensure compliance with OpenSSL 3.0+, the script utilizes PBKDF2 with 10,000 iterations to derive a secure key, preventing "deprecated key derivation" errors.


Asymmetric Encryption (RSA): The symmetric key (key.txt) is protected by encrypting it with the Attacker's RSA Public Key.  Only the holder of the corresponding Private Key can recover the symmetric key to decrypt the data.

OpenSSL 3.0 Compatibility: The script utilizes pkeyutl instead of the deprecated rsautl for RSA operations to ensure stability on modern Kali Linux environments.

2. How to Run the Program (Encryption)
Preparation: Create a secret file in the script's directory:


echo "Confidential data" > my_secrets.txt 

Execution: Run the Python script:


python3 ransomware.py 

Observation & Result:

The terminal displays the Author's name and the current date. 

The script generates an RSA key pair, a random symmetric key, and encrypts the target file. 

Original files (my_secrets.txt and key.txt) are deleted. 

A ransom message is displayed, and the resulting data_cipher.txt and key_cipher.txt are provided in base64 format. 


3. How to Run the Program (Decryption)
Assuming the "ransom" is paid and the attacker provides the private key (attacker_private.pem), follow these steps to restore the file: 

Decode the Key Cipher: Convert the base64 key back to binary:


base64 -d key_cipher.txt > key_cipher.bin


Recover the Symmetric Key: Use the private RSA key to decrypt the AES key:


openssl pkeyutl -decrypt -inkey attacker_private.pem -in key_cipher.bin -out recovered_key.txt


Restore the Original File: Use the recovered key to decrypt the data:


openssl enc -aes-128-cbc -d -pbkdf2 -iter 10000 -in data_cipher.txt -out my_secrets.txt -pass file:recovered_key.txt -base64


4. Decryption Result

Result: The data_cipher.txt is successfully decrypted. The file my_secrets.txt reappears in the directory, and its contents are identical to the original version before the attack.