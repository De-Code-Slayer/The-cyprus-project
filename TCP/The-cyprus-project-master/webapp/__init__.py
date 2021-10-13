from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager

db = SQLAlchemy()
DB_NAME = "mywebappdatabase.db"




def create_app():
 app = Flask(__name__)
 app.config["SECRET_KEY"] = "JHHGUIF HUHUH HHUF UH"
 app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(DB_NAME)
 
 db.init_app(app)

 from .views import views
 from .admin import admin


 app.register_blueprint(views)
 app.register_blueprint(admin, url_prefix="")

 from .models import User, Articles
 create_database(app)


 login_manager = LoginManager()
 login_manager.login_view = "admin.login"
 login_manager.init_app(app)

 @login_manager.user_loader
 def load_user(id):
    return User.query.get(int(id))
 
 
 
 @app.errorhandler(404)
 def not_found(e):
  
# defining function
  return render_template("404.html")

 return app



def create_database(app):
    if not path.exists("webapp/" + DB_NAME):
        db.create_all(app=app)
        print("Database created!!")
