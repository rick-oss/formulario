from flask import render_template, redirect, url_for, Blueprint, request, session

forms_bp = Blueprint("forms", __name__, template_folder="templates")


def is_authenticated():
    return "usuario" in session  # Verifica se o nome de usuario está na sessão


@forms_bp.route("/login", methods=["GET", "POST"])
def login():
    from app.models import User

    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        # Verifica se o usuario já existe no banco de dados
        existing_user = User.query.filter_by(username=usuario).first()

        # verifica se a senha corresponde
        if existing_user and existing_user.check_password(senha):
            session["usuario"] = usuario
            return redirect(url_for("index.home"))
        else:
            mensagem = "Credenciais Invalidas. Tente Novamente"
            return render_template("login.html", mensagem=mensagem)

    return render_template("login.html")


@forms_bp.route("/registro", methods=["GET", "POST"])
def registro():
    from app.models import User
    from app import db

    if request.method == "POST":
        novo_usuario = request.form["novo_usuario"]
        nova_senha = request.form["nova_senha"]
        conf_senha = request.form["conf_senha"]

        # Verifica se o usuario já existe no banco de dados
        existing_user = User.query.filter_by(username=novo_usuario).first()
        if existing_user:
            mensagem = "Este usuario já existe. Escolha outro nome de usuario"
            return render_template("registro.html", mensagem=mensagem)

        confirm = nova_senha != conf_senha
        if confirm:
            mensagem = "As senhas digitadas não correspondem. Tente novamente"
            return render_template("registro.html", mensagem=mensagem)
        # cria as tabelas do banco de dados
        # db.create_all()

        # cria o novo usuario e adiciona no banco de dados
        new_user = User(username=novo_usuario, password=nova_senha)
        new_user.set_password(nova_senha)  # cria o hash da senha
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))

    return render_template("registro.html")
