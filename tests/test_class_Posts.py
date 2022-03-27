from main import app
from flask import Flask, jsonify
from utils import Posts

app.config['JSON_AS_ASCII'] = False
DATA_PATH = 'data/data.json'
app = Flask(__name__)


def test_get_posts_all():
    response = app.test_client().get('api/posts/1')

    assert response.status_code == 200
    assert set(response.json.keys()) == {
        'content', 'pic', 'likes_count', 'pk', 'poster_name', 'poster_avatar', 'views_count'
    }


def test_get_post():
    response = app.test_client().get('/api/posts')

    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0
