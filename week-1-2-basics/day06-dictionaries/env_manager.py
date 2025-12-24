"""
Exercise 2: Environment Variables Handler

Task: Manage environment variables using dictionaries.
"""

print("=== Environment Variables Manager ===\n")

# Environment variables
env_vars = {
    "APP_NAME": "MyApp",
    "APP_ENV": "development",
    "DB_HOST": "localhost",
    "DB_PORT": "5432",
    "DB_NAME": "myapp_db",
    "DEBUG": "true",
    "LOG_LEVEL": "info"
}

# Display all environment variables
print("Environment Variables:")
print("="*50)
for key, value in env_vars.items():
    print(f"{key} = {value}")
print("="*50)

# Add new variables
print("\n--- Adding New Variables ---")
env_vars["API_KEY"] = "abc123xyz"
env_vars["MAX_CONNECTIONS"] = "100"
print("✓ Added API_KEY")
print("✓ Added MAX_CONNECTIONS")

# Update existing
print("\n--- Switching to Production ---")
env_vars["APP_ENV"] = "production"
env_vars["DB_HOST"] = "prod-db.example.com"
env_vars["DEBUG"] = "false"
env_vars["LOG_LEVEL"] = "warning"

print("✓ Environment switched to production")
print("✓ Database host updated")
print("✓ Debug mode disabled")
print("✓ Log level set to warning")

# Display updated variables
print("\nUpdated Environment Variables:")
print("="*50)
for key, value in env_vars.items():
    print(f"{key} = {value}")
print("="*50)

# Check critical variables
print("\nCritical Settings:")
print(f"  Environment: {env_vars['APP_ENV']}")
print(f"  Database: {env_vars['DB_HOST']}:{env_vars['DB_PORT']}")
print(f"  Debug Mode: {env_vars['DEBUG']}")
