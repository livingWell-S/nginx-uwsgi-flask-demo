from flask import Flask

from database import init_db
import config
import models


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    init_db(app)

    return app

app = create_app()