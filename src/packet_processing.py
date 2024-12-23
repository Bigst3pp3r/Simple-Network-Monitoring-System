# Functions for packet processing

# packet_processing.py
from scapy.layers.inet import IP
from datetime import datetime
import logging

def process_packet(packet, protocol_map, ip_counter, protocol_counter, lock):
    try:
        if IP in packet:
            with lock:
                # Increment counters
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                proto_number = packet[IP].proto
                protocol = protocol_map.get(proto_number, f"Unknown ({proto_number})")

                ip_counter[src_ip] += 1
                ip_counter[dst_ip] += 1
                protocol_counter[protocol] += 1

            # Log packet details
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp}, Source: {src_ip}, Destination: {dst_ip}, Protocol: {protocol}"
            logging.info(log_entry)
            print(log_entry)
    except Exception as e:
        logging.error(f"Error processing packet: {e}")
