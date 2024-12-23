# Functions for packet processing

from datetime import datetime
from scapy.layers.inet import IP
from collections import Counter

# Protocol map for human-readable names
protocol_map = {
    1: "ICMP",
    6: "TCP",
    17: "UDP",
    58: "ICMPv6",
}

# Global counters for real-time traffic analysis
packet_count = 0
protocol_counter = Counter()
ip_counter = Counter()

def process_packet(packet, lock, logger):
    """
    Process a single packet, extract relevant information, and log it.
    - packet: The packet to process.
    - lock: Threading lock for synchronization.
    - logger: Logger instance for logging details.
    """
    global packet_count
    try:
        if IP in packet:
            with lock:
                # Update counters
                packet_count += 1
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                ip_counter[src_ip] += 1
                ip_counter[dst_ip] += 1

                # Identify protocol
                proto_number = packet[IP].proto
                protocol = protocol_map.get(proto_number, f"Unknown ({proto_number})")
                protocol_counter[protocol] += 1

            # Log packet details
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp}, Source: {src_ip}, Destination: {dst_ip}, Protocol: {protocol}"
            logger.info(log_entry)
            print(log_entry)  # Display in console for real-time feedback
    except Exception as e:
        logger.error(f"Error processing packet: {e}")
