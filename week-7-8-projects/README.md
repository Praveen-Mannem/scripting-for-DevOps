# Week 7-8: Real DevOps Projects

Build production-ready automation scripts that solve real DevOps problems.

## Overview

This week, you'll build three complete projects that demonstrate all the skills you've learned:
1. **Automated Backup System** - File management and scheduling
2. **Server Health Monitor** - System monitoring with alerts
3. **Deployment Automation** - CI/CD pipeline automation

These projects are portfolio-worthy and can be used in real production environments!

---

## Project 1: Automated Backup System

### Features
- Create timestamped backups
- Compress files into ZIP archives
- Rotate old backups (keep only N recent)
- Schedule automatic backups
- Email notifications
- Backup verification
- Restore functionality

### Technologies
- `zipfile` - Compression
- `shutil` - File operations
- `datetime` - Timestamps
- `schedule` - Task scheduling
- `smtplib` - Email alerts

### Use Cases
- Database backups
- Configuration backups
- Log archival
- Code repository backups
- Document backups

### Code Structure
```
backup-automation/
├── backup.py          # Main backup script
├── config.json        # Backup configuration
├── restore.py         # Restore from backup
├── schedule_backup.py # Automated scheduling
└── README.md          # Documentation
```

### Key Features to Implement
```python
class BackupManager:
    def create_backup(source, destination)
    def compress_backup(backup_path)
    def rotate_backups(keep_count=5)
    def verify_backup(backup_path)
    def send_notification(status, details)
    def restore_backup(backup_path, restore_to)
```

---

## Project 2: Server Health Monitor

### Features
- Monitor CPU, memory, disk usage
- Track network statistics
- Check running processes
- Alert on thresholds
- Generate health reports
- Historical data tracking
- Dashboard visualization
- Multi-server support

### Technologies
- `psutil` - System monitoring
- `requests` - API integration
- `matplotlib` - Graphs (optional)
- `sqlite3` - Data storage
- `smtplib` - Email alerts

### Use Cases
- Production server monitoring
- Resource usage tracking
- Capacity planning
- Performance optimization
- Incident detection

### Code Structure
```
health-monitor/
├── monitor.py         # Main monitoring script
├── alerts.py          # Alert system
├── database.py        # Data storage
├── report.py          # Report generation
├── config.yaml        # Configuration
└── README.md          # Documentation
```

### Key Features to Implement
```python
class ServerMonitor:
    def check_cpu()
    def check_memory()
    def check_disk()
    def check_network()
    def check_processes()
    def generate_report()
    def send_alerts()
    def store_metrics()
```

---

## Project 3: Deployment Automation

### Features
- Pull latest code from Git
- Run tests automatically
- Build applications
- Deploy to servers
- Rollback on failure
- Deployment logging
- Slack/email notifications
- Multi-environment support

### Technologies
- `subprocess` - Run commands
- `git` - Version control
- `paramiko` - SSH connections
- `fabric` - Remote execution
- `requests` - API calls

### Use Cases
- Web application deployment
- Microservices deployment
- Configuration updates
- Database migrations
- Blue-green deployments

### Code Structure
```
deployment-script/
├── deploy.py          # Main deployment script
├── rollback.py        # Rollback functionality
├── test_runner.py     # Test execution
├── notify.py          # Notifications
├── config/            # Environment configs
│   ├── production.json
│   ├── staging.json
│   └── development.json
└── README.md          # Documentation
```

### Key Features to Implement
```python
class Deployer:
    def pull_code()
    def run_tests()
    def build_application()
    def deploy_to_server()
    def verify_deployment()
    def rollback()
    def send_notification()
    def log_deployment()
```

---

## Complete Project Examples

### Example 1: Full Backup Script

