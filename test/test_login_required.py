# TODO
# ログインが必要なページにアクセスするテスト
# ログインしていない場合、ログインページにリダイレクトされることをテストする
# ログインしている場合、アクセスできることをテストする
# ログインしている場合、リダイレクト先のURLをテストする
# ログインしている場合、リダイレクト先のURLにクエリパラメータを追加するテスト

from flask_login import current_user
import logging

logger = logging.getLogger(__name__)


def test_login_required(client):
    response = client.get("/todo/")
    assert response.status_code == 401

    # ログイン
    data = {
        "username": "test_user",
        "password": "test_password"
    }
    response = client.post("/auth/login", data=data, follow_redirects=True)
    assert response.status_code == 200

    # ログイン後のアクセス
    response = client.get("/todo/")
    assert response.status_code == 200
    logger.debug(f"current_user: {current_user}")

    with client.session_transaction() as session:
        assert session["_user_id"] == "1"  # User(1, username, password)のIDを確認

    # ログアウト
    response = client.get("/auth/logout", follow_redirects=True)
    assert response.status_code == 200

    # ログアウト後のアクセス
    response = client.get("/todo/")
    assert response.status_code == 401
