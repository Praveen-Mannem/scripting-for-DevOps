# Day 6: Personal Notes

## What I Learned Today
- 
- 
- 

## Key Concepts
1. **Dictionaries**: Key-value pairs for structured data
2. **Keys**: Must be unique, usually strings
3. **Values**: Can be any data type
4. **Methods**: get(), keys(), values(), items()

## Dictionary Operations Cheatsheet
```python
server = {"name": "web-01", "ip": "192.168.1.10"}

# Access
server["name"]           # Direct access
server.get("ip")         # Safe access
server.get("port", 80)   # With default value

# Modify
server["status"] = "running"  # Add/update
del server["ip"]              # Delete
server.pop("name")            # Remove and return

# Check
"name" in server         # Check if key exists
len(server)              # Count keys

# Iterate
for key in server.keys():
    print(key)
    
for value in server.values():
    print(value)
    
for key, value in server.items():
    print(f"{key}: {value}")
```

## DevOps Use Cases
- **Configuration**: Store server settings
- **Environment vars**: Manage app configuration
- **API responses**: Handle JSON data
- **Metadata**: Store system information

## Practice Summary
- [ ] Completed server_config.py
- [ ] Completed env_manager.py
- [ ] Completed system_info.py

## Tomorrow's Preview
Day 7: Conditional Statements - Make decisions in code
