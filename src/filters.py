# Filtering mechanisms and options
# filter_selection.py
def get_filter_choice():
    print("Choose a filter option:")
    print("1. No filter (capture all traffic)")
    print("2. Filter by protocol (TCP, UDP, ICMP)")
    print("3. Filter by source or destination IP")
    print("4. Filter by port number")
    
    choice = input("Enter your choice (1-4): ").strip()
    if choice == "1":
        return None
    elif choice == "2":
        protocol = input("Enter protocol to filter (TCP/UDP/ICMP): ").strip().upper()
        return protocol.lower() if protocol in ["TCP", "UDP", "ICMP"] else None
    elif choice == "3":
        ip = input("Enter the IP address to filter: ").strip()
        return f"host {ip}"
    elif choice == "4":
        port = input("Enter the port number to filter: ").strip()
        return f"port {port}"
    else:
        return None
