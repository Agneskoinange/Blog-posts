import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLAlchemy engine='sqlite:///:memory:'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nessie:agnes1234@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='agnes12346'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nessie:agnes1234@localhost/blogs'
    # uri = os.getenv('DATABASE_URL')
    # if uri and uri.startswith('postgres://'):
    #     uri = uri.replace('postgres://', 'postgresql://', 1)
    # SQLALCHEMY_DATABASE_URI = uri



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nessie:agnes1234@localhost/blogs'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}