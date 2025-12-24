"""
Exercise 3: Backup Creator

Task: Create backups of important files.
"""

import os
from datetime import datetime

print("=== Backup Creator ===\n")

# Create sample files to backup
sample_files = {
    'app_config.txt': 'database=localhost\nport=5432\nuser=admin',
    'server_list.txt': 'web-01\nweb-02\ndb-01\ncache-01',
    'env_vars.txt': 'APP_ENV=production\nDEBUG=false\nLOG_LEVEL=info'
}

print("Creating sample files...")
for filename, content in sample_files.items():
    with open(filename, 'w') as file:
        file.write(content)
    print(f"  ✓ Created {filename}")

# Create backup directory
backup_dir = 'backups'
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
    print(f"\n✓ Created backup directory: {backup_dir}")

# Create timestamp for backup
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Backup each file
print(f"\nBacking up files (timestamp: {timestamp})...")
backed_up_files = []

for filename in sample_files.keys():
    if os.path.exists(filename):
        # Read original file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Create backup filename
        backup_filename = f"{filename}.backup_{timestamp}"
        backup_path = os.path.join(backup_dir, backup_filename)
        
        # Write backup
        with open(backup_path, 'w') as file:
            file.write(content)
        
        backed_up_files.append(backup_filename)
        print(f"  ✓ Backed up: {filename} → {backup_filename}")

# Create backup manifest
manifest_path = os.path.join(backup_dir, f'manifest_{timestamp}.txt')
with open(manifest_path, 'w') as file:
    file.write(f"Backup Manifest\n")
    file.write(f"Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"="*50 + "\n\n")
    file.write(f"Files backed up:\n")
    for filename in backed_up_files:
        file_path = os.path.join(backup_dir, filename)
        file_size = os.path.getsize(file_path)
        file.write(f"  - {filename} ({file_size} bytes)\n")

print(f"\n✓ Backup manifest created: manifest_{timestamp}.txt")

# Display summary
print("\n" + "="*50)
print("BACKUP SUMMARY")
print("="*50)
print(f"Files backed up: {len(backed_up_files)}")
print(f"Backup location: {backup_dir}/")
print(f"Timestamp: {timestamp}")
print("="*50)
