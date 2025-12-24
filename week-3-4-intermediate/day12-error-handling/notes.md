# Day 12: Personal Notes

## What I Learned Today
- 
- 
- 

## Key Concepts
1. **try/except**: Catch and handle errors
2. **Multiple except blocks**: Handle different error types
3. **finally**: Code that always runs
4. **raise**: Create custom exceptions

## Error Handling Cheatsheet
```python
# Basic try/except
try:
    # code that might fail
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# Multiple exceptions
try:
    file = open('file.txt')
    value = int(file.read())
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Invalid value")

# Catch all exceptions
try:
    # code
    pass
except Exception as e:
    print(f"Error: {e}")

# Finally block
try:
    # code
    pass
except Exception as e:
    print(f"Error: {e}")
finally:
    # always runs
    print("Cleanup")

# Raise exception
if invalid_condition:
    raise ValueError("Invalid input")
```

## DevOps Use Cases
- **File operations**: Handle missing files
- **Network operations**: Handle connection failures
- **Input validation**: Handle invalid user input
- **API calls**: Handle timeouts and errors

## Practice Summary
- [ ] Completed safe_file_reader.py
- [ ] Completed connection_retry.py
- [ ] Completed input_validator.py

## Tomorrow's Preview
Day 13: Modules and Packages - Organize code into reusable modules
