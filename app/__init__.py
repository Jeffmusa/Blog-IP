from flask import Flask
from flask import Blueprint





# Initializing application
def create_app(config_name):
    app = Flask(__name__)


         # Creating the app configurations
    # app.config.from_object(config_options[config_name])


 # Registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    '''
    Here I register my blue prints
    '''

    #setting config
    return app