from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# Call modules from out scope because of blueprint
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # 1. Add configuration of database
    app.config.from_object(config)

    # 2. ORM - $ flask db init
    db.init_app(app)
    migrate.init_app(app, db)  # app, sqlite

    from app.data import todo_model

    # 3. Blueprint view
    from app.views import main_views
    app.register_blueprint(main_views.bp)

    return app


if __name__ == '__main__':

    create_app().run(debug=True)


