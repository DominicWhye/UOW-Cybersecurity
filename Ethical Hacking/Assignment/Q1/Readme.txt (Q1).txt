Q1 - ARP Spoofer

Author: Dominic Whye Date: 13/02/2026 


1. Underlying Concepts: ARP Spoofing
ARP (Address Resolution Protocol) is responsible for mapping a known IP address to a MAC address on a local network. ARP Spoofing is an attack where forged ARP messages are sent to a local area network to link an attacker's MAC address with the IP address of a legitimate server or gateway.

In this implementation, arpspoof.py helps to perform the following:


Target the victim: The script sends forged ARP "is-at" responses to the victim (Metasploitable2), claiming that the Attacker's MAC address belongs to the Gateway



Target the gateway: Simultaneously, it sends forged responses to the Gateway, claiming the Attacker's MAC address belongs to the Victim


Man-in-the-Middle: This places the attacker (Kali) in the middle of the communication flow, allowing for traffic interception.

2. How to Run the Program
This program must be executed on Kali Linux to target the Metasploitable2 VM. It requires the Scapy package

Enable IP Forwarding: Ensure the Kali machine forwards the intercepted traffic so the victim does not lose connectivity:
sudo sysctl -w net.ipv4.ip_forward=1


Execute the Command: Use the following command format in the terminal:
sudo python3 arpspoof.py 10.0.2.3 10.0.2.1
(Note: 10.0.2.3 is the Victim IP and 10.0.2.1 is the Gateway IP) [this IP was during my own testing, Ip might differ]

3. Expected Results
Upon execution, the program will display the Author's name and the current date.

The script will continuously send spoofed packets to maintain the "poisoned" state of the ARP caches.

Verification: If you run arp -a on the Metasploitable2 machine, the MAC address associated with the Gateway (10.0.2.1) will match the MAC address of the Kali Attacker (10.0.2.15).