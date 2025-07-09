from flask import Flask
from db import init_db, db
from routes import routes
from flask_cors import CORS

PORT = 5000

app = Flask(__name__)
init_db(app)
app.register_blueprint(routes)
CORS(app)


def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True,port=PORT)
