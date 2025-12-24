"""
Exercise 1: Log File Reader

Task: Read and analyze a log file.
"""

import os

# Create sample log file
log_content = """[2024-12-24 10:00:00] INFO: Application started
[2024-12-24 10:05:23] WARNING: High memory usage detected
[2024-12-24 10:10:45] ERROR: Database connection failed
[2024-12-24 10:15:12] INFO: Retry attempt 1
[2024-12-24 10:15:30] INFO: Database connection established
[2024-12-24 10:20:00] WARNING: Slow response time detected
[2024-12-24 10:25:15] ERROR: API timeout
[2024-12-24 10:30:00] INFO: Application running normally
"""

# Write sample log file
with open('server.log', 'w') as file:
    file.write(log_content)

print("=== Log File Reader ===\n")

# Read and analyze log file
print("Reading server.log...\n")

error_count = 0
warning_count = 0
info_count = 0
errors = []

with open('server.log', 'r') as file:
    for line_num, line in enumerate(file, 1):
        line = line.strip()
        
        if 'ERROR' in line:
            error_count += 1
            errors.append(line)
        elif 'WARNING' in line:
            warning_count += 1
        elif 'INFO' in line:
            info_count += 1

# Display analysis
print("="*50)
print("LOG ANALYSIS REPORT")
print("="*50)
print(f"Total Lines:  {line_num}")
print(f"INFO:         {info_count}")
print(f"WARNING:      {warning_count}")
print(f"ERROR:        {error_count}")
print("="*50)

# Show errors
if errors:
    print("\n🚨 ERROR ENTRIES:")
    for error in errors:
        print(f"  {error}")

# Write summary to file
with open('log_summary.txt', 'w') as file:
    file.write("LOG ANALYSIS SUMMARY\n")
    file.write("="*50 + "\n")
    file.write(f"Total Lines: {line_num}\n")
    file.write(f"INFO: {info_count}\n")
    file.write(f"WARNING: {warning_count}\n")
    file.write(f"ERROR: {error_count}\n")

print("\n✓ Summary written to log_summary.txt")
