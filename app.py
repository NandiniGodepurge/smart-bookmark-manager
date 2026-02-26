from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from models import db, Bookmark

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookmarks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

# Add Bookmark
@app.route("/api/bookmarks", methods=["POST"])
def add_bookmark():
    data = request.json
    new_bookmark = Bookmark(title=data["title"], url=data["url"])
    db.session.add(new_bookmark)
    db.session.commit()
    return jsonify(new_bookmark.to_dict()), 201

# View All
@app.route("/api/bookmarks", methods=["GET"])
def get_bookmarks():
    bookmarks = Bookmark.query.all()
    return jsonify([b.to_dict() for b in bookmarks])

# Update
@app.route("/api/bookmarks/<int:id>", methods=["PUT"])
def update_bookmark(id):
    bookmark = Bookmark.query.get_or_404(id)
    data = request.json
    bookmark.title = data["title"]
    bookmark.url = data["url"]
    db.session.commit()
    return jsonify(bookmark.to_dict())

# Delete
@app.route("/api/bookmarks/<int:id>", methods=["DELETE"])
def delete_bookmark(id):
    bookmark = Bookmark.query.get_or_404(id)
    db.session.delete(bookmark)
    db.session.commit()
    return jsonify({"message": "Deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)