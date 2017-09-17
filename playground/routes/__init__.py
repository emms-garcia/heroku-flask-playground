from datetime import datetime

from flask import Blueprint

from playground.models.greetings import Greetings

home_page = Blueprint('home_page', __name__, template_folder='templates')


@home_page.route('/')
def index():
    the_time = datetime.now().isoformat()

    # Create new greeting
    Greetings().create()

    # List all greetings
    all_greetings = ''.join([
        '<li>{} - {}</li>'.format(
            greeting.id, greeting.when.isoformat()
        ) for greeting in Greetings.query.all()
    ])

    return (
        '<h1>Hello World!</h1>'
        '<p>Current timestamp: {}.</p>'
        '<p>Access Log:</p>'
        '<ul>{}</ul>'
    ).format(the_time, all_greetings)
