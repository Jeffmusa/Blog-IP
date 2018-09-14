import os



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://vicklyne:Moringa123@localhost/blog'

    '''
    General configuration parent class
    '''


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