# Day 8: Personal Notes

## What I Learned Today
- 
- 
- 

## Key Concepts
1. **for loops**: Iterate through sequences
2. **while loops**: Repeat while condition is true
3. **break**: Exit loop early
4. **continue**: Skip to next iteration
5. **enumerate()**: Get index while looping

## Loop Cheatsheet
```python
# For loop - list
for item in list:
    print(item)

# For loop - range
for i in range(5):  # 0 to 4
    print(i)

# For loop - with index
for index, item in enumerate(list):
    print(f"{index}: {item}")

# While loop
while condition:
    # code
    # update condition

# Break - exit loop
for i in range(10):
    if i == 5:
        break

# Continue - skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)

# Loop through dictionary
for key, value in dict.items():
    print(f"{key}: {value}")
```

## DevOps Use Cases
- **Multi-server operations**: Process multiple servers
- **Log processing**: Iterate through log entries
- **Retry logic**: Attempt operations multiple times
- **Batch operations**: Perform same action on many items

## Practice Summary
- [ ] Completed multi_server_monitor.py
- [ ] Completed log_processor.py
- [ ] Completed retry_mechanism.py

## Tomorrow's Preview
Day 9-10: Functions - Organize code into reusable blocks
