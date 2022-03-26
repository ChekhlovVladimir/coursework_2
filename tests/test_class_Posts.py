from utils import Posts
import pytest
from main import app

class TestPosts:
    def test_get_posts_all(self):
        path = 'data/data.json'
        posts = Posts(path)
        assert posts.get_posts_all() == 'data/data.json', 'Ошибка в пути файла'

    def test_get_posts_by_user(self):
        user_name = 'user_name'
        posts = Posts(user_name)
        assert posts.get_posts_by_user(user_name) == 'user_name', 'Ошибка в имени'
