# Day 5: Personal Notes

## What I Learned Today
- 
- 
- 

## Key Concepts
1. **Lists**: Ordered collections of items
2. **Indexing**: Access items by position (starts at 0)
3. **List methods**: append(), remove(), pop(), insert()
4. **Slicing**: Get portions of lists

## List Operations Cheatsheet
```python
servers = ["web1", "web2", "db1"]

# Access
servers[0]      # First item
servers[-1]     # Last item
servers[1:3]    # Slice (items 1-2)

# Modify
servers.append("cache1")    # Add to end
servers.insert(0, "lb1")    # Insert at position
servers.remove("web1")      # Remove by value
servers.pop()               # Remove last
servers.pop(0)              # Remove first

# Check
len(servers)              # Count items
"web1" in servers         # Check if exists

# Sort
servers.sort()            # Sort alphabetically
servers.reverse()         # Reverse order
```

## DevOps Use Cases
- **Server lists**: Manage multiple servers
- **Port lists**: Track ports to monitor
- **Log entries**: Collect and process logs
- **IP addresses**: Store network information

## Questions/Confusion
- 
- 

## Practice Summary
- [ ] Completed server_manager.py
- [ ] Completed port_scanner.py
- [ ] Completed log_collector.py
- [ ] Experimented with list methods

## Real-World Example
```python
# Manage deployment servers
production_servers = ["prod-web-01", "prod-web-02", "prod-db-01"]

# Add new server
production_servers.append("prod-cache-01")

# Check server count
print(f"Total servers: {len(production_servers)}")

# Deploy to all
for server in production_servers:
    print(f"Deploying to {server}...")
```

## Tomorrow's Preview
Day 6: Dictionaries - Learn key-value pairs for structured data
