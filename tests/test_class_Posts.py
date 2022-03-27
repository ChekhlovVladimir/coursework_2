from main import app
from flask import Flask, jsonify

app.config['JSON_AS_ASCII'] = False
DATA_PATH = 'data/data.json'
app = Flask(__name__)


@app.route('/api/posts')
def test_text():
    return "it is ok"


@app.route('/api/posts/15')
def json_key():
    data = {'poster_name': 'leo'}
    return jsonify(data)


def test_get_posts_all():
    response = app.test_client().get('api/posts/15')

    assert response.status_code == 404
    assert set(response.json.keys()) == {
        'content', 'pic', 'likes_count', 'pk', 'poster_name', 'poster_avatar', 'views_count'
    }
    assert response.json == {'error': "Пост не найден"}


def test_get_post():
    response = app.test_client().get('/api/posts')

    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0
