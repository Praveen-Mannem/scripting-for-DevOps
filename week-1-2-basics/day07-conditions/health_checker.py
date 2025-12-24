"""
Exercise 1: Server Health Checker

Task: Check server health based on multiple metrics.
"""

print("=== Server Health Checker ===\n")

# Get server metrics
print("Enter server metrics:")
cpu_usage = float(input("CPU usage (%): "))
memory_usage = float(input("Memory usage (%): "))
disk_usage = float(input("Disk usage (%): "))
status = input("Server status (running/stopped): ").lower()

print("\n" + "="*50)
print("HEALTH CHECK REPORT")
print("="*50)

# Check CPU
print("\nCPU Status:")
if cpu_usage < 70:
    print(f"  ✓ CPU: {cpu_usage}% - Healthy")
elif cpu_usage < 85:
    print(f"  ⚠️ CPU: {cpu_usage}% - Warning")
else:
    print(f"  🚨 CPU: {cpu_usage}% - Critical")

# Check Memory
print("\nMemory Status:")
if memory_usage < 70:
    print(f"  ✓ Memory: {memory_usage}% - Healthy")
elif memory_usage < 85:
    print(f"  ⚠️ Memory: {memory_usage}% - Warning")
else:
    print(f"  🚨 Memory: {memory_usage}% - Critical")

# Check Disk
print("\nDisk Status:")
if disk_usage < 70:
    print(f"  ✓ Disk: {disk_usage}% - Healthy")
elif disk_usage < 85:
    print(f"  ⚠️ Disk: {disk_usage}% - Warning")
else:
    print(f"  🚨 Disk: {disk_usage}% - Critical")

# Overall health
print("\n" + "="*50)
print("OVERALL HEALTH:")
if status != "running":
    print("  🚨 CRITICAL: Server is not running!")
elif cpu_usage > 85 or memory_usage > 85 or disk_usage > 85:
    print("  🚨 CRITICAL: One or more metrics in critical state")
elif cpu_usage > 70 or memory_usage > 70 or disk_usage > 70:
    print("  ⚠️ WARNING: Monitoring required")
else:
    print("  ✓ HEALTHY: All systems normal")
print("="*50)
