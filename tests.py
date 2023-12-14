from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_predict_positive():
    response = client.get("/get_text",
                          params={"text": "Я обожаю API и программную инженерию"})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    response = client.get("/get_text",
                          params={"text": "у меня ничего не получается"})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data['label'] == 'NEGATIVE'