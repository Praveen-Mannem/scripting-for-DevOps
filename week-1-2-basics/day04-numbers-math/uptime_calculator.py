"""
Exercise 2: Server Uptime Calculator

Task: Calculate server uptime in different time units.

Requirements:
1. Get uptime in hours from user
2. Convert to days, hours, minutes
3. Calculate uptime percentage (assume 30-day month)
4. Display formatted results
"""

print("=== Server Uptime Calculator ===\n")

# Get uptime in hours
uptime_hours = float(input("Enter server uptime (in hours): "))

# Convert to different units
uptime_days = uptime_hours // 24
remaining_hours = uptime_hours % 24
uptime_minutes = uptime_hours * 60

# Calculate uptime percentage (30-day month = 720 hours)
total_hours_in_month = 30 * 24  # 720 hours
uptime_percentage = (uptime_hours / total_hours_in_month) * 100

# Display results
print("\n" + "="*40)
print("SERVER UPTIME REPORT")
print("="*40)
print(f"Total Uptime:    {uptime_hours} hours")
print(f"Converted:       {int(uptime_days)} days, {int(remaining_hours)} hours")
print(f"In Minutes:      {uptime_minutes:.0f} minutes")
print(f"Uptime %:        {uptime_percentage:.2f}%")
print("="*40)

# Calculate downtime
downtime_hours = total_hours_in_month - uptime_hours
downtime_percentage = 100 - uptime_percentage

print(f"\nDowntime:        {downtime_hours:.2f} hours ({downtime_percentage:.2f}%)")

# SLA check (99.9% uptime)
sla_target = 99.9
if uptime_percentage >= sla_target:
    print(f"✓ Meeting SLA target of {sla_target}%")
else:
    print(f"✗ Below SLA target of {sla_target}%")
