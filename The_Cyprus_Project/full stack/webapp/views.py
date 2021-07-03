from datetime import date, time
from webapp.models import Articles, Whatsapp
from flask import Blueprint, render_template, url_for, request
from flask_login import current_user
from . import db


views = Blueprint("views", __name__)


@views.route("/")
def home():

    # Queries to database to get the post by the 5 most recents

    post = db.session.query(Articles.articles).order_by(
        Articles.date.desc()).limit(5).all()

    post_title = db.session.query(Articles.articletitle).order_by(
        Articles.date.desc()).limit(5).all()

    post_date = db.session.query(Articles.date).order_by(
        Articles.date.desc()).limit(5).all()

    post_author = db.session.query(Articles.author).order_by(
        Articles.date.desc()).limit(5).all()
    post_id = db.session.query(Articles.id).order_by(
        Articles.date.desc()).limit(5).all()

    return render_template("index.html", content=post,  post_title=post_title, post_date=post_date, post_author=post_author, post_id=post_id)


@views.route("/<id>")
def more(id):
    ident = id

    post = Articles.query.get(ident)
    return render_template("more_post.html", content=post)


@views.route("/whatsapp")
def whatsapp():
    if request.method == "POST":
        institute = request.form.get("category")
        category = Whatsapp.query.filter_by(institute=institute).all()
        if category:
            whatsapp = category
            return render_template("whatsapp.html", whatsapp)
    # Queries to database to get All the whatsapp links
    whatsapp_groups = db.session.query(Whatsapp).all()
    return render_template("whatsapp.html", whatsapp=whatsapp_groups)
