# server_monitor.py
# Week 1-2 Final Project: Server Monitoring Dashboard

"""
Server Monitoring Dashboard
----------------------------
This script monitors multiple servers and displays their health status.
It combines concepts from Week 1-2: variables, lists, dictionaries, 
conditions, loops, and functions.
"""

def check_health(name, cpu, memory, disk):
    """
    Check if a server is healthy based on resource usage.
    
    Args:
        name (str): Server name
        cpu (int): CPU usage percentage
        memory (int): Memory usage percentage
        disk (int): Disk usage percentage
    
    Returns:
        str: Health status (HEALTHY, WARNING, or CRITICAL)
    """
    if cpu > 80 or memory > 80 or disk > 80:
        return "🔴 CRITICAL"
    elif cpu > 60 or memory > 60 or disk > 60:
        return "🟡 WARNING"
    else:
        return "🟢 HEALTHY"


def calculate_average(cpu, memory, disk):
    """Calculate average resource usage."""
    total = cpu + memory + disk
    average = total / 3
    return round(average, 2)


def print_server_status(server):
    """Print formatted status for a single server."""
    status = check_health(
        server["name"],
        server["cpu"],
        server["memory"],
        server["disk"]
    )
    
    avg = calculate_average(server["cpu"], server["memory"], server["disk"])
    
    print(f"\n{server['name']}")
    print(f"  CPU: {server['cpu']}% | Memory: {server['memory']}% | Disk: {server['disk']}%")
    print(f"  Average: {avg}%")
    print(f"  Status: {status}")


def print_dashboard(servers):
    """Print complete monitoring dashboard."""
    print("=" * 60)
    print(" " * 15 + "SERVER MONITORING DASHBOARD")
    print("=" * 60)
    
    # Initialize counters
    healthy_count = 0
    warning_count = 0
    critical_count = 0
    
    # Check each server
    for server in servers:
        print_server_status(server)
        
        status = check_health(
            server["name"],
            server["cpu"],
            server["memory"],
            server["disk"]
        )
        
        if "HEALTHY" in status:
            healthy_count += 1
        elif "WARNING" in status:
            warning_count += 1
        else:
            critical_count += 1
    
    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total Servers: {len(servers)}")
    print(f"🟢 Healthy: {healthy_count}")
    print(f"🟡 Warning: {warning_count}")
    print(f"🔴 Critical: {critical_count}")
    print("=" * 60)
    
    # Overall status
    if critical_count > 0:
        print("\n⚠️  ACTION REQUIRED: Some servers need immediate attention!")
    elif warning_count > 0:
        print("\n⚡ NOTICE: Some servers are approaching capacity")
    else:
        print("\n✅ ALL SYSTEMS OPERATIONAL")


def main():
    """Main function to run the monitoring dashboard."""
    
    # Server data (in real scenario, this would come from monitoring tools)
    servers = [
        {
            "name": "web-server-1",
            "cpu": 45,
            "memory": 55,
            "disk": 40
        },
        {
            "name": "web-server-2",
            "cpu": 85,
            "memory": 70,
            "disk": 60
        },
        {
            "name": "database-server-1",
            "cpu": 60,
            "memory": 90,
            "disk": 75
        },
        {
            "name": "app-server-1",
            "cpu": 30,
            "memory": 40,
            "disk": 35
        },
        {
            "name": "cache-server-1",
            "cpu": 25,
            "memory": 50,
            "disk": 30
        }
    ]
    
    # Display dashboard
    print_dashboard(servers)


if __name__ == "__main__":
    main()


# ============================================================================
# EXERCISES TO EXTEND THIS PROJECT
# ============================================================================

"""
1. Add more servers to the list and test the dashboard

2. Add a new metric (e.g., network usage) to each server

3. Create a function to find the server with highest CPU usage

4. Add timestamp to show when the report was generated

5. Save the report to a text file

6. Add color coding using ANSI escape codes (advanced)

7. Create a function to send alerts for critical servers

8. Add historical data tracking (store previous readings)

9. Calculate trends (is usage increasing or decreasing?)

10. Create a web-based dashboard using HTML (very advanced!)
"""


# ============================================================================
# EXAMPLE EXTENSIONS
# ============================================================================

# Extension 1: Find server with highest CPU
def find_highest_cpu(servers):
    """Find the server with highest CPU usage."""
    highest = servers[0]
    for server in servers:
        if server["cpu"] > highest["cpu"]:
            highest = server
    return highest

# Extension 2: Add timestamp
from datetime import datetime

def print_dashboard_with_time(servers):
    """Print dashboard with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nReport Generated: {timestamp}")
    print_dashboard(servers)

# Extension 3: Save to file
def save_report_to_file(servers, filename="server_report.txt"):
    """Save monitoring report to a file."""
    with open(filename, "w") as file:
        file.write("SERVER MONITORING REPORT\n")
        file.write("=" * 60 + "\n")
        
        for server in servers:
            status = check_health(
                server["name"],
                server["cpu"],
                server["memory"],
                server["disk"]
            )
            
            file.write(f"\n{server['name']}\n")
            file.write(f"  CPU: {server['cpu']}%\n")
            file.write(f"  Memory: {server['memory']}%\n")
            file.write(f"  Disk: {server['disk']}%\n")
            file.write(f"  Status: {status}\n")
    
    print(f"\nReport saved to {filename}")


# ============================================================================
# INTERACTIVE VERSION
# ============================================================================

def interactive_monitor():
    """Interactive version that lets you add servers manually."""
    servers = []
    
    print("=== Interactive Server Monitor ===")
    print("Add servers to monitor (type 'done' when finished)\n")
    
    while True:
        name = input("Server name (or 'done'): ")
        if name.lower() == 'done':
            break
        
        try:
            cpu = int(input("CPU usage %: "))
            memory = int(input("Memory usage %: "))
            disk = int(input("Disk usage %: "))
            
            servers.append({
                "name": name,
                "cpu": cpu,
                "memory": memory,
                "disk": disk
            })
            
            print(f"✅ Added {name}\n")
        
        except ValueError:
            print("❌ Invalid input. Please enter numbers for usage percentages.\n")
    
    if servers:
        print("\n")
        print_dashboard(servers)
    else:
        print("No servers added.")


# Uncomment to run interactive version:
# interactive_monitor()
