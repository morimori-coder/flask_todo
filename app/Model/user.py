from flask_login import UserMixin
from app.app import db
from app.app import login_manager


class User(UserMixin):
    # id = db.Column(db.Integer, primary_key=True)
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    return User(user_id, "testuser", "4")
    # return User.query.get(int(user_id))  # ユーザーIDに基づいてユーザーを取得
