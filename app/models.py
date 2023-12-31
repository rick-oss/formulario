from app import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)  # chama set_password para criar o hash da senha

    def set_password(self, password):
        # Lógica para criar o hash da senha e armazená-lo no atributo password_hash
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        # Lógica para verificar a senha
        return bcrypt.check_password_hash(self.password, password)


