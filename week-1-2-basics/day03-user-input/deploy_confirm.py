"""
Exercise 3: Deployment Confirmation Script

Task: Create a script that asks for confirmation before deployment.

Requirements:
1. Show deployment details
2. Ask for confirmation (yes/no)
3. Display appropriate message based on response
"""

# Your code here
print("=== Deployment Confirmation ===\n")

# Get deployment details
app_name = input("Enter application name: ")
environment = input("Enter environment (dev/staging/prod): ")
version = input("Enter version to deploy: ")

# Show deployment summary
print("\n" + "="*50)
print("DEPLOYMENT SUMMARY")
print("="*50)
print(f"Application:  {app_name}")
print(f"Environment:  {environment.upper()}")
print(f"Version:      {version}")
print("="*50)

# Ask for confirmation
confirmation = input("\nDo you want to proceed? (yes/no): ")

# Process confirmation
if confirmation.lower() == "yes":
    print(f"\n✓ Deploying {app_name} v{version} to {environment}...")
    print("Deployment initiated!")
else:
    print("\n✗ Deployment cancelled.")

# Bonus: Show what was entered
print(f"\nYou entered: '{confirmation}'")
print(f"Lowercase version: '{confirmation.lower()}'")
print(f"Stripped version: '{confirmation.strip()}'")
