# tests/integration_tests/test_api.py
import requests

def test_api_status():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert "userId" in response.json()