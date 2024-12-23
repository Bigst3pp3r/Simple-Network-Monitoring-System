# Real-time traffic summary logic
from datetime import datetime
import threading

def display_summary(packet_count, protocol_counter, ip_counter, lock):
    """
    Display a real-time summary of traffic statistics.
    - packet_count: Total number of packets processed.
    - protocol_counter: Count of packets per protocol.
    - ip_counter: Count of packets per IP address.
    - lock: Threading lock for synchronization.
    """
    while True:
        with lock:
            print("\n=== Real-Time Traffic Summary ===")
            print(f"Total Packets Captured: {packet_count}")
            print(f"Protocol Breakdown: {dict(protocol_counter)}")
            print("Top Talkers (IP Addresses):")
            for ip, count in ip_counter.most_common(5):
                print(f"    - {ip}: {count} packets")
            print(f"Last Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("---------------------------------\n")
        # Wait for 5 seconds before updating the summary
        threading.Event().wait(5)
