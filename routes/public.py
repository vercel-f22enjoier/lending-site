from flask import Blueprint, render_template
from models.models import Post

public_bp = Blueprint("public", __name__)

@public_bp.route("/")
def index():
    posts = Post.query.order_by(Post.created_at.desc()).limit(3).all()
    return render_template("index.html", posts=posts)


@public_bp.route("/about")
def about():
    return render_template("about.html")


@public_bp.route("/services")
def services():
    return render_template("services.html")


@public_bp.route("/contacts")
def contacts():
    return render_template("contacts.html")