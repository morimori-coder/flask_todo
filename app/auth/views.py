from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from app.Model.user import User
from app.Model.todo import Todo
from app.app import login_manager
import logging

logger = logging.getLogger(__name__)

# ログイン用のviews.pyを作成します。
# ログイン用のBlueprintを作成して、ログイン画面を表示するためのルートを定義します。
# ログイン画面は、templates/login.htmlを表示します。
# ログイン画面には、ユーザ名とパスワードを入力するフォームがあります。
# ログインボタンをクリックすると、POSTリクエストが送信されます。
# ログイン処理は、POSTリクエストを受け取り、ユーザ名とパスワードを検証します。
# ユーザ名とパスワードが正しい場合は、ログイン状態にします。
# ログイン状態にするには、Flask-Loginのlogin_user関数を使用します。
# ログイン状態にすると、current_user変数が設定されます。
# current_user変数は、ログイン中のユーザを表します。
# ログイン状態になると、TODO画面にリダイレクトされます。
# ログインに失敗した場合は、エラーメッセージを表示します。
# ログアウト処理は、GETリクエストを受け取り、ログアウト状態にします。
# ログアウト状態にするには、Flask-Loginのlogout_user関数を使用します。
# ログアウト状態になると、current_user変数がクリアされます。
# ログアウト状態になると、ログイン画面にリダイレクトされます。
# ログイン画面には、ログアウトボタンが表示されます。

auth_bp = Blueprint("auth", __name__, url_prefix="/auth",
                    template_folder="templates")

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # user = User.query.filter_by(username=username).first()

        # if user and check_password_hash(user.password, password):
        if username and password:
            login_user(User(1, username, password))
            return redirect(url_for('todo.get_todo'))
        else:
            flash('Invalid username or password')

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# @login_manager.user_loader
# def load_user(user_id, username, password):
#     logger.debug(f"load_user: {user_id}")
#     return User(user_id, username, password)
#     # return User.query.get(int(user_id))
