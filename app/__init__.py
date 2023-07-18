from flask import Flask


def create_app():
    app = Flask(__name__)

    # 2. create Blueprint view
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app

# if __name__ == '__main__':
#     app.run(debug=True)


