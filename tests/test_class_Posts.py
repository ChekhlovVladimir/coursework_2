import pytest
from main import app
from utils import Posts

DATA_PATH = 'data/data.json'


class TestPosts:
    def test_get_posts_all(self):
        response = app.test_client().get('/api/posts')
        assert response.status_code == 200

    def test_get_posts_by_user(self):
        user_name = 'user_name'
        posts = Posts(user_name)
        response = app.test_client().get('/username')
        assert response.json.get(user_name) == 'user_name', 'Ошибка в имени'
