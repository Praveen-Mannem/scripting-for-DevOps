"""
Exercise 1: Multi-Server Monitor

Task: Monitor multiple servers using loops.
"""

print("=== Multi-Server Monitor ===\n")

# Server list with details
servers = [
    {"name": "web-01", "ip": "192.168.1.10", "status": "running"},
    {"name": "web-02", "ip": "192.168.1.11", "status": "running"},
    {"name": "db-01", "ip": "192.168.1.20", "status": "stopped"},
    {"name": "cache-01", "ip": "192.168.1.30", "status": "running"},
    {"name": "api-01", "ip": "192.168.1.40", "status": "running"}
]

print("Monitoring servers...\n")

# Monitor each server
healthy_count = 0
unhealthy_count = 0

for index, server in enumerate(servers, 1):
    print(f"[{index}/{len(servers)}] Checking {server['name']} ({server['ip']})...")
    
    if server['status'] == "running":
        print(f"  ✓ Status: RUNNING")
        healthy_count += 1
    else:
        print(f"  ✗ Status: STOPPED")
        unhealthy_count += 1
    print()

# Summary
print("="*50)
print("MONITORING SUMMARY")
print("="*50)
print(f"Total Servers:    {len(servers)}")
print(f"Healthy:          {healthy_count}")
print(f"Unhealthy:        {unhealthy_count}")
print("="*50)

# List unhealthy servers
if unhealthy_count > 0:
    print("\n⚠️ Servers requiring attention:")
    for server in servers:
        if server['status'] != "running":
            print(f"  - {server['name']} ({server['ip']})")
else:
    print("\n✓ All servers are healthy!")
