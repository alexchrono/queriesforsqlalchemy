
from app.config import Configuration
from app.models import db,Student,Teacher,Course
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app,db)


# from . import selfmade_queries  # Import your routes (selfmade_queries) here

if __name__ == "__main__":
    app.run()

