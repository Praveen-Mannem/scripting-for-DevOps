"""
Exercise 2: Monitoring Utilities

Task: Create utility functions for monitoring.
"""

def calculate_percentage(used, total):
    """Calculate percentage of resource usage."""
    return (used / total) * 100

def get_status_icon(percentage, warning_threshold=75, critical_threshold=90):
    """Get status icon based on percentage."""
    if percentage >= critical_threshold:
        return "🚨"
    elif percentage >= warning_threshold:
        return "⚠️"
    else:
        return "✓"

def format_metric(name, value, unit, total=None):
    """Format a metric for display."""
    if total:
        percentage = calculate_percentage(value, total)
        icon = get_status_icon(percentage)
        return f"{icon} {name}: {value}{unit}/{total}{unit} ({percentage:.1f}%)"
    else:
        return f"{name}: {value}{unit}"

def check_threshold(value, threshold, metric_name):
    """Check if value exceeds threshold and return alert."""
    if value > threshold:
        return f"ALERT: {metric_name} ({value}%) exceeds threshold ({threshold}%)"
    return None

def generate_report(metrics):
    """Generate a monitoring report from metrics."""
    print("\n" + "="*50)
    print("MONITORING REPORT")
    print("="*50)
    
    alerts = []
    for metric in metrics:
        print(metric)
        # Check for alerts (if percentage > 80)
        if "%" in metric:
            # Extract percentage
            pct_str = metric.split("(")[1].split("%")[0]
            pct = float(pct_str)
            if pct > 80:
                alerts.append(metric)
    
    print("="*50)
    
    if alerts:
        print("\n⚠️ ALERTS:")
        for alert in alerts:
            print(f"  {alert}")
    else:
        print("\n✓ All metrics within normal range")

# Main program
print("=== Monitoring Utilities Demo ===")

# Collect metrics
cpu_used = 75
cpu_total = 100

memory_used = 12
memory_total = 16

disk_used = 450
disk_total = 500

# Format metrics
metrics = [
    format_metric("CPU", cpu_used, "%", cpu_total),
    format_metric("Memory", memory_used, "GB", memory_total),
    format_metric("Disk", disk_used, "GB", disk_total),
    format_metric("Uptime", 99.9, "%")
]

# Generate report
generate_report(metrics)

# Check individual thresholds
print("\n--- Threshold Checks ---")
alert = check_threshold(cpu_used, 70, "CPU")
if alert:
    print(alert)

alert = check_threshold((memory_used/memory_total)*100, 80, "Memory")
if alert:
    print(alert)

alert = check_threshold((disk_used/disk_total)*100, 85, "Disk")
if alert:
    print(alert)
