Q2 - SSH Brute-forcer
Author: Dominic Whye

Date: 13/02/2026

1. Underlying Concepts: SSH Brute-forcing
SSH Brute-forcing is a trial-and-error method used to gain unauthorized access to a server by attempting to guess a user's password. This script uses the Paramiko library to automate this process. It iteratively attempts to establish an SSH connection with a target machine using a pre-defined list of passwords. If the AuthenticationException is not raised, the script identifies that the correct password has been found.

2. How to Run the Program
Ensure Paramiko is installed:
pip3 install paramiko 
[I have added the paramiko installation in the py file so there is no need for this step ^]

Execute the Script: Run the script using the Python interpreter in your Kali terminal:
python3 ssh_bruteforce.py

3. Expected Results
The program will display the author and current date

It will print each password attempt

Upon reaching the correct password (msfadmin), it will print a success message and stop execution.