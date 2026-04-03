# Python Port Scanner

A simple cybersecurity tool that scans open ports on a target system using Python. This project is designed for educational purposes and authorized security testing.

## Features

- **Fast port scanning** - Efficiently scans multiple ports
- **Multithreading support** - Uses up to 100 concurrent threads for faster scanning
- **Domain name resolution** - Automatically resolves domain names to IP addresses
- **Custom port range scanning** - Scan any range of ports (1-65535)
- **Simple CLI interface** - Easy-to-use command-line interface
- **Error handling** - Graceful handling of network errors and invalid inputs
- **Progress tracking** - Real-time display of open ports as they're discovered

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only built-in libraries)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/python-port-scanner.git
cd python-port-scanner
```

2. Run the scanner:
```bash
python port_scanner.py
```

## Usage

1. Run the program:
```bash
python port_scanner.py
```

2. Enter the target (IP address or domain name):
```
Enter target (IP or domain): scanme.nmap.org
```

3. Enter the port range to scan:
```
Enter start port: 1
Enter end port: 100
```

4. Wait for the scan to complete and view the results.

## Example Output

```
==================================================
===       Python Port Scanner                  ===
==================================================

Enter target (IP or domain): scanme.nmap.org
Enter start port: 1
Enter end port: 100

Scanning target: scanme.nmap.org
Resolved IP: 45.33.32.156

Start Time: 2026-04-03 20:15:00

Port 22 is OPEN
Port 80 is OPEN

Scan completed. Found 2 open port(s).
Total time taken: 2.84 seconds
```

## How It Works

1. **Input Validation** - Validates target and port range inputs
2. **DNS Resolution** - Resolves domain names to IP addresses using `socket.gethostbyname()`
3. **Multithreaded Scanning** - Creates multiple threads to scan ports concurrently
4. **Port Probing** - Attempts TCP connection to each port with a timeout
5. **Result Display** - Shows open ports in real-time and provides summary statistics

## Technical Details

- **Threading**: Uses up to 100 concurrent threads for optimal performance
- **Socket Timeout**: 1 second timeout per port to prevent hanging
- **Thread Safety**: Implements locks for thread-safe printing and data collection
- **Queue Management**: Uses `Queue` for efficient work distribution among threads

## Common Port Numbers

Here are some commonly scanned ports:

- **21** - FTP (File Transfer Protocol)
- **22** - SSH (Secure Shell)
- **23** - Telnet
- **25** - SMTP (Email)
- **53** - DNS (Domain Name System)
- **80** - HTTP (Web)
- **443** - HTTPS (Secure Web)
- **3306** - MySQL Database
- **3389** - RDP (Remote Desktop)
- **8080** - HTTP Alternate

## Limitations

- Only scans TCP ports (UDP scanning not supported)
- Firewall rules may block scan attempts
- Some systems may detect and block port scanning activity
- Scanning speed depends on network conditions and target responsiveness

## Disclaimer

⚠️ **IMPORTANT**: This tool is created for **educational purposes** and **authorized security testing only**.

- Only scan systems you own or have explicit permission to test
- Unauthorized port scanning may be illegal in your jurisdiction
- The author is not responsible for misuse of this tool
- Always follow ethical hacking guidelines and local laws

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Author

[Vishal Rathod]

## Acknowledgments

- Built with Python's built-in libraries
- Inspired by the need for simple security testing tools
- Thanks to the cybersecurity community for educational resources
#
