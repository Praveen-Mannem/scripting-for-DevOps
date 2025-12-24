"""
Exercise 2: Port Scanner Simulator

Task: Simulate a port scanner using lists.

Requirements:
1. Create a list of common ports
2. Display all ports to scan
3. Mark some ports as open
4. Display scan results
"""

print("=== Port Scanner Simulator ===\n")

# Common ports to scan
ports_to_scan = [21, 22, 23, 25, 80, 443, 3306, 5432, 8080, 27017]

print("Ports to scan:")
print(ports_to_scan)
print(f"Total ports: {len(ports_to_scan)}")

# Simulate scanning (mark some as open)
open_ports = []
closed_ports = []

print("\nScanning ports...")
for port in ports_to_scan:
    # Simulate: common ports are open
    if port in [22, 80, 443]:
        open_ports.append(port)
        print(f"Port {port}: OPEN ✓")
    else:
        closed_ports.append(port)
        print(f"Port {port}: CLOSED ✗")

# Display results
print("\n" + "="*40)
print("SCAN RESULTS")
print("="*40)
print(f"Open Ports:   {open_ports}")
print(f"Closed Ports: {closed_ports}")
print(f"Total Open:   {len(open_ports)}")
print(f"Total Closed: {len(closed_ports)}")
print("="*40)

# Security check
if 23 in open_ports:  # Telnet
    print("\n⚠️  WARNING: Telnet (port 23) is open - security risk!")

if 22 in open_ports:  # SSH
    print("✓ SSH (port 22) is open - good for remote access")

# Bonus: Find highest port number
highest_port = max(ports_to_scan)
lowest_port = min(ports_to_scan)
print(f"\nPort range: {lowest_port} - {highest_port}")
