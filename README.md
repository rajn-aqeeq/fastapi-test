# FastAPI Test Project

This is a simple FastAPI project to test server configurations.

## Features
- Test firewall outbound connectivity.
- Retrieve process manager details.
- Check Nginx server status.

## Requirements
- Python 3.9+
- FastAPI
- Uvicorn
- Psutil
- Requests

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rajn-aqeeq/fastapi-test.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fastapi-test
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

## API Endpoints
- `GET /` - Check if the server is running.
- `GET /test/firewall` - Test firewall outbound connectivity.
- `GET /test/process-manager` - Retrieve process manager details.
- `GET /test/nginx` - Check Nginx server status.

## License
This project is licensed under the MIT License.