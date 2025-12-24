"""
Exercise 3: Performance Metrics Calculator

Task: Calculate statistics from performance data.

Requirements:
1. Get 5 CPU usage readings from user
2. Calculate average, minimum, maximum
3. Calculate range and variance
4. Display formatted statistics
"""

print("=== Performance Metrics Calculator ===\n")

# Collect 5 CPU readings
print("Enter 5 CPU usage readings (0-100%):")
readings = []
for i in range(5):
    reading = float(input(f"Reading {i+1}: "))
    readings.append(reading)

# Calculate statistics
average = sum(readings) / len(readings)
minimum = min(readings)
maximum = max(readings)
range_value = maximum - minimum

# Calculate variance (how spread out the data is)
variance = sum((x - average) ** 2 for x in readings) / len(readings)

# Display results
print("\n" + "="*40)
print("PERFORMANCE STATISTICS")
print("="*40)
print(f"Readings:   {readings}")
print(f"Average:    {average:.2f}%")
print(f"Minimum:    {minimum:.2f}%")
print(f"Maximum:    {maximum:.2f}%")
print(f"Range:      {range_value:.2f}%")
print(f"Variance:   {variance:.2f}")
print("="*40)

# Performance assessment
if average < 50:
    print("\n✓ Performance is good (low CPU usage)")
elif average < 75:
    print("\n⚠️  Performance is moderate")
else:
    print("\n🚨 Performance is poor (high CPU usage)")

# Check for spikes
if range_value > 30:
    print(f"⚠️  Large variation detected ({range_value:.2f}%)")
