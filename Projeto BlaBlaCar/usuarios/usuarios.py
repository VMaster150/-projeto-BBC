from utilidades.utilidades import verificar_email, email_existente, verificar_senha

def cadastrar_usuario(usuarios):
    email = input('Digite seu email: ')
    if not verificar_email(email):
        print('Email inválido')
        return usuarios

    if email_existente(email, usuarios):
        print('Email já cadastrado')
        return usuarios

    senha = input('Digite sua senha: ')
    if not verificar_senha(senha):
        return usuarios

    nome = input('Digite seu nome: ')
    usuarios.append({'email': email, 'senha': senha, 'nome': nome})
    print('Usuário cadastrado com sucesso!')
    return usuarios

def login(usuarios):
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')

    for user in usuarios:
        if user['email'] == email and user['senha'] == senha:
            print(f"\nBem-vindo, {user['nome']}!\n")
            return user
    print('Email ou senha incorretos. Tente novamente.')
    return {}