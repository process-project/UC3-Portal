from browsepy import db


class Metadata(db.Model):
    path = db.Column(db.String(), primary_key=True)
    desc = db.Column(db.String())
    size = db.Column(db.Integer())
    size_date = db.Column(db.DateTime())
