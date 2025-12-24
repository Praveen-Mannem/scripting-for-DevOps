"""
Exercise 3: Deployment Helper

Task: Create functions to help with deployments.
"""

def validate_environment(env):
    """Validate if environment is valid."""
    valid_envs = ["dev", "staging", "prod"]
    return env.lower() in valid_envs

def get_deployment_config(environment):
    """Get configuration based on environment."""
    configs = {
        "dev": {
            "requires_approval": False,
            "backup_enabled": False,
            "notification": False
        },
        "staging": {
            "requires_approval": False,
            "backup_enabled": True,
            "notification": True
        },
        "prod": {
            "requires_approval": True,
            "backup_enabled": True,
            "notification": True
        }
    }
    return configs.get(environment.lower(), {})

def create_backup(app_name):
    """Simulate creating a backup."""
    backup_name = f"{app_name}_backup_20241224"
    print(f"  📦 Creating backup: {backup_name}")
    return backup_name

def send_notification(app_name, environment, status):
    """Simulate sending a notification."""
    print(f"  📧 Notification sent: {app_name} deployment to {environment} - {status}")

def deploy_application(app_name, version, environment):
    """Deploy application with proper checks and procedures."""
    print(f"\n{'='*50}")
    print(f"DEPLOYING: {app_name} v{version} to {environment.upper()}")
    print(f"{'='*50}")
    
    # Validate environment
    if not validate_environment(environment):
        print("✗ ERROR: Invalid environment")
        return False
    
    # Get configuration
    config = get_deployment_config(environment)
    
    # Check if approval required
    if config['requires_approval']:
        print("\n🔒 Production deployment requires approval")
        approval = input("Type 'APPROVE' to continue: ")
        if approval != "APPROVE":
            print("✗ Deployment cancelled")
            return False
    
    # Create backup if enabled
    if config['backup_enabled']:
        print("\n--- Backup Phase ---")
        backup = create_backup(app_name)
        print(f"  ✓ Backup created: {backup}")
    
    # Deploy
    print("\n--- Deployment Phase ---")
    print(f"  🚀 Deploying {app_name} v{version}...")
    print(f"  ✓ Deployment successful")
    
    # Send notification if enabled
    if config['notification']:
        print("\n--- Notification Phase ---")
        send_notification(app_name, environment, "SUCCESS")
    
    print(f"\n{'='*50}")
    print(f"✓ DEPLOYMENT COMPLETE")
    print(f"{'='*50}")
    return True

# Main program
print("=== Deployment Helper System ===")

# Get deployment details
app_name = input("\nApplication name: ")
version = input("Version: ")
environment = input("Environment (dev/staging/prod): ")

# Execute deployment
success = deploy_application(app_name, version, environment)

if success:
    print(f"\n✓ {app_name} v{version} is now live in {environment}!")
else:
    print(f"\n✗ Deployment failed or was cancelled")
