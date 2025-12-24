"""
Exercise 1: Server Manager

Task: Create a server management system using lists.

Requirements:
1. Start with a list of 3 servers
2. Display all servers
3. Add a new server
4. Remove a server
5. Display final list
"""

print("=== Server Manager ===\n")

# Initial server list
servers = ["web-server-01", "db-server-01", "cache-server-01"]

print("Initial Servers:")
for i, server in enumerate(servers, 1):
    print(f"{i}. {server}")

# Add new server
new_server = input("\nEnter new server name to add: ")
servers.append(new_server)

print(f"\n✓ Added {new_server}")
print(f"Total servers: {len(servers)}")

# Display updated list
print("\nUpdated Server List:")
for i, server in enumerate(servers, 1):
    print(f"{i}. {server}")

# Remove a server
remove_server = input("\nEnter server name to remove: ")
if remove_server in servers:
    servers.remove(remove_server)
    print(f"✓ Removed {remove_server}")
else:
    print(f"✗ Server '{remove_server}' not found")

# Display final list
print("\nFinal Server List:")
for i, server in enumerate(servers, 1):
    print(f"{i}. {server}")

print(f"\nTotal servers: {len(servers)}")

# Bonus: Check if specific server exists
check_server = input("\nCheck if server exists: ")
if check_server in servers:
    print(f"✓ {check_server} is in the list")
else:
    print(f"✗ {check_server} is not in the list")
