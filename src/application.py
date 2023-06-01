from flask import Flask


def create_app() -> Flask:
    # Define Flask Application as app.
    app = Flask(__name__)
    
    # Load Configurations
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = False
    app.config['TESTING'] = False

    # Initialize Blueprints
    initialize_blueprints(app)

    # Log Application Mode.
    print(
        f"Application running in {app.config['ENV']} mode"
    )
    # Return and start Flask application.
    return app


def initialize_blueprints(app: object) -> None:
    # Base Blueprints
    from base import (
        base_bp
    )
    app.register_blueprint(
        base_bp
    )
    # Recipe Blueprints
    from recipes import (
        recipes_bp
    )
    app.register_blueprint(
        recipes_bp
    )
    # System Blueprints
    from system import (
        system_bp
    )
    app.register_blueprint(
        system_bp
    )
