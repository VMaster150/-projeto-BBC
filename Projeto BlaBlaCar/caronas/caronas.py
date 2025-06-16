def cadastrar_carona(caronas, usuario_logado, carona_id_counter):
    origem = input('Digite a cidade de origem: ')
    destino = input('Digite a cidade de destino: ')
    data_carona = input('Digite a data da carona (DD/MM/AAAA): ')
    horario = input('Digite o horário da carona (HH:MM): ')
    vagas_input = input('Digite o número de vagas disponíveis: ')

    if not vagas_input.isdigit():
        print('Número de vagas deve ser um valor numérico.')
        return caronas, carona_id_counter

    vagas = int(vagas_input)
    if vagas <= 0 or vagas > 4:
        print('Número de vagas inválido (deve ser entre 1 e 4).')
        return caronas, carona_id_counter

    for carona in caronas:
        if (carona['origem'] == origem and
                carona['destino'] == destino and
                carona['data'] == data_carona and
                carona['horario'] == horario and
                carona['email_motorista'] == usuario_logado['email']):
            print('Já existe uma carona cadastrada com esses dados.')
            return caronas, carona_id_counter

    nova_carona = {
        'origem': origem,
        'destino': destino,
        'data': data_carona,
        'horario': horario,
        'vagas': vagas,
        'carona_id': carona_id_counter,
        'email_motorista': usuario_logado['email'],
        'nome_motorista': usuario_logado['nome'],
        'passageiros': [],
        'valor': 5
    }
    caronas.append(nova_carona)
    carona_id_counter += 1
    print('Carona cadastrada com sucesso!')
    return caronas, carona_id_counter + 1


def reservar_vaga(caronas, usuario_logado):
    carona_id_input = input('Digite o ID da carona que deseja reservar: ')

    if not carona_id_input.isdigit():
        print('ID inválido! Deve ser um número.')
        return

    carona_id = int(carona_id_input)

    for carona in caronas:
        if carona['carona_id'] == carona_id:
            if carona['email_motorista'] == usuario_logado['email']:
                print('Você não pode reservar uma vaga na sua própria carona!')
                return

            if carona['vagas'] > 0:
                if usuario_logado['email'] in carona['passageiros']:
                    print('Você já está nessa carona!')
                    return

                carona['passageiros'].append(usuario_logado['email'])
                carona['vagas'] -= 1
                carona['valor'] += 5
                print(f'Vaga reservada com sucesso na carona de {carona["origem"]} para {carona["destino"]}!')
                print(f'Valor da carona: R$ {carona["valor"]}')
                print('Lembre-se de pagar o valor da carona ao motorista no dia da viagem.')
                return
            else:
                print('Não há vagas disponíveis nessa carona.')
                return
    print('Carona não encontrada.')


def cancelar_reserva(caronas, usuario_logado):
    carona_id_input = input('Digite o ID da carona que deseja cancelar a reserva: ')

    if not carona_id_input.isdigit():
        print('ID inválido! Deve ser um número.')
        return

    carona_id = int(carona_id_input)

    for carona in caronas:
        if carona['carona_id'] == carona_id:
            if usuario_logado['email'] in carona['passageiros']:
                carona['passageiros'].remove(usuario_logado['email'])
                carona['vagas'] += 1
                carona['valor'] -= 5
                print('Reserva cancelada com sucesso!')
                return
            else:
                print('Você não tem uma reserva nessa carona.')
                return
    print('Carona não encontrada.')


def cancelar_carona(caronas, usuario_logado):
    carona_id_input = input('Digite o ID da carona que deseja cancelar: ')

    if not carona_id_input.isdigit():
        print('ID inválido! Deve ser um número.')
        return caronas

    carona_id = int(carona_id_input)

    for carona in caronas[:]:
        if carona['carona_id'] == carona_id and carona['email_motorista'] == usuario_logado['email']:
            caronas.remove(carona)
            print('Carona cancelada com sucesso!')
            return caronas
    print('Carona não encontrada ou você não é o motorista dessa carona.')
    return caronas


def listar_caronas_disponiveis(caronas):
    if not caronas:
        print('Nenhuma carona disponível no momento.')
        return
    print('Caronas disponíveis:')
    for carona in caronas:
        print(
            f'ID: {carona['carona_id']}, Origem: {carona['origem']}, Destino: {carona['destino']}, '
            f'Data: {carona['data']}, Horário: {carona['horario']}, Vagas: {carona['vagas']}, Valor: R$ {carona['valor']} ')


def procurar_carona_por_rota(caronas):
    origem = input('Digite a cidade de origem: ')
    destino = input('Digite a cidade de destino: ')
    encontradas = []
    for carona in caronas:
        if (carona['origem'].lower() == origem.lower() and
                carona['destino'].lower() == destino.lower()):
            encontradas.append(carona)

    if not encontradas:
        print('Nenhuma carona encontrada com os critérios informados.')
        return

    print('Caronas encontradas:')
    for carona in encontradas:
        print(
            f'ID: {carona['carona_id']}, Motorista: {carona['nome_motorista']}, '
            f'Data: {carona['data']}, Horário: {carona['horario']}, Vagas: {carona['vagas']}')


def listar_minhas_reservas(caronas, usuario_logado):
    reservas = []
    for carona in caronas:
        if usuario_logado['email'] in carona['passageiros']:
            reservas.append(carona)

    if not reservas:
        print('Você não tem reservas ativas.')
        return

    print('Suas reservas:')
    for carona in reservas:
        print(
            f'ID: {carona['carona_id']}, Origem: {carona['origem']}, Destino: {carona['destino']}, '
            f'Data: {carona['data']}, Horário: {carona['horario']}, Vagas: {carona['vagas']}, Valor: R$ {carona['valor']}, ')