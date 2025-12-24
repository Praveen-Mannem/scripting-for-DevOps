"""
Exercise 2: Log Message Formatter

Task: Create a script that formats log messages with different severity levels.

Requirements:
1. Ask user for log message
2. Ask for severity level (INFO/WARNING/ERROR)
3. Ask for service name
4. Format and display the log message
"""

# Your code here
print("=== Log Message Formatter ===\n")

# Get log details
message = input("Enter log message: ")
severity = input("Enter severity (INFO/WARNING/ERROR): ")
service = input("Enter service name: ")

# Format the log message
# Format: [SEVERITY] ServiceName: Message
formatted_log = f"[{severity.upper()}] {service}: {message}"

print("\nFormatted Log Message:")
print("-" * 50)
print(formatted_log)
print("-" * 50)

# Bonus: Show message length
print(f"\nMessage length: {len(message)} characters")

# Bonus: Show uppercase version
print(f"Uppercase: {formatted_log.upper()}")
