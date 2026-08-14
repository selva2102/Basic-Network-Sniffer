from scapy.all import sniff, IP, TCP, UDP, Raw

def process_packet(packet):
    print("\n" + "=" * 60)

    # IP Layer Information
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")
        print(f"Protocol       : {ip_layer.proto}")

    # TCP Information
    if packet.haslayer(TCP):
        tcp_layer = packet[TCP]
        print(f"TCP Source Port: {tcp_layer.sport}")
        print(f"TCP Dest Port  : {tcp_layer.dport}")

    # UDP Information
    elif packet.haslayer(UDP):
        udp_layer = packet[UDP]
        print(f"UDP Source Port: {udp_layer.sport}")
        print(f"UDP Dest Port  : {udp_layer.dport}")

    # Payload Information
    if packet.haslayer(Raw):
        payload = packet[Raw].load
        print(f"Payload        : {payload[:100]}")

# Capture packets continuously
print("Starting packet capture...")
sniff(prn=process_packet, store=False)