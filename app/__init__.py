from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

import config

# Call modules from out scope because of blueprint
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap5()


def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)     # bootstrap init

    # 1. Add configuration of database
    app.config.from_object(config)

    # 2. ORM - $ flask db init
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)  # app, sqlite

    from app.data import todo_model

    # 3. Blueprint view
    from app.views import main_views, detail_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(detail_views.bp)
    app.register_blueprint(auth_views.auth_bp)

    # 4. Filter
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime  # built-in filter

    return app


app = create_app()


@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)


