import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-hard-to-guess-string'
    DATABASE = 'sqlite:///crop_monitor.db'  # SQLite database
