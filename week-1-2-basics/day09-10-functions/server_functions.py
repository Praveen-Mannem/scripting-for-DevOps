"""
Exercise 1: Server Management Functions

Task: Create reusable functions for server management.
"""

def display_server_info(name, ip, status):
    """Display server information in a formatted way."""
    print("="*40)
    print(f"Server: {name}")
    print(f"IP:     {ip}")
    print(f"Status: {status}")
    print("="*40)

def check_server_status(status):
    """Check if server status is healthy."""
    if status.lower() == "running":
        return True
    return False

def calculate_server_count(servers):
    """Calculate total, running, and stopped servers."""
    total = len(servers)
    running = sum(1 for s in servers if s['status'] == 'running')
    stopped = total - running
    return total, running, stopped

def restart_server(server_name):
    """Simulate server restart."""
    print(f"\n🔄 Restarting {server_name}...")
    print(f"✓ {server_name} restarted successfully")
    return "running"

# Main program
print("=== Server Management System ===\n")

# Server data
servers = [
    {"name": "web-01", "ip": "192.168.1.10", "status": "running"},
    {"name": "web-02", "ip": "192.168.1.11", "status": "stopped"},
    {"name": "db-01", "ip": "192.168.1.20", "status": "running"}
]

# Display all servers
print("Current Servers:\n")
for server in servers:
    display_server_info(server['name'], server['ip'], server['status'])
    print()

# Calculate statistics
total, running, stopped = calculate_server_count(servers)
print(f"\nStatistics:")
print(f"  Total:   {total}")
print(f"  Running: {running}")
print(f"  Stopped: {stopped}")

# Restart stopped servers
print("\n--- Restarting Stopped Servers ---")
for server in servers:
    if not check_server_status(server['status']):
        new_status = restart_server(server['name'])
        server['status'] = new_status

# Display updated statistics
total, running, stopped = calculate_server_count(servers)
print(f"\nUpdated Statistics:")
print(f"  Total:   {total}")
print(f"  Running: {running}")
print(f"  Stopped: {stopped}")
