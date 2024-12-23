 # Entry point for the application
 # main.py
import threading
from scapy.all import sniff
from packet_processing import process_packet
from logging_setup import setup_logger
from filters import get_filter_choice
from traffic_summary import display_summary

if __name__ == "__main__":
    # Initialize logger
    logger = setup_logger()
    lock = threading.Lock()  # Lock for thread-safe updates

    print("Starting packet capture... Press Ctrl+C to stop.")

    # Get filter choice from user
    chosen_filter = get_filter_choice()

    # Start traffic summary thread
    summary_thread = threading.Thread(
        target=display_summary,
        args=(process_packet.packet_count, process_packet.protocol_counter, process_packet.ip_counter, lock),
        daemon=True,
    )
    summary_thread.start()

    try:
        # Start packet sniffing with the chosen filter
        sniff(prn=lambda p: process_packet(p, lock, logger), store=False, filter=chosen_filter)
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        print(f"Error occurred: {e}")
