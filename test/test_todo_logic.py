import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from app.Model.todo import Todo
from app.todo.logic import check_description_length

# ロジック関数のテスト例
def test_check_description_length_normal():
    input_data = "test_input"
    expected_output = True
    result = check_description_length(input_data)
    print(result)
    assert result == expected_output


def test_check_description_length_abnormal():
    input_data = "a" * 31
    expected_output = "Description should be within 30 characters."
    try:
        check_description_length(input_data)
    except Exception as e:
        print(e)
        assert str(e) == expected_output


def test_add_todo_success(client, app):
    data = {
        "description": "Test todo",
        "deadline": "2024-12-31"
    }
    print("ココのログを見たい")
    print(f'{app.config["SQLALCHEMY_DATABASE_URI"]}=')

    response = client.post("/todo/add", data=data, follow_redirects=True)

    print(response)
    print(response.status_code)
    assert response.status_code == 200

    with app.app_context():
        added_todo = Todo.query.filter_by(description="Test todo").first()
        print(added_todo)
        assert added_todo is not None
        assert str(added_todo.deadline) == "2024-12-31 00:00:00"
