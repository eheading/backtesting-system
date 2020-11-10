import flask
from flask_cors import CORS
from endpoints.bt import bt_result
from endpoints.error_handlers import error

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


# The basic routes
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to Back Testing API</h1>
    <p>Hello world </p>'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# register new endpoints
app.register_blueprint(bt_result)
app.register_blueprint(error)


if __name__ == '__main__':
    app.run()