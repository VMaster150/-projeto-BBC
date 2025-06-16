from usuarios.usuarios import (cadastrar_usuario, login)
from caronas.caronas import (cadastrar_carona, listar_caronas_disponiveis, procurar_carona_por_rota,
                     reservar_vaga, cancelar_reserva, cancelar_carona, listar_minhas_reservas)
from admin.admin import (menu_administrativo, listar_usuarios, listar_caronas, excluir_usuario, excluir_carona,
                   gerar_pdf_usuarios, gerar_pdf_caronas)
from dados.dados import dados


usuarios, caronas, carona_id_counter = dados()
usuario_logado = {}


while True:
    if not usuario_logado:
        print('\n=== MENU PRINCIPAL ===')
        print('1. Cadastrar usuário')
        print('2. Login')
        print('3. Menu administrativo')
        print('4. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            usuarios = cadastrar_usuario(usuarios)
        elif opcao == '2':
            usuario_logado = login(usuarios)
        elif opcao == '3':
            menu_administrativo(usuarios, caronas)
        elif opcao == '4':
            print('Saindo do sistema.')
            break
        else:
            print('Opção inválida!')
    else:
        if usuario_logado['email'] == 'admin@admin.com':
            print('\n=== MENU ADMINISTRADOR ===')
            print('1. Listar usuários')
            print('2. Listar caronas')
            print('3. Excluir usuário')
            print('4. Excluir carona')
            print('5. Gerar PDF de usuários')
            print('6. Gerar PDF de caronas')
            print('7. Login')
            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                listar_usuarios(usuarios)
            elif opcao == '2':
                listar_caronas(caronas)
            elif opcao == '3':
                usuarios = excluir_usuario(usuarios)
            elif opcao == '4':
                caronas = excluir_carona(caronas)
            elif opcao == '5':
                gerar_pdf_usuarios(usuarios)
            elif opcao == '6':
                gerar_pdf_caronas(caronas)
            elif opcao == '7':
                usuario_logado = {}
                print('Login realizado com sucesso!')
            else:
                print('Opção inválida!')
        else:
            print('\n=== MENU USUÁRIO ===')
            print('1. Cadastrar carona')
            print('2. Listar caronas disponíveis')
            print('3. Procurar carona por rota')
            print('4. Reservar vaga em carona')
            print('5. Cancelar reserva')
            print('6. Cancelar carona (motorista)')
            print('7. Minhas reservas')
            print('8. Login')
            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                caronas, carona_id_counter = cadastrar_carona(caronas, usuario_logado, carona_id_counter)
            elif opcao == '2':
                listar_caronas_disponiveis(caronas)
            elif opcao == '3':
                procurar_carona_por_rota(caronas)
            elif opcao == '4':
                reservar_vaga(caronas, usuario_logado)
            elif opcao == '5':
                cancelar_reserva(caronas, usuario_logado)
            elif opcao == '6':
                caronas = cancelar_carona(caronas, usuario_logado)
            elif opcao == '7':
                listar_minhas_reservas(caronas, usuario_logado)
            elif opcao == '8':
                usuario_logado = {}
                print('Login realizado com sucesso!')
            else:
                print('Opção inválida!')