Q3 - Reverse Shell
Author: Dominic Whye

Date: 13/02/2026

1. Underlying Concepts
A Reverse Shell is a type of shell session where the target machine (client) initiates a connection back to the attacker's machine (server). This is often used to bypass firewalls that block incoming connections but allow outgoing ones.


Socket Programming: The scripts use Python’s socket module to establish a TCP connection between the two programs

JSON Serialization: Because network sockets transmit raw bytes, the json package is used to package command strings and results into a structured format. This ensures that large amounts of data (like long directory listings) are transferred seamlessly without being cut off.


Command Execution: The subprocess module is used on the client side to execute system commands received from the server and capture their output to send back.

2. The "cd" Command Challenge
The primary challenge of this task was implementing the cd (change directory) command.

The Problem: Standard commands run via subprocess.check_output execute in a temporary child process. When a child process changes its directory, it does not affect the parent process (the reverse shell script itself)

The Solution: The revshell.py script identifies if a command starts with "cd". If it does, it uses the os.chdir() function to change the directory of the main Python process. Subsequent commands will then execute within that new directory.

3. How to Run the Program
For assessment convenience, both programs are run on the same Kali VM


Configure IP: Ensure the IP address in both server.py and revshell.py matches your Kali eth0/IP address (e.g., 10.0.2.15). 

Start the Server: Open a terminal and run:
python3 server.py
The terminal will display "Listening...".

Start the Client: Open a second terminal and run:

python3 revshell.py.

Remote Control: The Server terminal will confirm the connection. You can now type Linux commands (e.g., ls, whoami, pwd) to execute them on the "victim" terminal.

4. Expected Results
The server successfully establishes a connection with the client.

Standard Linux commands return the correct output to the server terminal.

The cd command successfully changes the working directory, which can be verified by running pwd after a cd command.

Typing quit closes the connection on both ends.