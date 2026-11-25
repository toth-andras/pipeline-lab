from app import app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_index_returns_200():
    response = client().get("/")
    assert response.status_code == 200


def test_index_contains_version():
    payload = client().get("/").get_json()
    assert payload["service"] == "demo-app"
    assert "version" in payload


def test_health_is_ok():
    payload = client().get("/health").get_json()
    assert payload == {"status": "ok"}
