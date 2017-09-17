import logging

from flask import Flask

from playground.config import CONFIG
from playground.env import IS_DEVELOPMENT
from playground.models import db
from playground.routes import home_page

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

# Register blueprints
app.register_blueprint(home_page)

if __name__ == '__main__':
    app.run(
        debug=IS_DEVELOPMENT,
        use_reloader=IS_DEVELOPMENT,
    )
