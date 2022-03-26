import pytest
from main import app
from utils import Posts
from flask import Flask, jsonify

app.config['JSON_AS_ASCII'] = False
DATA_PATH = 'data/data.json'
app = Flask(__name__)


@app.route('/posts')
def test_text():
    return "it is ok"


@app.route('/users/leo')
def json_key():
    data = {'name': 'leo'}
    return jsonify(data)


class TestPosts:
    def test_get_posts_all(self):
        """
        Тестирование на правильное соединение с сервером при выводе всех постов, на возврат списка, значений ключа

        """
        response = app.test_client().get('/posts')
        temp = []
        assert response.status_code == 200
        assert response.data == b'it is ok'
        assert type(temp) == type(response.json), 'Вернулся не список'
        assert 'poster_name' in response.json[0], 'Нет ключа к "poster_name"'

    def test_get_post_json(self):
        """
        Проверка на возврат словаря, ключей словаря.

        """
        temp = {}
        response = app.test_client().get('/users/leo')
        assert response.json.get("name") == "leo", 'Incorrect name'
        assert type(temp) == type(response.json), 'Вернулся не словарь'

