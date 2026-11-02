from flask import Blueprint, render_template

from app.models import Character

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    characters = Character.query.order_by(Character.name).all()
    return render_template("index.html", characters=characters)
