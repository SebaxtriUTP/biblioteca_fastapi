import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from main import app, _services


@pytest.fixture
def mock_db_session():
    """Crear un objeto de sesión de base de datos simulado."""
    mock_db = MagicMock()
    yield mock_db
    mock_db.close.assert_called_once()


@pytest.fixture
def client():
    """Inicializar el cliente de pruebas."""
    client = TestClient(app)
    return client


# Test para crear un libro
def test_create_book(client, mock_db_session):
    # Simular un libro que sería retornado por el servicio
    mock_book = MagicMock()
    mock_book.id = 1
    mock_book.title = "Test Book"
    mock_book.author = "Test Author"

    # Simular el servicio `create_book`
    _services.create_book = MagicMock(return_value=mock_book)

    # Crear un libro
    response = client.post("/api/books/", json={"title": "Test Book", "author": "Test Author"})

    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Test Book", "author": "Test Author"}


# Test para obtener todos los libros
def test_get_books(client, mock_db_session):
    # Simular la lista de libros
    mock_books = [
        {"id": 1, "title": "Test Book 1", "author": "Author 1"},
        {"id": 2, "title": "Test Book 2", "author": "Author 2"}
    ]

    # Simular el servicio `get_all_books`
    _services.get_all_books = MagicMock(return_value=mock_books)

    # Obtener todos los libros
    response = client.get("/api/books/")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json() == mock_books


# Test para obtener un libro por ID
def test_get_book_by_id(client, mock_db_session):
    # Simular un libro que sería retornado por el servicio
    mock_book = {"id": 1, "title": "Test Book", "author": "Test Author"}

    # Simular el servicio `get_book`
    _services.get_book = MagicMock(return_value=mock_book)

    # Obtener un libro por ID
    response = client.get("/api/books/1")

    assert response.status_code == 200
    assert response.json() == mock_book


# Test para obtener libros por autor
def test_get_books_by_author(client, mock_db_session):
    # Simular libros por autor
    mock_books = [
        {"id": 1, "title": "Book by Author", "author": "Test Author"}
    ]

    # Simular el servicio `get_book_by_author`
    _services.get_book_by_author = MagicMock(return_value=mock_books)

    # Obtener libros por autor
    response = client.get("/api/books/author/Test Author")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json() == mock_books


# Test para obtener libros por título
def test_get_books_by_title(client, mock_db_session):
    # Simular libros por título
    mock_books = [
        {"id": 1, "title": "Test Book Title", "author": "Test Author"}
    ]

    # Simular el servicio `get_book_by_title`
    _services.get_book_by_title = MagicMock(return_value=mock_books)

    # Obtener libros por título
    response = client.get("/api/books/title/Test Book Title")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json() == mock_books


# Test para eliminar un libro
def test_delete_book(client, mock_db_session):
    # Simular el libro a eliminar
    mock_book = {"id": 1, "title": "Test Book", "author": "Test Author"}

    # Simular el servicio `get_book` para encontrar el libro
    _services.get_book = MagicMock(return_value=mock_book)
    # Simular el servicio `delete_book`
    _services.delete_book = MagicMock()

    # Eliminar el libro
    response = client.delete("/api/books/1")

    assert response.status_code == 200
    assert response.json() == "Book deleted successfully"


# Test para actualizar un libro
def test_update_book(client, mock_db_session):
    # Simular el libro original
    mock_book = {"id": 1, "title": "Old Book Title", "author": "Old Author"}

    # Simular el libro actualizado
    mock_updated_book = {"id": 1, "title": "Updated Book Title", "author": "Updated Author"}

    # Simular el servicio `get_book` para encontrar el libro
    _services.get_book = MagicMock(return_value=mock_book)
    # Simular el servicio `update_book`
    _services.update_book = MagicMock(return_value=mock_updated_book)

    # Actualizar el libro
    response = client.put("/api/books/1", json={"title": "Updated Book Title", "author": "Updated Author"})

    assert response.status_code == 200
    assert response.json() == mock_updated_book
