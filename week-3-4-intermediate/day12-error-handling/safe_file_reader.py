"""
Exercise 1: Safe File Reader

Task: Read files with proper error handling.
"""

def read_file_safely(filename):
    """Read a file with error handling."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"✗ ERROR: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"✗ ERROR: No permission to read '{filename}'")
        return None
    except Exception as e:
        print(f"✗ ERROR: Unexpected error: {e}")
        return None

print("=== Safe File Reader ===\n")

# Test with existing file
print("Test 1: Reading existing file")
content = read_file_safely('test_config.txt')
if content:
    print(f"✓ File read successfully")
    print(f"Content: {content[:50]}...")

# Test with non-existent file
print("\nTest 2: Reading non-existent file")
content = read_file_safely('nonexistent.txt')

# Create a test file and read it
print("\nTest 3: Creating and reading new file")
try:
    with open('test_config.txt', 'w') as file:
        file.write("server=localhost\nport=8080\nenv=production")
    print("✓ Test file created")
    
    content = read_file_safely('test_config.txt')
    if content:
        print("✓ File read successfully")
        print(f"Content:\n{content}")
except Exception as e:
    print(f"✗ Error creating file: {e}")
