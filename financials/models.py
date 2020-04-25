from datetime import datetime
from financials import db
from sqlalchemy.sql import func


class Ticker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.String(5), nullable=False)
    key = db.Column(db.String(120), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    fy = db.Column(db.String(4), nullable=False)

    def __repr__(self):
        return "Stock('{}', '{}', '{}')".format(self.stock, self.key, self.value)
