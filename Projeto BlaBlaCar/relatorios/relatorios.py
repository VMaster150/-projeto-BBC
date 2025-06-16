from fpdf import FPDF
import os
from utilidades.utilidades import limpar_tela
import time

def gerar_pdf_usuarios(usuarios):
    if not os.path.exists('../Projeto/relatorios'):
        os.makedirs('../Projeto/relatorios')

    pdf = FPDF(orientation='L')
    pdf.add_page()
    pdf.set_font('Arial', size=12)

    pdf.cell(0, 10, ln=1, align='C')
    pdf.ln(10)

    pdf.set_font('Arial', size=10, style='B')
    col_widths = [60, 80, 60]

    headers = ['Nome', 'Email', 'Senha']
    for i in range(len(headers)):
        pdf.cell(col_widths[i], 10, headers[i], border=1)
    pdf.ln()

    pdf.set_font('Arial', size=9)
    if not usuarios:
        pdf.cell(0, 10, 'Nenhum usuário cadastrado.', ln=1, align='C')
    else:
        for usuario in usuarios:
            pdf.cell(col_widths[0], 10, usuario['nome'], border=1)
            pdf.cell(col_widths[1], 10, usuario['email'], border=1)
            pdf.cell(col_widths[2], 10, usuario['senha'], border=1)
            pdf.ln()

    pdf_file = os.path.join('../Projeto/relatorios', 'lista_usuarios.pdf')
    pdf.output(pdf_file)
    print(f'Relatório PDF gerado com sucesso: {pdf_file}')
    time.sleep(3)
    limpar_tela()

def gerar_pdf_caronas(caronas):
    if not os.path.exists('../Projeto/relatorios'):
        os.makedirs('../Projeto/relatorios')

    pdf = FPDF(orientation='L')
    pdf.add_page()
    pdf.set_font('Arial', size=12)

    pdf.cell(0, 10, ln=1, align='C')
    pdf.ln(10)

    pdf.set_font('Arial', size=9, style='B')
    col_widths = [15, 35, 35, 25, 20, 15, 60]

    headers = ['ID', 'Origem', 'Destino', 'Data', 'Horário', 'Vagas', 'Motorista (Email)']
    for i in range(len(headers)):
        pdf.cell(col_widths[i], 10, headers[i], border=1)
    pdf.ln()

    pdf.set_font('Arial', size=8)
    if not caronas:
        pdf.cell(0, 10, 'Nenhuma carona cadastrada.', ln=1, align='C')
    else:
        for carona in caronas:
            pdf.cell(col_widths[0], 10, str(carona['carona_id']), border=1)
            pdf.cell(col_widths[1], 10, carona['origem'], border=1)
            pdf.cell(col_widths[2], 10, carona['destino'], border=1)
            pdf.cell(col_widths[3], 10, carona['data'], border=1)
            pdf.cell(col_widths[4], 10, carona['horario'], border=1)
            pdf.cell(col_widths[5], 10, str(carona['vagas']), border=1)
            pdf.cell(col_widths[6], 10, carona['email_motorista'], border=1)
            pdf.ln()

    pdf_file = os.path.join('../Projeto/relatorios', 'lista_caronas.pdf')
    pdf.output(pdf_file)
    print(f'Relatório PDF gerado com sucesso: {pdf_file}')
    time.sleep(3)
    limpar_tela()
def gerar_pdp_valores_caronas(caronas):
    if not os.path.exists('../Projeto/relatorios'):
        os.makedirs('../Projeto/relatorios')

    pdf = FPDF(orientation='L')
    pdf.add_page()
    pdf.set_font('Arial', size=12)

    pdf.cell(0, 10, ln=1, align='C')
    pdf.ln(10)

    pdf.set_font('Arial', size=9, style='B')
    headers = ['ID', 'Origem', 'Destino', 'Valor' ]
    col_widths = [15, 35, 35, 20]
    for i in range(len(headers)):
        pdf.cell(col_widths[i], 10, headers[i], border=1)
    pdf.ln()
    pdf.set_font('Arial', size=8)
    if not caronas:
        pdf.cell(0, 10, 'Nenhuma carona cadastrada.', ln=1, align='C')
    else:
        for carona in caronas:
            pdf.cell(col_widths[0], 10, str(carona['carona_id']), border=1)
            pdf.cell(col_widths[1], 10, carona['origem'], border=1)
            pdf.cell(col_widths[2], 10, carona['destino'], border=1)
            pdf.cell(col_widths[3], 10, str(carona['valor']), border=1)
            pdf.ln()
def download_lista_usuarios(usuarios):
    if not os.path.exists('../Projeto/relatorios'):
        os.makedirs('../Projeto/relatorios')

    with open('relatorios/lista_usuarios.txt', 'w') as doc:
        if not usuarios:
            doc.write('Nenhum usuário cadastrado.\n')
        else:
            for usuario in usuarios:
                doc.write(f'Nome: {usuario['nome']}, E-mail: {usuario['email']}\n')

    print('Lista de usuários salva em relatorios/lista_usuarios.txt')
    time.sleep(3)
    limpar_tela()

def download_lista_caronas(caronas):
    if not os.path.exists('../Projeto/relatorios'):
        os.makedirs('../Projeto/relatorios')

    with open('relatorios/lista_caronas.txt', 'w') as doc:
        if not caronas:
            doc.write('Nenhuma carona cadastrada.\n')
        else:
            for carona in caronas:
                doc.write(
                    f'ID: {carona['carona_id']}, Motorista: {carona['nome_motorista']}, '
                    f'Origem: {carona['origem']}, Destino: {carona['destino']}, '
                    f'Data: {carona['data']}, Horário: {carona['horario']}, '
                    f'Vagas: {carona['vagas']}\n')

    print('Lista de caronas salva em relatorios/lista_caronas.txt')
    time.sleep(3)
    limpar_tela()
def download_lista_valores_caronas(caronas):
    if not os.path.exists('../Projeto/relatorios'):
        os.makedirs('../Projeto/relatorios')

    with open('relatorios/lista_valores_caronas.txt', 'w') as doc:
        if not caronas:
            doc.write('Nenhuma carona cadastrada.\n')
        else:
            for carona in caronas:
                doc.write(
                    f'ID: {carona['carona_id']}, Origem: {carona['origem']}, '
                    f'Destino: {carona['destino']}, Valor: {carona['valor']}\n')

    print('Lista de valores de caronas salva em relatorios/lista_valores_caronas.txt')
    time.sleep(3)
    limpar_tela()
def download_lista_valores_caronas(caronas):
    if not os.path.exists('../Projeto/relatorios'):
        os.makedirs('../Projeto/relatorios')

    with open('relatorios/lista_valores_caronas.txt', 'w') as doc:
        if not caronas:
            doc.write('Nenhuma carona cadastrada.\n')
        else:
            for carona in caronas:
                doc.write(
                    f' Usuário: {carona['nome_motorista']}, Valor: {carona['valor']}\n')

    print('Lista de valores de caronas salva em relatorios/lista_valores_caronas.txt')
    time.sleep(3)
    limpar_tela()