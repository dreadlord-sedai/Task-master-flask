# Imports
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# App Config
app = Flask(__name__)
Scss(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# Models
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __ref__(self) -> str:
        return f"Ttask {self.id}"




# Routes
@app.route('/')
def index():
    return render_template('index.html')

# Runner and Debugger
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)