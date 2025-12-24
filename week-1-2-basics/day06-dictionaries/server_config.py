"""
Exercise 1: Server Configuration Manager

Task: Manage server configuration using dictionaries.
"""

print("=== Server Configuration Manager ===\n")

# Server configuration
server_config = {
    "hostname": "prod-web-01",
    "ip_address": "192.168.1.100",
    "port": 8080,
    "status": "running",
    "cpu_cores": 4,
    "memory_gb": 16,
    "environment": "production"
}

# Display configuration
print("Current Server Configuration:")
print("="*50)
for key, value in server_config.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
print("="*50)

# Update configuration
print("\n--- Updating Configuration ---")
server_config["status"] = "maintenance"
server_config["memory_gb"] = 32  # Upgraded memory
server_config["last_updated"] = "2024-12-24"

print("✓ Status changed to maintenance")
print("✓ Memory upgraded to 32GB")
print("✓ Last updated timestamp added")

# Display updated configuration
print("\nUpdated Configuration:")
print("="*50)
for key, value in server_config.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
print("="*50)

# Check specific values
print(f"\nServer is in {server_config['environment']} environment")
print(f"Total resources: {server_config['cpu_cores']} cores, {server_config['memory_gb']}GB RAM")

# Safe access with get()
backup_status = server_config.get("backup_enabled", "Not configured")
print(f"Backup status: {backup_status}")
