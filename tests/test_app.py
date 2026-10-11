from app import app, initialize_database


def setup_module():
    initialize_database()


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_books_api():
    client = app.test_client()
    response = client.get("/api/books")
    assert response.status_code == 200
