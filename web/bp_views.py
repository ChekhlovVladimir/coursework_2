from flask import Flask, render_template, Blueprint, request
from utils import Posts

app = Flask(__name__)
blueprint_web = Blueprint('blueprint_web', __name__, template_folder='templates', static_folder='static')
PATH = "data/data.json"


@blueprint_web.route('/')
def index():
    return render_template('index.html')


@blueprint_web.route('/posts/<post_id>')
def get_comments_by_post_id():
    post_id = request.args.get('post_id')
    content = get_comments_by_post_id(post_id)
    return render_template('post.html', content=content, post_id=post_id)
