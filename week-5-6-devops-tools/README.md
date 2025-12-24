# Week 5-6: DevOps-Specific Python

Master Python tools and techniques specifically used in DevOps workflows.

## Overview

This week focuses on Python skills that DevOps engineers use daily:
- Running system commands from Python
- Working with REST APIs
- Managing environment variables
- Interacting with cloud services
- Automation patterns

---

## Topics Covered

### Day 21-23: Running System Commands

**Learn:**
- `subprocess` module
- Running shell commands
- Capturing output
- Error handling
- Cross-platform compatibility

**DevOps Applications:**
- Execute git commands
- Run docker commands
- Manage systemd services
- Check system status
- Automate deployments

**Key Code:**
```python
import subprocess

# Run command and capture output
result = subprocess.run(
    ['ls', '-l'],
    capture_output=True,
    text=True
)

print(result.stdout)
print(f"Exit code: {result.returncode}")

# Run with error handling
try:
    subprocess.run(
        ['docker', 'ps'],
        check=True,
        capture_output=True
    )
except subprocess.CalledProcessError as e:
    print(f"Command failed: {e}")
```

**Real Examples:**
```python
# Check Docker containers
def list_containers():
    result = subprocess.run(
        ['docker', 'ps', '--format', '{{.Names}}'],
        capture_output=True,
        text=True
    )
    return result.stdout.strip().split('\n')

# Git operations
def git_pull():
    result = subprocess.run(
        ['git', 'pull', 'origin', 'main'],
        capture_output=True,
        text=True,
        cwd='/path/to/repo'
    )
    return result.returncode == 0
```

---

### Day 24-26: Working with APIs

**Learn:**
- `requests` library
- GET/POST/PUT/DELETE requests
- Headers and authentication
- JSON responses
- Error handling
- Rate limiting

**DevOps Applications:**
- GitHub API
- Docker Hub API
- Kubernetes API
- Cloud provider APIs (AWS, Azure, GCP)
- Monitoring tools (Prometheus, Grafana)
- CI/CD webhooks

**Key Code:**
```python
import requests

# GET request
response = requests.get('https://api.github.com/repos/python/cpython')
if response.status_code == 200:
    data = response.json()
    print(f"Stars: {data['stargazers_count']}")

# POST request with authentication
headers = {
    'Authorization': 'Bearer YOUR_TOKEN',
    'Content-Type': 'application/json'
}

data = {
    'name': 'new-repo',
    'description': 'Created via API'
}

response = requests.post(
    'https://api.github.com/user/repos',
    json=data,
    headers=headers
)
```

**Real Examples:**
```python
# GitHub API wrapper
class GitHubAPI:
    def __init__(self, token):
        self.base_url = 'https://api.github.com'
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
    
    def get_repo(self, owner, repo):
        url = f'{self.base_url}/repos/{owner}/{repo}'
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def list_issues(self, owner, repo, state='open'):
        url = f'{self.base_url}/repos/{owner}/{repo}/issues'
        params = {'state': state}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

# Docker Hub API
def get_docker_image_tags(image_name):
    url = f'https://hub.docker.com/v2/repositories/{image_name}/tags'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return [tag['name'] for tag in data['results']]
    return []
```

---

### Day 27-28: Environment Variables & Configuration

**Learn:**
- `os.environ` and `os.getenv()`
- `.env` files
- `python-dotenv` library
- Configuration management
- Secrets handling

**DevOps Applications:**
- API keys and tokens
- Database credentials
- Environment-specific configs
- CI/CD variables
- Docker environment variables

**Key Code:**
```python
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Read environment variables
api_key = os.getenv('API_KEY')
db_host = os.getenv('DB_HOST', 'localhost')
debug = os.getenv('DEBUG', 'False') == 'True'

# Set environment variable
os.environ['MY_VAR'] = 'value'

# Check if variable exists
if 'API_KEY' in os.environ:
    print("API key is configured")
```

**Real Examples:**
```python
# Configuration class
class Config:
    def __init__(self):
        load_dotenv()
        
        # Required variables
        self.api_key = os.getenv('API_KEY')
        self.db_host = os.getenv('DB_HOST')
        
        # Optional with defaults
        self.db_port = int(os.getenv('DB_PORT', '5432'))
        self.debug = os.getenv('DEBUG', 'False') == 'True'
        self.environment = os.getenv('ENVIRONMENT', 'development')
    
    def validate(self):
        """Validate required configuration"""
        if not self.api_key:
            raise ValueError("API_KEY environment variable is required")
        if not self.db_host:
            raise ValueError("DB_HOST environment variable is required")
        return True

# Multi-environment configuration
class EnvironmentConfig:
    def __init__(self):
        self.env = os.getenv('ENVIRONMENT', 'development')
        
        if self.env == 'production':
            self.load_production_config()
        elif self.env == 'staging':
            self.load_staging_config()
        else:
            self.load_development_config()
    
    def load_production_config(self):
        self.db_host = os.getenv('PROD_DB_HOST')
        self.api_url = 'https://api.production.com'
        self.debug = False
    
    def load_staging_config(self):
        self.db_host = os.getenv('STAGING_DB_HOST')
        self.api_url = 'https://api.staging.com'
        self.debug = True
    
    def load_development_config(self):
        self.db_host = 'localhost'
        self.api_url = 'http://localhost:8000'
        self.debug = True
```

---

## Week Project: API Integration & Automation

