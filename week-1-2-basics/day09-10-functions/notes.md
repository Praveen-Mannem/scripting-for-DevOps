# Day 9-10: Personal Notes

## What I Learned Today
- 
- 
- 

## Key Concepts
1. **Functions**: Reusable blocks of code
2. **Parameters**: Input values for functions
3. **Return values**: Output from functions
4. **Default parameters**: Optional parameters with defaults
5. **Docstrings**: Function documentation

## Functions Cheatsheet
```python
# Basic function
def function_name():
    # code
    pass

# Function with parameters
def greet(name):
    print(f"Hello, {name}")

# Function with return value
def add(a, b):
    return a + b

# Function with default parameter
def deploy(app, env="dev"):
    print(f"Deploying {app} to {env}")

# Function with multiple returns
def get_info():
    return "web-01", "192.168.1.10"

# Call function
result = add(5, 3)
name, ip = get_info()

# Docstring
def my_function():
    """
    This is a docstring.
    It explains what the function does.
    """
    pass
```

## DevOps Use Cases
- **Reusable utilities**: Common operations
- **Monitoring functions**: Check health, calculate metrics
- **Deployment helpers**: Automate deployment steps
- **Code organization**: Break complex scripts into functions

## Practice Summary
- [ ] Completed server_functions.py
- [ ] Completed monitoring_utils.py
- [ ] Completed deployment_helper.py

## Key Benefits of Functions
- **Reusability**: Write once, use many times
- **Organization**: Break complex code into manageable pieces
- **Testing**: Easier to test individual functions
- **Maintenance**: Update in one place
- **Readability**: Clear, descriptive function names

## Tomorrow's Preview
Week 3-4: File handling, error handling, modules, JSON/YAML
