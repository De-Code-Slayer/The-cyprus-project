from typing import AsyncGenerator
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from datetime import timedelta, datetime
from webapp.models import Articles, Whatsapp
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

admin = Blueprint("admin", __name__)


@admin.route("/admin", methods=["GET", "POST"])
#@login_required
def administrator():
     if request.method == "POST":
         # this is to seperate the admin page requests payloads
         section = str(request.form.get("section"))
         print(section)
         if section == "Blog":
                print("Blog")
         #add if statements to check if the post added are long enough and acutually valid
                articletitle = str(request.form.get("articletitle"))
                articles = str(request.form.get("articles"))
                author = str(request.form.get("author"))
                print(articles, articletitle, author)

                new_article = Articles(
            articles=articles, author=author, articletitle=articletitle)
                db.session.add(new_article)
                db.session.commit()
                print("added")
                flash("posted")
#====------------------- Whatsapp section -------------------------------------------------------------
         elif section == "Whatsapp":
                print("Whatsapp")
         #add if statements to check if the links added are acutually valid
                whatsapp_title = str(request.form.get("whatsapp_title"))
                whatsapp_link = str(request.form.get("Whatsapp_link"))
                institute = str(request.form.get("Institute"))

                new_whatsapp = Whatsapp(
                    name=whatsapp_title, link=whatsapp_link, institute=institute)
                db.session.add(new_whatsapp)
                db.session.commit()
                print("added")
                flash("New Whatsapp added")

         else:
            flash("error")
     return render_template("admin_page.html")



#Login for admin of the website
@admin.route("/login_admin", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(user_name=username, password=password).first()
        if user:
           login_user(user, remember=True)
           return redirect(url_for("admin.administrator"))
        if not user:
            print(username)
            flash("No administrator found")

    return render_template("admin_login.html")


@admin.route("/add_admin", methods=["POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(user_name=username).first()
        if user:
            return "username already exist"

        else:

         new_admin = User( password=password, user_name=username)
         db.session.add(new_admin)
         db.session.commit()
         return "added {username} as admin with {password} as password"
