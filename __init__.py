import secrets
from flask import Flask
from home import home
from secrets_manager import secrets as secrets_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(64)
    
    # Register blueprints
    app.register_blueprint(home)
    app.register_blueprint(secrets_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
