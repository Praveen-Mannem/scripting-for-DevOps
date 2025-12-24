"""
Exercise 3: Alert System

Task: Generate alerts based on system metrics.
"""

print("=== Alert System ===\n")

# Get metrics
cpu = float(input("CPU usage (%): "))
memory = float(input("Memory usage (%): "))
disk = float(input("Disk usage (%): "))
response_time = float(input("Response time (ms): "))

print("\n" + "="*50)
print("ALERT MONITORING")
print("="*50)

alert_count = 0

# CPU alerts
if cpu > 90:
    print("\n🚨 CRITICAL ALERT: CPU usage above 90%")
    print(f"   Current: {cpu}%")
    print("   Action: Scale up immediately")
    alert_count += 1
elif cpu > 75:
    print("\n⚠️ WARNING: CPU usage above 75%")
    print(f"   Current: {cpu}%")
    print("   Action: Monitor closely")
    alert_count += 1

# Memory alerts
if memory > 90:
    print("\n🚨 CRITICAL ALERT: Memory usage above 90%")
    print(f"   Current: {memory}%")
    print("   Action: Restart services or add memory")
    alert_count += 1
elif memory > 75:
    print("\n⚠️ WARNING: Memory usage above 75%")
    print(f"   Current: {memory}%")
    print("   Action: Investigate memory leaks")
    alert_count += 1

# Disk alerts
if disk > 90:
    print("\n🚨 CRITICAL ALERT: Disk usage above 90%")
    print(f"   Current: {disk}%")
    print("   Action: Clean up logs or expand disk")
    alert_count += 1
elif disk > 80:
    print("\n⚠️ WARNING: Disk usage above 80%")
    print(f"   Current: {disk}%")
    print("   Action: Plan disk expansion")
    alert_count += 1

# Response time alerts
if response_time > 1000:
    print("\n🚨 CRITICAL ALERT: Response time above 1000ms")
    print(f"   Current: {response_time}ms")
    print("   Action: Check application performance")
    alert_count += 1
elif response_time > 500:
    print("\n⚠️ WARNING: Response time above 500ms")
    print(f"   Current: {response_time}ms")
    print("   Action: Monitor application")
    alert_count += 1

# Summary
print("\n" + "="*50)
if alert_count == 0:
    print("✓ ALL SYSTEMS NORMAL - No alerts")
else:
    print(f"⚠️ TOTAL ALERTS: {alert_count}")
    if alert_count >= 3:
        print("🚨 MULTIPLE ALERTS - Immediate attention required!")
print("="*50)
