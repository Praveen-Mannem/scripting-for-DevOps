"""
Exercise 2: Environment Validator

Task: Validate deployment based on environment.
"""

print("=== Environment Validator ===\n")

# Get deployment details
app_name = input("Application name: ")
environment = input("Environment (dev/staging/prod): ").lower()
version = input("Version: ")

print("\n" + "="*50)
print("DEPLOYMENT VALIDATION")
print("="*50)

# Validate environment
if environment not in ["dev", "staging", "prod"]:
    print("✗ ERROR: Invalid environment!")
    print("  Valid environments: dev, staging, prod")
else:
    print(f"✓ Environment: {environment}")
    
    # Environment-specific checks
    if environment == "prod":
        print("\n🔒 PRODUCTION DEPLOYMENT")
        print("  - Requires approval")
        print("  - Backup will be created")
        print("  - Rollback plan required")
        
        confirmation = input("\nType 'DEPLOY' to confirm: ")
        if confirmation == "DEPLOY":
            print(f"\n✓ Deploying {app_name} v{version} to PRODUCTION")
        else:
            print("\n✗ Deployment cancelled")
            
    elif environment == "staging":
        print("\n⚠️ STAGING DEPLOYMENT")
        print("  - Testing environment")
        print("  - No approval required")
        print(f"\n✓ Deploying {app_name} v{version} to STAGING")
        
    else:  # dev
        print("\n🔧 DEVELOPMENT DEPLOYMENT")
        print("  - Development environment")
        print("  - Auto-deploy enabled")
        print(f"\n✓ Deploying {app_name} v{version} to DEVELOPMENT")

print("="*50)
