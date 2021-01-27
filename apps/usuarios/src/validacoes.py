from django.contrib.auth.models import User

def campo_vazio(campo):
    return not campo.strip()

def usuario_cadastrado(username, email):
    return User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists()

def senhas_diferentes(password_1, password_2):
    return password_1 != password_2