Build a comprehensive automation tool that:
- Integrates with GitHub API
- Manages repositories
- Automates deployments
- Sends notifications
- Uses environment variables for configuration

**Project Features:**
- List repositories
- Create new repositories
- Trigger CI/CD pipelines
- Monitor build status
- Send Slack/email notifications

---

## Essential Libraries

### Install These:
```bash
# HTTP requests
pip install requests

# Environment variables
pip install python-dotenv

# Advanced HTTP client
pip install httpx

# AWS SDK
pip install boto3

# Azure SDK
pip install azure-mgmt-compute

# Google Cloud SDK
pip install google-cloud-storage

# Kubernetes client
pip install kubernetes

# Docker SDK
pip install docker
```

---

## Real-World Examples

### Example 1: AWS S3 Operations
```python
import boto3
from botocore.exceptions import ClientError

class S3Manager:
    def __init__(self):
        self.s3 = boto3.client('s3')
    
    def upload_file(self, file_path, bucket, object_name=None):
        if object_name is None:
            object_name = file_path
        
        try:
            self.s3.upload_file(file_path, bucket, object_name)
            print(f"Uploaded {file_path} to {bucket}/{object_name}")
            return True
        except ClientError as e:
            print(f"Upload failed: {e}")
            return False
    
    def list_buckets(self):
        response = self.s3.list_buckets()
        return [bucket['Name'] for bucket in response['Buckets']]
```

### Example 2: Docker Container Management
```python
import docker

class DockerManager:
    def __init__(self):
        self.client = docker.from_env()
    
    def list_containers(self, all=False):
        containers = self.client.containers.list(all=all)
        return [{
            'id': c.id[:12],
            'name': c.name,
            'status': c.status,
            'image': c.image.tags[0] if c.image.tags else 'none'
        } for c in containers]
    
    def start_container(self, container_name):
        try:
            container = self.client.containers.get(container_name)
            container.start()
            return True
        except docker.errors.NotFound:
            print(f"Container {container_name} not found")
            return False
```

### Example 3: Kubernetes Pod Management
```python
from kubernetes import client, config

class K8sManager:
    def __init__(self):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()
    
    def list_pods(self, namespace='default'):
        pods = self.v1.list_namespaced_pod(namespace)
        return [{
            'name': pod.metadata.name,
            'status': pod.status.phase,
            'ip': pod.status.pod_ip
        } for pod in pods.items]
    
    def get_pod_logs(self, pod_name, namespace='default'):
        return self.v1.read_namespaced_pod_log(
            name=pod_name,
            namespace=namespace
        )
```

---

## Common DevOps Patterns

### Pattern 1: Retry with Exponential Backoff
```python
import time
import requests

def retry_request(url, max_attempts=3, base_delay=1):
    for attempt in range(max_attempts):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt == max_attempts - 1:
                raise
            
            delay = base_delay * (2 ** attempt)
            print(f"Attempt {attempt + 1} failed. Retrying in {delay}s...")
            time.sleep(delay)
```

### Pattern 2: Health Check
```python
def check_service_health(url):
    try:
        response = requests.get(f"{url}/health", timeout=5)
        return {
            'status': 'healthy' if response.status_code == 200 else 'unhealthy',
            'response_time': response.elapsed.total_seconds(),
            'status_code': response.status_code
        }
    except requests.exceptions.RequestException as e:
        return {
            'status': 'down',
            'error': str(e)
        }
```

### Pattern 3: Webhook Handler
```python
from flask import Flask, request
import hmac
import hashlib

app = Flask(__name__)

def verify_signature(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    signature = request.headers.get('X-Hub-Signature-256')
    payload = request.get_data()
    
    if verify_signature(payload, signature, WEBHOOK_SECRET):
        data = request.json
        # Process webhook
        print(f"Received event: {data['action']}")
        return {'status': 'success'}, 200
    
    return {'status': 'unauthorized'}, 401
```

---

## Best Practices

### 1. API Requests
- Always set timeouts
- Handle rate limiting
- Use connection pooling
- Implement retry logic
- Log all API calls

### 2. Environment Variables
- Never commit secrets to git
- Use `.env` files for local development
- Validate required variables on startup
- Use different configs per environment
- Document all required variables

### 3. System Commands
- Check command exists before running
- Handle errors gracefully
- Log command output
- Use absolute paths
- Be careful with shell=True

### 4. Error Handling
- Catch specific exceptions
- Provide meaningful error messages
- Log errors with context
- Implement fallback behavior
- Don't expose sensitive info in errors

---

## Security Considerations

```python
# ❌ BAD - Hardcoded secrets
api_key = "sk-1234567890abcdef"

# ✅ GOOD - From environment
api_key = os.getenv('API_KEY')

# ❌ BAD - SQL injection risk
query = f"SELECT * FROM users WHERE name = '{user_input}'"

# ✅ GOOD - Parameterized query
query = "SELECT * FROM users WHERE name = ?"

# ❌ BAD - Command injection risk
subprocess.run(f"ls {user_input}", shell=True)

# ✅ GOOD - List of arguments
subprocess.run(['ls', user_input])
```

---

## Next Steps

After Week 5-6, you'll be ready to:
- Build production-ready automation scripts
- Integrate with any API
- Manage cloud resources programmatically
- Create CI/CD pipelines
- Build monitoring and alerting systems

**Week 7-8 will bring it all together with real-world projects! 🚀**
