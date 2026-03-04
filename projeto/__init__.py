from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///livros.sqlite3"

db = SQLAlchemy(app)

#db.init_app()

from projeto import routes