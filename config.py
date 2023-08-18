import os

BASE_DIR = os.path.dirname(__file__)

# 1. Use SQLite and create pybo database
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False  # alchemy event handler option

