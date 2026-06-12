from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models.models import Post

admin_bp = Blueprint("admin", __name__)


# CREATE
@admin_bp.route("/create", methods=["POST"])
def create():
    title = request.form.get("title")
    content = request.form.get("content")

    if title and content:
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()

    return redirect(url_for("admin.admin_dashboard"))


# READ
@admin_bp.route("/")
def admin_dashboard():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("admin.html", posts=posts)


# UPDATE
@admin_bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]

        db.session.commit()
        return redirect(url_for("admin.admin_dashboard"))

    return render_template("edit_post.html", post=post)


# DELETE
@admin_bp.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("admin.admin_dashboard"))