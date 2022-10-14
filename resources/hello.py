from flask_smorest import Blueprint


blp = Blueprint("hello", __name__)


@blp.route("/")
def hello():
    return("Hello")

@blp.route("/<string:name>")
def hello(name):
    return("Hello " + name)