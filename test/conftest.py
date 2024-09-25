from datetime import datetime
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app.app import create_app, db
from app.Model.todo import Todo
from app.todo.logic import check_description_length


@pytest.fixture
def app():
    app = create_app(sqlite=True)
    app.config.update({
        "TESTING": True
    })

    # アプリケーションコンテキストを使用してテスト用DBを作成
    with app.app_context():
        db.create_all()

    yield app  # テストの実行

    # テスト終了後、テスト用DBを削除（インメモリの場合のみ）
    with app.app_context():
        if app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///:memory:":
            db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
