from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if os.getenv("CI") == "true" or os.getenv("AWS_ENV") == "true":
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "postgresql://user:password@db:5432/mydb"
    )

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET"])
def health_check():
    return "OK", 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "completed": t.completed} for t in tasks])

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    new_task = Task(title=data["title"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added"}), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
