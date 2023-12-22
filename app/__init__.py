from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# Cria uma instancia do SQLAlchemy e Migrate
db = SQLAlchemy()
migrate = Migrate()


# Cria e configura uma instancia do aplicativo Flask
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "##25!!73##"

    # Configuraçao do SQLAlchemy
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqlconnector://root:6273!Ric#@localhost/meusite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Configuraçao do banco de dados
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = "6273!Ric#"
    app.config["MYSQL_DB"] = "MeuBanco"

    # Inicializa o SQLAlchemy e o Migrate com o aplicativo Flask
    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import forms_bp

    # Registra os Blueprints no aplicativo
    app.register_blueprint(forms_bp, url_prefix="/")

    return app
