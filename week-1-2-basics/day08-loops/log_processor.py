"""
Exercise 2: Log File Processor

Task: Process log entries using loops.
"""

print("=== Log File Processor ===\n")

# Simulated log entries
log_entries = [
    "[INFO] Application started",
    "[ERROR] Database connection failed",
    "[INFO] User logged in",
    "[WARNING] High memory usage detected",
    "[ERROR] API request timeout",
    "[INFO] Backup completed successfully",
    "[WARNING] Disk space low",
    "[INFO] Cache cleared",
    "[ERROR] Authentication failed",
    "[INFO] Server shutdown initiated"
]

print(f"Processing {len(log_entries)} log entries...\n")

# Count by severity
info_count = 0
warning_count = 0
error_count = 0

# Process each log
for index, log in enumerate(log_entries, 1):
    print(f"[{index}] {log}")
    
    # Count by type
    if "[INFO]" in log:
        info_count += 1
    elif "[WARNING]" in log:
        warning_count += 1
    elif "[ERROR]" in log:
        error_count += 1

# Summary
print("\n" + "="*50)
print("LOG ANALYSIS SUMMARY")
print("="*50)
print(f"Total Entries:  {len(log_entries)}")
print(f"INFO:           {info_count}")
print(f"WARNING:        {warning_count}")
print(f"ERROR:          {error_count}")
print("="*50)

# Show errors only
if error_count > 0:
    print("\n🚨 ERROR ENTRIES:")
    for log in log_entries:
        if "[ERROR]" in log:
            print(f"  {log}")

# Show warnings only
if warning_count > 0:
    print("\n⚠️ WARNING ENTRIES:")
    for log in log_entries:
        if "[WARNING]" in log:
            print(f"  {log}")

# Health assessment
if error_count == 0 and warning_count == 0:
    print("\n✓ No issues found in logs")
elif error_count > 0:
    print(f"\n🚨 Action required: {error_count} error(s) detected")
else:
    print(f"\n⚠️ Monitor: {warning_count} warning(s) detected")
