import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi_tutorial.ex28_sql_databases.database import Base
from fastapi_tutorial.ex28_sql_databases.main import app, get_db


class TestSQL:
  
    def setup_class(self):

        SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

        engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, echo=True
        )
        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        Base.metadata.create_all(bind=engine)

        def override_get_db():
            try:
                db = TestingSessionLocal()
                yield db
            finally:
                db.close()

        app.dependency_overrides[get_db] = override_get_db

        self.client = TestClient(app)
        
    def test_create_user(self):
        response = self.client.post(
            "/users/",
            json={"email": "deadpool@example.com", "password": "chimichangas4life"},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "deadpool@example.com"
        assert "id" in data
        user_id = data["id"]

        response = self.client.get(f"/users/{user_id}")
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "deadpool@example.com"
        assert data["id"] == user_id
        
    def teardown_class(self):
        if os.path.exists('./test.db'):
            os.remove('./test.db')

