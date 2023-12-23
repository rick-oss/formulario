from flask import render_template, redirect, url_for, Blueprint, request, session

forms_bp = Blueprint("forms", __name__, template_folder="templates")


def is_authenticated():
    return "email" in session  # Verifica se o endereço de email está na sessão


@forms_bp.route("/login", methods=["GET", "POST"])
def login():
    from app.models import User

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        # Verifica se o usuario já existe no banco de dados:
        existing_user = User.query.filter_by(email=email).first()

        # verifica se a senha corresponde:
        if existing_user and existing_user.check_password(senha):
            session["email"] = email
            return redirect(url_for("index.home"))
        else:  # Se não corresponde envia uma mensagem de erro e volta para a página de login:
            mensagem = "Credenciais Invalidas. Tente Novamente"
            return render_template("login.html", mensagem=mensagem)

    return render_template("login.html")


@forms_bp.route("/registro", methods=["GET", "POST"])
def registro():
    from app.models import User
    from app import db

    if request.method == "POST":
        novo_email = request.form["novo_email"]
        nova_senha = request.form["nova_senha"]
        conf_senha = request.form["conf_senha"]

        # Verifica se o usuario já existe no banco de dados:
        existing_user = User.query.filter_by(email=novo_email).first()
        if existing_user:
            mensagem = "Este email já está registrado. Vincule outro endereço de email"
            return render_template("registro.html", mensagem=mensagem)

        confirm = nova_senha != conf_senha
        if confirm:
            mensagem = "As senhas digitadas não correspondem. Tente novamente"
            return render_template("registro.html", mensagem=mensagem)

        # cria o novo usuario e adiciona no banco de dados:
        new_user = User(email=novo_email, password=nova_senha)
        new_user.set_password(nova_senha)  # cria o hash da senha
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("forms.login"))

    return render_template("registro.html")
