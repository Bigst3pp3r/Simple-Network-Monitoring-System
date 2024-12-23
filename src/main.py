 # Entry point for the application
 # main.py
import threading
from scapy.all import sniff
from collections import Counter
from packet_processing import process_packet
from logger_setup import setup_logging
from filter_selection import get_filter_choice
from traffic_summary import display_summary

if __name__ == "__main__":
    # Setup
    protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP", 58: "ICMPv6"}
    packet_count = [0]
    protocol_counter = Counter()
    ip_counter = Counter()
    lock = threading.Lock()

    log_file = "traffic_log.txt"
    setup_logging(log_file, max_bytes=1024 * 1024, backup_count=5)

    print("Starting packet capture... Press Ctrl+C to stop.")
    chosen_filter = get_filter_choice()

    # Start real-time summary
    summary_thread = threading.Thread(target=display_summary, args=(packet_count, protocol_counter, ip_counter, lock), daemon=True)
    summary_thread.start()

    # Start sniffing
    sniff(prn=lambda pkt: process_packet(pkt, protocol_map, ip_counter, protocol_counter, lock), store=False, filter=chosen_filter)
