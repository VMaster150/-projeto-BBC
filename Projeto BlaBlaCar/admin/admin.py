from utilidades.utilidades import limpar_tela
from relatorios.relatorios import gerar_pdf_usuarios, gerar_pdf_caronas


def listar_usuarios(usuarios):
    if not usuarios:
        print('Nenhum usuário cadastrado.')
        return

    print('Lista de usuários:')
    for usuario in usuarios:
        print(f'Nome: {usuario['nome']}, Email: {usuario['email']}')


def listar_caronas(caronas):
    if not caronas:
        print('Nenhuma carona cadastrada.')
        return

    print('Lista de caronas:')
    for carona in caronas:
        print(
            f'ID: {carona['carona_id']}, Motorista: {carona['nome_motorista']}, '
            f'Origem: {carona['origem']}, Destino: {carona['destino']}, '
            f'Data: {carona['data']}, Horário: {carona['horario']}, Vagas: {carona['vagas']}')


def excluir_usuario(usuarios):
    listar_usuarios(usuarios)
    usuario_email = input('\nDigite o e-mail do usuário que deseja excluir: ')

    for usuario in usuarios[:]:
        if usuario['email'] == usuario_email:
            usuarios.remove(usuario)
            print(f'Usuário {usuario['nome']} excluído com sucesso!')
            return usuarios

    print('Usuário não encontrado.')
    return usuarios


def excluir_carona(caronas):
    listar_caronas(caronas)
    carona_id_input = input('\nDigite o ID da carona que deseja excluir: ')

    if not carona_id_input.isdigit():
        print('ID inválido! Deve ser um número.')
        return caronas

    carona_id = int(carona_id_input)

    for carona in caronas[:]:
        if carona['carona_id'] == carona_id:
            caronas.remove(carona)
            print('Carona excluída com sucesso!')
            return caronas

    print('Carona não encontrada.')
    return caronas


def menu_administrativo(usuarios, caronas):
    senha_admin = 'admin123'
    tentativa = input('\nDigite a senha de administrador: ')

    if tentativa == senha_admin:
        while True:
            limpar_tela()
            print('\n\n=== MENU ADMINISTRADOR ===\n')
            print('1 - Listar Usuários')
            print('2 - Listar Caronas')
            print('3 - lista de valores de caronas')
            print('4 - Excluir Usuário')
            print('5 - Excluir Carona')
            print('6 - Voltar ao menu principal\n')

            opcao_admin = input('Escolha uma opção: ')

            if opcao_admin == '1':
                limpar_tela()
                listar_usuarios(usuarios)
                opcao = input('deseja baixar a lista? (s/n): ').lower()
                if opcao == 's':
                    txt_pdf = input('Deseja baixar em txt ou pdf? (t/p): ').lower()
                if txt_pdf == 't':
                    download_lista_usuarios(usuarios)
                    print('Lista de usuários baixada com sucesso!')
                elif txt_pdf == 'p':
                    gerar_pdf_usuarios(usuarios)
                    print('PDF gerado com sucesso!')


            elif opcao_admin == '2':
                limpar_tela()
                listar_caronas(caronas)
                opcao = input('deseja baixar a lista? (s/n): ').lower()
                if opcao == 's':
                    txt_pdf = input('Deseja baixar em txt ou pdf? (t/p): ').lower()
                    if txt_pdf == 't':
                        download_lista_caronas(caronas)
                        print('Lista de caronas baixada com sucesso!')
                    elif txt_pdf == 'p':
                        gerar_pdf_caronas(caronas)
                        print('PDF gerado com sucesso!')
            elif opcao_admin == '3':
                limpar_tela()
                opcao = input('Deseja baixar a lista de valores de caronas? (s/n): ').lower()
                if opcao == 's':
                    txt_pdf = input('Deseja baixar em txt ou pdf? (t/p): ').lower()
                    if txt_pdf == 't':
                        download_lista_caronas(caronas)
                        print('Lista de caronas baixada com sucesso!')
                    elif txt_pdf == 'p':
                        gerar_pdf_caronas(caronas)
                        print('PDF gerado com sucesso!')
                                        
            elif opcao_admin == '4':
                limpar_tela()
                usuarios = excluir_usuario(usuarios)
            elif opcao_admin == '5':
                limpar_tela()
                caronas = excluir_carona(caronas)
            elif opcao_admin == '6':
                break
            else:
                print('Opção inválida!')
                input('\nPressione Enter para continuar...')
    else:
        print('Senha incorreta!')
        input('\nPressione Enter para continuar...')