```python
import os
import zipfile
import shutil
from datetime import datetime
from pathlib import Path

class BackupManager:
    def __init__(self, source_dir, backup_dir, keep_count=5):
        self.source_dir = Path(source_dir)
        self.backup_dir = Path(backup_dir)
        self.keep_count = keep_count
        self.backup_dir.mkdir(parents=True, exist_ok=True)
    
    def create_backup(self):
        """Create a timestamped backup"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}.zip"
        backup_path = self.backup_dir / backup_name
        
        print(f"Creating backup: {backup_name}")
        
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.source_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(self.source_dir)
                    zipf.write(file_path, arcname)
                    print(f"  Added: {arcname}")
        
        size_mb = backup_path.stat().st_size / (1024 * 1024)
        print(f"Backup created: {backup_path} ({size_mb:.2f} MB)")
        
        return backup_path
    
    def rotate_backups(self):
        """Keep only the latest N backups"""
        backups = sorted(
            self.backup_dir.glob('backup_*.zip'),
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )
        
        if len(backups) > self.keep_count:
            for old_backup in backups[self.keep_count:]:
                print(f"Removing old backup: {old_backup.name}")
                old_backup.unlink()
    
    def verify_backup(self, backup_path):
        """Verify backup integrity"""
        try:
            with zipfile.ZipFile(backup_path, 'r') as zipf:
                corrupt = zipf.testzip()
                if corrupt:
                    print(f"Corrupt file found: {corrupt}")
                    return False
                print("Backup verification successful")
                return True
        except zipfile.BadZipFile:
            print("Backup file is corrupted")
            return False
    
    def list_backups(self):
        """List all available backups"""
        backups = sorted(
            self.backup_dir.glob('backup_*.zip'),
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )
        
        print("\nAvailable Backups:")
        print("-" * 60)
        for backup in backups:
            size_mb = backup.stat().st_size / (1024 * 1024)
            mtime = datetime.fromtimestamp(backup.stat().st_mtime)
            print(f"{backup.name:30} {size_mb:8.2f} MB  {mtime}")
        print("-" * 60)
        
        return backups
    
    def restore_backup(self, backup_path, restore_to):
        """Restore from a backup"""
        restore_path = Path(restore_to)
        restore_path.mkdir(parents=True, exist_ok=True)
        
        print(f"Restoring backup to: {restore_path}")
        
        with zipfile.ZipFile(backup_path, 'r') as zipf:
            zipf.extractall(restore_path)
        
        print("Restore completed successfully")
    
    def run_backup(self):
        """Run complete backup process"""
        print("=" * 60)
        print("BACKUP PROCESS STARTED")
        print("=" * 60)
        
        # Create backup
        backup_path = self.create_backup()
        
        # Verify backup
        if self.verify_backup(backup_path):
            # Rotate old backups
            self.rotate_backups()
            
            # List current backups
            self.list_backups()
            
            print("\n✅ Backup completed successfully!")
            return True
        else:
            print("\n❌ Backup failed verification!")
            return False

# Usage
if __name__ == "__main__":
    manager = BackupManager(
        source_dir="C:\\MyProject",
        backup_dir="C:\\Backups",
        keep_count=3
    )
    
    manager.run_backup()
```

---

### Example 2: Complete Health Monitor

```python
import psutil
import time
from datetime import datetime
import json

class ServerMonitor:
    def __init__(self, thresholds=None):
        self.thresholds = thresholds or {
            'cpu': 80,
            'memory': 80,
            'disk': 80
        }
        self.alerts = []
    
    def get_cpu_info(self):
        """Get CPU usage information"""
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()
        
        return {
            'percent': cpu_percent,
            'count': cpu_count,
            'frequency_mhz': cpu_freq.current if cpu_freq else None,
            'status': 'critical' if cpu_percent > self.thresholds['cpu'] else 'ok'
        }
    
    def get_memory_info(self):
        """Get memory usage information"""
        memory = psutil.virtual_memory()
        
        return {
            'total_gb': memory.total / (1024**3),
            'available_gb': memory.available / (1024**3),
            'used_gb': memory.used / (1024**3),
            'percent': memory.percent,
            'status': 'critical' if memory.percent > self.thresholds['memory'] else 'ok'
        }
    
    def get_disk_info(self):
        """Get disk usage information"""
        disk = psutil.disk_usage('/')
        
        return {
            'total_gb': disk.total / (1024**3),
            'used_gb': disk.used / (1024**3),
            'free_gb': disk.free / (1024**3),
            'percent': disk.percent,
            'status': 'critical' if disk.percent > self.thresholds['disk'] else 'ok'
        }
    
    def get_network_info(self):
        """Get network statistics"""
        net_io = psutil.net_io_counters()
        
        return {
            'bytes_sent_mb': net_io.bytes_sent / (1024**2),
            'bytes_recv_mb': net_io.bytes_recv / (1024**2),
            'packets_sent': net_io.packets_sent,
            'packets_recv': net_io.packets_recv
        }
    
    def get_process_info(self):
        """Get top processes by CPU and memory"""
        processes = []
        
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        # Sort by CPU usage
        top_cpu = sorted(processes, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:5]
        
        # Sort by memory usage
        top_memory = sorted(processes, key=lambda x: x['memory_percent'] or 0, reverse=True)[:5]
        
        return {
            'top_cpu': top_cpu,
            'top_memory': top_memory
        }
    
    def check_health(self):
        """Perform complete health check"""
        cpu = self.get_cpu_info()
        memory = self.get_memory_info()
        disk = self.get_disk_info()
        network = self.get_network_info()
        processes = self.get_process_info()
        
        # Check for alerts
        if cpu['status'] == 'critical':
            self.alerts.append(f"⚠️ CPU usage high: {cpu['percent']}%")
        
        if memory['status'] == 'critical':
            self.alerts.append(f"⚠️ Memory usage high: {memory['percent']}%")
        
        if disk['status'] == 'critical':
            self.alerts.append(f"⚠️ Disk usage high: {disk['percent']}%")
        
        return {
            'timestamp': datetime.now().isoformat(),
            'cpu': cpu,
            'memory': memory,
            'disk': disk,
            'network': network,
            'processes': processes,
            'alerts': self.alerts
        }
    
    def generate_report(self):
        """Generate formatted health report"""
        health = self.check_health()
        
        report = f"""
{'='*70}
SERVER HEALTH REPORT
{'='*70}
Timestamp: {health['timestamp']}

CPU:
  Usage: {health['cpu']['percent']}%
  Cores: {health['cpu']['count']}
  Status: {health['cpu']['status'].upper()}

Memory:
  Total: {health['memory']['total_gb']:.2f} GB
  Used: {health['memory']['used_gb']:.2f} GB
  Available: {health['memory']['available_gb']:.2f} GB
  Usage: {health['memory']['percent']}%
  Status: {health['memory']['status'].upper()}

Disk:
  Total: {health['disk']['total_gb']:.2f} GB
  Used: {health['disk']['used_gb']:.2f} GB
  Free: {health['disk']['free_gb']:.2f} GB
  Usage: {health['disk']['percent']}%
  Status: {health['disk']['status'].upper()}

Network:
  Sent: {health['network']['bytes_sent_mb']:.2f} MB
  Received: {health['network']['bytes_recv_mb']:.2f} MB

Top CPU Processes:
"""
        for proc in health['processes']['top_cpu']:
            report += f"  {proc['name']:30} {proc['cpu_percent']:6.1f}%\n"
        
        if health['alerts']:
            report += f"\n{'='*70}\nALERTS:\n"
            for alert in health['alerts']:
                report += f"{alert}\n"
        else:
            report += f"\n✅ All systems normal\n"
        
        report += f"{'='*70}\n"
        
        return report
    
    def save_report(self, filename='health_report.json'):
        """Save health data to JSON file"""
        health = self.check_health()
        
        with open(filename, 'w') as f:
            json.dump(health, f, indent=2)
        
        print(f"Report saved to {filename}")

# Usage
if __name__ == "__main__":
    monitor = ServerMonitor(thresholds={
        'cpu': 70,
        'memory': 75,
        'disk': 80
    })
    
    print(monitor.generate_report())
    monitor.save_report()
```

