from playground.models import db
from sqlalchemy.sql import func


class Greetings(db.Model):
    __tablename__ = 'greetings'

    id = db.Column(db.Integer, primary_key=True)
    when = db.Column(
        db.DateTime, nullable=False, server_default=func.now()
    )

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
