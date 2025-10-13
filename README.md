# FastAPI Server Configuration Test API

This is a FastAPI project for testing server configurations with automated deployment workflows.

## Features

- Test firewall outbound connectivity
- Retrieve process manager details
- Check Nginx server status
- API-based server configuration testing
- Containerized deployment with Docker
- GitHub Actions CI/CD workflows
- VM deployment via SSH
- Artifact management for container releases

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- Psutil
- Requests
- Docker (for containerization)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd fastapi-test
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Check if the server is running
- `GET /test/firewall` - Test firewall outbound connectivity
- `GET /test/process-manager` - Retrieve process manager details
- `GET /test/nginx` - Check Nginx server status

## GitHub Actions Workflows

This repository includes GitHub Actions workflows for different deployment scenarios:

### 1. Syntax Check (`syntax-check.yml`)
- Checks Python syntax errors
- Runs basic code style checking

### 2. CI/CD Workflow (`blank.yml`)
- Tests the application across multiple Python versions
- Lints the code
- Deploys to production when tests pass

### 3. VM Deployment (`deploy-vm.yml`)
- Deploys to a VM via SSH
- Executes git pull on the remote server
- Automatically restarts the systemd service after code updates

### 4. Container Deployment (`deploy-container.yml`)
- Builds Docker container images
- Creates release artifacts with detailed descriptions
- Stores artifacts in GitHub releases with version tracking

### 5. General Deployment (`deploy.yml`)
- General deployment workflow for production environments

## Deployment Options

### Container Deployment with Artifact Management

The container deployment workflow creates Docker image artifacts stored as GitHub releases with detailed descriptions including commit information, timestamps, and version tracking. Each release contains a .tar file of the Docker image that can be loaded and run on any Docker-enabled system.

### VM Deployment via SSH

The VM deployment workflow:
- Pulls the latest code from the repository
- Updates dependencies in the virtual environment
- Restarts the systemd service to load new code changes

## Docker Configuration

The project includes:
- A `Dockerfile` for containerization
- A `docker-compose.yml` for alternative deployment
- Proper port mapping configuration

## Configuration for Deployments

### For VM Deployment
- Ensure the systemd service file is properly configured
- The service should be set to restart automatically
- SSH access must be configured with appropriate keys

### For Container Deployment
- Docker must be installed on the target system
- Proper port mappings should be configured
- Container images can be loaded from GitHub release artifacts

## Testing

Run the tests using pytest:
```bash
python -m pytest test_main.py -v
```

## Project Structure

```
fastapi-test/
├── main.py                 # Main FastAPI application
├── test_main.py           # API tests
├── Dockerfile             # Container configuration
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
├── nginx.conf             # Nginx configuration template
├── .github/
│   └── workflows/        # GitHub Actions workflows
└── README.md
```

## Architecture

The application provides endpoints for testing different aspects of a server configuration:
- Network connectivity (firewall testing)
- Process management (system resources)
- Service availability (Nginx status)

All deployment workflows are designed to be secure and maintainable for production use.

## License

This project is licensed under the MIT License.