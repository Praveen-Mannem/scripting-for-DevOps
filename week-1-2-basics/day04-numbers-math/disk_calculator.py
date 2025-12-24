"""
Exercise 1: Disk Space Calculator

Task: Create a script that calculates disk space usage and availability.

Requirements:
1. Get total disk space from user (in GB)
2. Get used disk space from user (in GB)
3. Calculate available space
4. Calculate usage percentage
5. Display all information formatted nicely
"""

import math

print("=== Disk Space Calculator ===\n")

# Get disk information
total_disk = float(input("Enter total disk space (GB): "))
used_disk = float(input("Enter used disk space (GB): "))

# Calculate metrics
available_disk = total_disk - used_disk
usage_percentage = (used_disk / total_disk) * 100

# Display results
print("\n" + "="*40)
print("DISK SPACE REPORT")
print("="*40)
print(f"Total Space:     {total_disk} GB")
print(f"Used Space:      {used_disk} GB")
print(f"Available Space: {available_disk} GB")
print(f"Usage:           {usage_percentage:.2f}%")
print("="*40)

# Warning if usage is high
if usage_percentage > 80:
    print("\n⚠️  WARNING: Disk usage is above 80%!")
elif usage_percentage > 90:
    print("\n🚨 CRITICAL: Disk usage is above 90%!")
else:
    print("\n✓ Disk usage is healthy")

# Bonus: Calculate how much more can be used
remaining_percentage = 100 - usage_percentage
print(f"\nYou can use {remaining_percentage:.2f}% more space")
