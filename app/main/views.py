from flask import render_template
from . import main



@main.route('/')
def index():
    '''
    View root page function that returns index page and its data
    '''
    title = 'BLOG MANENOS'

    

    return render_template('index.html', title = title, index = index)