---

## Project Requirements

### Required Libraries
```bash
pip install psutil          # System monitoring
pip install requests        # API calls
pip install python-dotenv   # Environment variables
pip install schedule        # Task scheduling
pip install paramiko        # SSH connections
pip install pyyaml          # YAML configuration
```

### Optional Libraries
```bash
pip install matplotlib      # Graphs
pip install pandas          # Data analysis
pip install slack-sdk       # Slack notifications
pip install boto3           # AWS integration
```

---

## Best Practices for Projects

1. **Code Organization**
   - Use classes for complex logic
   - Separate concerns (monitoring, alerting, reporting)
   - Create reusable functions
   - Follow PEP 8 style guide

2. **Configuration**
   - Use config files (JSON, YAML)
   - Support environment variables
   - Provide sensible defaults
   - Document all options

3. **Error Handling**
   - Handle all exceptions
   - Provide meaningful error messages
   - Log errors properly
   - Implement retry logic

4. **Logging**
   - Log all important events
   - Use appropriate log levels
   - Include timestamps
   - Rotate log files

5. **Testing**
   - Test edge cases
   - Validate inputs
   - Test error handling
   - Create sample data

6. **Documentation**
   - Write clear README
   - Document functions
   - Provide usage examples
   - Include troubleshooting guide

---

## Deployment Checklist

- [ ] Code is well-organized and documented
- [ ] All dependencies are listed
- [ ] Configuration is externalized
- [ ] Error handling is comprehensive
- [ ] Logging is implemented
- [ ] Tests are written
- [ ] README is complete
- [ ] Security best practices followed
- [ ] Performance is optimized
- [ ] Code is version controlled

---

## Next Steps After Completion

1. **Enhance Projects**
   - Add web dashboards
   - Implement databases
   - Add more integrations
   - Improve performance

2. **Learn Advanced Topics**
   - Async programming
   - Multi-threading
   - Database operations
   - Message queues

3. **Explore DevOps Tools**
   - Docker
   - Kubernetes
   - Ansible
   - Terraform

4. **Build Portfolio**
   - Publish on GitHub
   - Write blog posts
   - Create videos
   - Contribute to open source

---

**Congratulations on completing the course! You're now ready to automate the world! 🚀**
