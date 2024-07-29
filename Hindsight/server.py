from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import db_name


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_name

db = SQLAlchemy()

db.init_app(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)


@app.route('/', methods=['GET'])
def get_home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
