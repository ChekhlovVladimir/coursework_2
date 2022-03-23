from flask import Flask, render_template, Blueprint, request
from utils import Posts
from pprint import pprint as pp

app = Flask(__name__)
blueprint_web = Blueprint('blueprint_web', __name__, template_folder='templates', static_folder='static')
DATA_PATH = "data/data.json"
COMMENT_PATH = "data/comments.json"


@blueprint_web.route('/')
def index():
    post_data = Posts(DATA_PATH)
    return render_template('index.html', posts=post_data.get_posts_all())


@blueprint_web.route('/post/<int:post_id>')
def get_post_by_post_id(post_id):
    post_data = Posts(DATA_PATH)
    content = post_data.get_post_by_pk(post_id)
    post_comment = Posts(COMMENT_PATH)
    comments = post_comment.get_comments_by_post_id(post_id)
    count_comment = len(comments)
    return render_template('post.html', content=content, post_id_=post_id,
                           comments=comments, count_comment=count_comment)


@blueprint_web.route('/search/<user_id>')
def get_comments_by_user_id():
    # post_id = request.args.get('post_id')
    # content = get_comments_by_post_id(post_id)
    return render_template('user-feed.html')
