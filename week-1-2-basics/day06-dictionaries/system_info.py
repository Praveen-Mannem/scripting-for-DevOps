"""
Exercise 3: System Info Collector

Task: Collect and display system information using dictionaries.
"""

print("=== System Information Collector ===\n")

# Collect system info (simulated)
system_info = {}

print("Enter system information:")
system_info["hostname"] = input("Hostname: ")
system_info["os"] = input("Operating System: ")
system_info["kernel"] = input("Kernel Version: ")
system_info["cpu_model"] = input("CPU Model: ")
system_info["cpu_cores"] = int(input("CPU Cores: "))
system_info["memory_gb"] = int(input("Memory (GB): "))
system_info["disk_gb"] = int(input("Disk Space (GB): "))

# Display formatted system info
print("\n" + "="*50)
print("SYSTEM INFORMATION REPORT")
print("="*50)
print(f"Hostname:        {system_info['hostname']}")
print(f"OS:              {system_info['os']}")
print(f"Kernel:          {system_info['kernel']}")
print(f"CPU:             {system_info['cpu_model']}")
print(f"CPU Cores:       {system_info['cpu_cores']}")
print(f"Memory:          {system_info['memory_gb']} GB")
print(f"Disk Space:      {system_info['disk_gb']} GB")
print("="*50)

# Calculate totals
total_cores = system_info['cpu_cores']
total_memory = system_info['memory_gb']
total_disk = system_info['disk_gb']

print(f"\nTotal Resources:")
print(f"  {total_cores} CPU cores")
print(f"  {total_memory} GB RAM")
print(f"  {total_disk} GB Storage")

# System classification
if total_memory >= 32 and total_cores >= 8:
    classification = "High-Performance Server"
elif total_memory >= 16 and total_cores >= 4:
    classification = "Standard Server"
else:
    classification = "Basic Server"

print(f"\nClassification: {classification}")

# Add metadata
system_info["classification"] = classification
system_info["total_resources"] = f"{total_cores}C/{total_memory}GB/{total_disk}GB"

print(f"\nTotal keys in dictionary: {len(system_info)}")
