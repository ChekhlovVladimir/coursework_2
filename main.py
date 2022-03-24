from flask import Flask, render_template
from web.bp_views import blueprint_web
from  pprint import pprint as pp
app = Flask(__name__)
app.register_blueprint(blueprint_web)


@app.route("/")
def page_index():
    pass


@app.route('/search')
def search_page(s):
    return render_template('search.html')

pp(search_page("пирог"))

if __name__ == "__main__":
    app.run()
