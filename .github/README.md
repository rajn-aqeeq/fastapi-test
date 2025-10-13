# GitHub Actions Workflows

This directory contains the GitHub Actions workflows for the FastAPI application.

## Workflows

### Test Workflow (`test.yml`)
- Runs tests on multiple operating systems (Ubuntu, Windows, macOS)
- Tests multiple Python versions (3.9, 3.10, 3.11, 3.12, 3.13)
- Generates code coverage reports
- Uploads coverage reports to Codecov

### Development Workflow (`dev.yml`)
- Runs on pushes to development branches
- Checks code formatting with Black
- Lints code with flake8
- Performs type checking with mypy
- Runs security audit with bandit

### Security Workflow (`security.yml`)
- Scans for security vulnerabilities in dependencies
- Scans for secrets in the codebase
- Performs dependency review

### Deployment Workflow (`deploy.yml`)
- Deploys the application to production when changes are pushed to the main branch
- Supports deployment to various platforms (Docker, Heroku, AWS)

### CI/CD Workflow (`blank.yml`)
- Tests the application across multiple Python versions
- Lints the code
- Deploys to production when tests pass