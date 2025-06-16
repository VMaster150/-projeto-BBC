def dados():
    usuarios = []
    caronas = []
    carona_id_counter = 1

    usuario_inicial = {
        'nome': 'geraldo',
        'email': 'geraldo@victor.com',
        'senha': '123456'
    }

    carona_inicial = {
        'origem': 'triunfo',
        'destino': 'cajazeiras',
        'data': '13/05/2025',
        'horario': '22:20',
        'vagas': 4,
        'carona_id': carona_id_counter,
        'email_motorista': 'geraldo@victor.com',
        'nome_motorista': 'geraldo',
        'passageiros': [],
        'valor': 5
    }

    usuarios.append(usuario_inicial)
    caronas.append(carona_inicial)

    return usuarios, caronas, carona_id_counter + 1

