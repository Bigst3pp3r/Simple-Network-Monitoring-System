# Filtering mechanisms and options
def get_filter_choice():
    """
    Presents the user with filtering options and returns the chosen filter string.
    Supported options:
    1. No filter
    2. Protocol filter (TCP, UDP, ICMP)
    3. IP address filter
    4. Port number filter
    """
    print("Choose a filter option:")
    print("1. No filter (capture all traffic)")
    print("2. Filter by protocol (TCP, UDP, ICMP)")
    print("3. Filter by source or destination IP")
    print("4. Filter by port number")

    choice = input("Enter your choice (1-4): ").strip()
    if choice == "1":
        return None  # No filter
    elif choice == "2":
        protocol = input("Enter protocol to filter (TCP/UDP/ICMP): ").strip().upper()
        if protocol in ["TCP", "UDP", "ICMP"]:
            return f"{protocol.lower()}"  # Filter by protocol
    elif choice == "3":
        ip = input("Enter the IP address to filter: ").strip()
        return f"host {ip}"  # Filter by IP address
    elif choice == "4":
        port = input("Enter the port number to filter: ").strip()
        return f"port {port}"  # Filter by port
    else:
        print("Invalid choice. Capturing all traffic.")
        return None
