from flask import Blueprint, request
from app.controllers.user import user

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route('/signup', methods=["GET", "POST"])
def signup():
    return user.signup(request)


@bp.route('/login', methods=["GET","POST"])
def login():
    return user.login(request)


