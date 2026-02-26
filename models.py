from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url
        }