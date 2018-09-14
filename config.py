import os



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vicklyne:Moringa123@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    '''
    General configuration parent class
    '''

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



class DevConfig(Config):
    '''
    Development  configuration child class
    '''
    DEBUG = True


class ProdConfig(Config):
    '''
    Production  configuration child class
    '''    


config_options={
    'development':DevConfig,
    'production': ProdConfig
}    