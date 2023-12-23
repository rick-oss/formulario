from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Cria uma instancia do SQLAlchemy e Migrate
db = SQLAlchemy()
migrate = Migrate()


# Cria e configura uma instancia do aplicativo Flask
def create_app():
    # importa User para garantir que o SQLAlchemy e o Flask-Migrate tenham acesso ao modelo
    from app.models import User
    from app.routes import forms_bp

    app = Flask(__name__)

    # Configuraçao do SQLAlchemy e banco de dados
    app.config["SECRET_KEY"] = "##25!!73##"
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqlconnector://root:6273!Ric#@localhost/meubanco"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "6273!Ric#"
    app.config["MYSQL_DB"] = "meubanco"

    # Inicializa o SQLAlchemy e o Migrate com o aplicativo Flask
    db.init_app(app)
    migrate.init_app(app, db)

    # Registra os Blueprints no aplicativo
    app.register_blueprint(forms_bp, url_prefix="/")

    return app
