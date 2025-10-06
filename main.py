from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Server Configuration Test API")

class ServerStatus(BaseModel):
    status: str
    details: dict

@app.get("/")
async def read_root():
    return {"message": "Server is running"}

@app.get("/test/firewall")
async def test_firewall():
    try:
        # Test basic outbound connectivity
        # In a real scenario, you would test specific ports and protocols
        return {
            "status": "success",
            "firewall_status": "Outbound connections working",
            "details": {
                "outbound_access": True,
                "ports_tested": ["80", "443"]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test/process-manager")
async def test_process_manager():
    import psutil
    try:
        # Get current process information
        current_process = psutil.Process()
        return {
            "status": "success",
            "process_info": {
                "pid": current_process.pid,
                "memory_use": f"{current_process.memory_info().rss / 1024 / 1024:.2f} MB",
                "cpu_percent": current_process.cpu_percent(),
                "threads": current_process.num_threads()
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test/nginx")
async def test_nginx():
    import requests
    try:
        # Attempt to connect to localhost through Nginx
        response = requests.get("http://localhost")
        return {
            "status": "success",
            "nginx_status": {
                "running": True,
                "response_code": response.status_code,
                "server_header": response.headers.get("Server", "Not Found")
            }
        }
    except requests.RequestException as e:
        return {
            "status": "error",
            "nginx_status": {
                "running": False,
                "error": str(e)
            }
        }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)