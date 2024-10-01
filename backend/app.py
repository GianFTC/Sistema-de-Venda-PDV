from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from routes import routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

# Registre o Blueprint
app.register_blueprint(routes)

@app.route('/')
def index():
    return 'Sistema PDV'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Modificado para escutar em todas as interfaces
