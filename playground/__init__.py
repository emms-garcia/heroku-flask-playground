from datetime import datetime
import logging

from flask import Flask

from playground.config import CONFIG
from playground.models import db
from playground.utils.env import IS_DEVELOPMENT

logging.basicConfig(
    level=logging.DEBUG
    if IS_DEVELOPMENT
    else logging.INFO
)

# Create Flask app
app = Flask(__name__)
app.config.from_object(CONFIG)

# Init plugins
db.init_app(app)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return (
        '<h1>Hello World!</h1>'
        '<p>It is currently {time}.</p>'
        '<img src="http://loremflickr.com/600/400" />'
    ).format(time=the_time)


if __name__ == '__main__':
    app.run(
        debug=IS_DEVELOPMENT,
        use_reloader=IS_DEVELOPMENT,
    )
