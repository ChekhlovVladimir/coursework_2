from flask import Flask, render_template
from web.bp_views import blueprint_web

app = Flask(__name__)
app.register_blueprint(blueprint_web)


@app.route("/")
def page_index():
    pass


if __name__ == "__main__":
    app.run()
