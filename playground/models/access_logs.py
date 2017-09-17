from playground.models import db
from sqlalchemy.sql import func


class AccessLogs(db.Model):
    __tablename__ = 'access_logs'

    id = db.Column(db.Integer, primary_key=True)
    when = db.Column(
        db.DateTime, nullable=False, server_default=func.now()
    )

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
