"""
Exercise 3: Retry Mechanism

Task: Implement retry logic using while loops.
"""

print("=== Retry Mechanism Simulator ===\n")

# Configuration
max_retries = 3
retry_count = 0
success = False

print(f"Attempting to connect to server (max {max_retries} retries)...\n")

# Simulate connection attempts
while retry_count < max_retries and not success:
    retry_count += 1
    print(f"Attempt {retry_count}/{max_retries}...")
    
    # Simulate user input (in real scenario, this would be actual connection)
    result = input("  Connection successful? (yes/no): ").lower()
    
    if result == "yes":
        success = True
        print("  ✓ Connection established!")
    else:
        print("  ✗ Connection failed")
        if retry_count < max_retries:
            print(f"  Retrying... ({max_retries - retry_count} attempts remaining)\n")

# Final result
print("\n" + "="*50)
if success:
    print("✓ SUCCESS: Connected to server")
    print(f"  Attempts used: {retry_count}/{max_retries}")
else:
    print("✗ FAILED: Could not connect to server")
    print(f"  All {max_retries} attempts exhausted")
    print("  Action: Check network connectivity")
print("="*50)

# Bonus: Countdown example
print("\n--- Bonus: Deployment Countdown ---")
countdown = 5
print(f"Deployment starting in {countdown} seconds...")

while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1

print("🚀 Deploying now!")
