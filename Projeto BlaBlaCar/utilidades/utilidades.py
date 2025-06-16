import os
import time

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def verificar_email(email):
    if '@' not in email or '.' not in email:
        return False
    return True

def email_existente(email, usuarios):
    for user in usuarios:
        if user['email'] == email:
            return True
    return False

def verificar_senha(senha):
    if len(senha) < 6:
        print('Sua senha deve ter no mínimo 6 caracteres.A')
        return False
    return True