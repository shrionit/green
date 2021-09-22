from flask import Flask, redirect
from . import settings
from app.routes.routelist import routes

app = Flask(__name__)

app.secret_key = settings.SECRET_KEY

# registering all routes
for route in routes:
    app.register_blueprint(route)


@app.route("/")
def redirect_to_auth():
    return redirect(settings.DEFAULT_REDIRECT)

