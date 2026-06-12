from flask import Flask
from extensions import db

from routes.public import public_bp
from routes.admin import admin_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(public_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)