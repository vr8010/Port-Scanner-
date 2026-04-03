#!/usr/bin/env python3
"""
Python Port Scanner
A simple cybersecurity tool for scanning open ports on target systems.
Author: [Your Name]
"""

import socket
import threading
import sys
from datetime import datetime
from queue import Queue

# Configuration
THREAD_LIMIT = 100
SOCKET_TIMEOUT = 1

# Thread-safe queue for port numbers
port_queue = Queue()
# Thread-safe list for open ports
open_ports = []
# Lock for thread-safe printing
print_lock = threading.Lock()


def resolve_target(target):
    """
    Resolve domain name to IP address.
    
    Args:
        target (str): Domain name or IP address
        
    Returns:
        str: Resolved IP address
        
    Raises:
        socket.gaierror: If hostname cannot be resolved
    """
    try:
        ip_address = socket.gethostbyname(target)
        return ip_address
    except socket.gaierror:
        raise Exception(f"Unable to resolve hostname: {target}")


def scan_port(target_ip, port):
    """
    Attempt to connect to a specific port on the target.
    
    Args:
        target_ip (str): Target IP address
        port (int): Port number to scan
        
    Returns:
        bool: True if port is open, False otherwise
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(SOCKET_TIMEOUT)
        
        # Attempt connection
        result = sock.connect_ex((target_ip, port))
        sock.close()
        
        return result == 0
    except socket.error:
        return False


def worker(target_ip):
    """
    Worker thread function to scan ports from the queue.
    
    Args:
        target_ip (str): Target IP address
    """
    while not port_queue.empty():
        port = port_queue.get()
        
        if scan_port(target_ip, port):
            with print_lock:
                print(f"Port {port} is OPEN")
                open_ports.append(port)
        
        port_queue.task_done()


def validate_port(port_str, port_type):
    """
    Validate and convert port string to integer.
    
    Args:
        port_str (str): Port number as string
        port_type (str): Type of port (start/end) for error messages
        
    Returns:
        int: Valid port number
        
    Raises:
        ValueError: If port is invalid
    """
    try:
        port = int(port_str)
        if port < 1 or port > 65535:
            raise ValueError(f"Port must be between 1 and 65535")
        return port
    except ValueError:
        raise ValueError(f"Invalid {port_type} port: {port_str}")


def main():
    """
    Main function to run the port scanner.
    """
    print("=" * 50)
    print("=== Python Port Scanner ===".center(50))
    print("=" * 50)
    print()
    
    try:
        # Get user input
        target = input("Enter target (IP or domain): ").strip()
        if not target:
            print("Error: Target cannot be empty")
            sys.exit(1)
        
        start_port_str = input("Enter start port: ").strip()
        end_port_str = input("Enter end port: ").strip()
        
        # Validate ports
        start_port = validate_port(start_port_str, "start")
        end_port = validate_port(end_port_str, "end")
        
        if start_port > end_port:
            print("Error: Start port must be less than or equal to end port")
            sys.exit(1)
        
        print()
        print(f"Scanning target: {target}")
        
        # Resolve target to IP
        target_ip = resolve_target(target)
        print(f"Resolved IP: {target_ip}")
        print()
        
        # Record start time
        start_time = datetime.now()
        print(f"Start Time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Fill the queue with port numbers
        for port in range(start_port, end_port + 1):
            port_queue.put(port)
        
        # Create and start threads
        threads = []
        thread_count = min(THREAD_LIMIT, end_port - start_port + 1)
        
        for _ in range(thread_count):
            thread = threading.Thread(target=worker, args=(target_ip,))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        # Wait for all threads to complete
        port_queue.join()
        
        # Calculate duration
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        
        print()
        if open_ports:
            print(f"Scan completed. Found {len(open_ports)} open port(s).")
        else:
            print("Scan completed. No open ports found.")
        
        print(f"Total time taken: {duration:.2f} seconds")
        print()
        
    except KeyboardInterrupt:
        print("\n\nScan interrupted by user (Ctrl+C)")
        print("Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
