# Real-time traffic summary logic
# traffic_summary.py
from threading import Lock, Event
from datetime import datetime

def display_summary(packet_count, protocol_counter, ip_counter, lock):
    while True:
        with lock:
            print("\n=== Real-Time Traffic Summary ===")
            print(f"Total Packets Captured: {packet_count[0]}")
            print(f"Protocol Breakdown: {dict(protocol_counter)}")
            print("Top Talkers (IP Addresses):")
            for ip, count in ip_counter.most_common(5):
                print(f"    - {ip}: {count} packets")
            print(f"Last Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        Event().wait(5)

