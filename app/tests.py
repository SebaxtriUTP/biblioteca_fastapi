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

