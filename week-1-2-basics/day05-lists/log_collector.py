"""
Exercise 3: Log Entry Collector

Task: Collect and manage log entries using lists.

Requirements:
1. Create an empty list for logs
2. Add 5 log entries from user
3. Display all logs
4. Show first and last log
5. Count total logs
"""

print("=== Log Entry Collector ===\n")

# Initialize empty log list
logs = []

# Collect log entries
print("Enter 5 log entries:")
for i in range(5):
    log_entry = input(f"Log {i+1}: ")
    logs.append(log_entry)

# Display all logs
print("\n" + "="*50)
print("ALL LOG ENTRIES")
print("="*50)
for i, log in enumerate(logs, 1):
    print(f"{i}. {log}")
print("="*50)

# Show first and last
print(f"\nFirst log: {logs[0]}")
print(f"Last log:  {logs[-1]}")

# Count logs
print(f"\nTotal log entries: {len(logs)}")

# Search for keyword
keyword = input("\nSearch logs for keyword: ")
matching_logs = []

for log in logs:
    if keyword.lower() in log.lower():
        matching_logs.append(log)

if matching_logs:
    print(f"\nFound {len(matching_logs)} matching log(s):")
    for log in matching_logs:
        print(f"  - {log}")
else:
    print(f"\nNo logs found containing '{keyword}'")

# Bonus: Reverse the logs
print("\nLogs in reverse order:")
for i, log in enumerate(reversed(logs), 1):
    print(f"{i}. {log}")
