from datetime import datetime

from flask import Blueprint

from playground.models.access_logs import AccessLogs

home_page = Blueprint('home_page', __name__, template_folder='templates')


@home_page.route('/')
def index():
    the_time = datetime.now().isoformat()

    # Create new access log entry
    AccessLogs().create()

    # List access logs
    all_access_logs = ''.join([
        '<li>{} - {}</li>'.format(
            log.id, log.when.isoformat()
        ) for log in AccessLogs.query.all()
    ])

    return (
        '<h1>Hello World!</h1>'
        '<p>Current timestamp: {}.</p>'
        '<p>Access Log:</p>'
        '<ul>{}</ul>'
    ).format(the_time, all_access_logs)
