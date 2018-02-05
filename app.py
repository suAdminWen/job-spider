from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

from web.views import web


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.register_blueprint(web, url_prefix="/web")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
