"""
Exercise 2: Configuration File Writer

Task: Create and manage configuration files.
"""

print("=== Configuration File Writer ===\n")

# Get configuration from user
print("Enter server configuration:")
hostname = input("Hostname: ")
ip_address = input("IP Address: ")
port = input("Port: ")
environment = input("Environment: ")

# Write configuration file
config_content = f"""# Server Configuration
# Generated: 2024-12-24

[SERVER]
hostname = {hostname}
ip_address = {ip_address}
port = {port}
environment = {environment}

[DATABASE]
db_host = localhost
db_port = 5432
db_name = myapp_db

[LOGGING]
log_level = INFO
log_file = /var/log/app.log
"""

# Write to file
with open('server_config.ini', 'w') as file:
    file.write(config_content)

print("\n✓ Configuration written to server_config.ini")

# Read and display
print("\nConfiguration file contents:")
print("="*50)
with open('server_config.ini', 'r') as file:
    print(file.read())
print("="*50)

# Append additional settings
print("\nAdding backup configuration...")
with open('server_config.ini', 'a') as file:
    file.write("\n[BACKUP]\n")
    file.write("backup_enabled = true\n")
    file.write("backup_schedule = daily\n")
    file.write("backup_retention = 7\n")

print("✓ Backup configuration appended")

# Display updated file
print("\nUpdated configuration:")
print("="*50)
with open('server_config.ini', 'r') as file:
    print(file.read())
print("="*50)
