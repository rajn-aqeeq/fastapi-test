from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server is running"}

def test_test_firewall():
    response = client.get("/test/firewall")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "firewall_status" in data

def test_test_process_manager():
    response = client.get("/test/process-manager")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "process_info" in data

def test_test_nginx():
    response = client.get("/test/nginx")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "nginx_status" in data