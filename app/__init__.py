from flask import Flask
from app.db import init_db


# -----------------------------------------------------------
# Create and setup the Flask app
def create_app():
    
    # Create the app
    app = Flask(__name__)

    # Initialise database
    init_db()

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app

