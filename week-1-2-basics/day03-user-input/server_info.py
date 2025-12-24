"""
Exercise 1: Server Information Collector

Task: Create a script that collects server information from the user
and displays it in a formatted way.

Requirements:
1. Ask for server name
2. Ask for IP address
3. Ask for environment (dev/staging/prod)
4. Ask for owner name
5. Display all information in a nice format
"""

# Your code here
print("=== Server Information Collector ===\n")

# Collect information
server_name = input("Enter server name: ")
ip_address = input("Enter IP address: ")
environment = input("Enter environment (dev/staging/prod): ")
owner = input("Enter owner name: ")

# Display formatted output
print("\n" + "="*40)
print("SERVER INFORMATION")
print("="*40)
print(f"Server Name:  {server_name}")
print(f"IP Address:   {ip_address}")
print(f"Environment:  {environment.upper()}")
print(f"Owner:        {owner}")
print("="*40)

# Bonus: Create a summary line
summary = f"{server_name} ({ip_address}) - {environment} - Owner: {owner}"
print(f"\nSummary: {summary}")
