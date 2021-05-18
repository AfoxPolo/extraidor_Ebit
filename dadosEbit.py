""" atenção! """
""" infelizmente não esta mais funcionando :( pois o site atualizou, em breve tenterei fazer algo semelhante. """

import webbrowser
import requests
from bs4 import BeautifulSoup
import json

"""fechamento"""
af = '\033[m'

"""vermelho"""
a31 = '\033[1;31m'

"""verde"""
a32 = '\033[1;32m'

"""amarelo"""
a33 = '\033[1;33m'

"""azul"""
a34 = '\033[1;34m'

"""blold"""
abl = '\033[1m'


def corpo():
    link = f'https://www.ebit.com.br/reputacao-de-lojas?m={medalha}'
    req = requests.get(link).text
    soup = BeautifulSoup(req, 'html.parser')

    var = soup.find("input", {"id": "JSONCompanyReputation"}).get('value')
    json_var = (json.loads(var))
    json_data = json_var['Data']

    nome_loja = list()
    for a in json_data:
        nome_loja.append(str(a['CompanyName']))

    descricao_loja = list()
    for a in json_data:
        if a['CompanyDescription'] == '' or not(a['CompanyDescription']):
            descricao_loja.append('Sem Descrição')
        else:
            li = [a['CompanyDescription']]
            conta_ctr = 0
            txt = ''
            limite_linha = 50
            for letra in li[0]:
                conta_ctr += 1
                if conta_ctr == limite_linha:
                    limite_linha += 50
                    txt += '\n'
                else:
                    txt += letra
            txt = txt.strip()
            descricao_loja.append(str(txt))

    link_loja = list()
    for a in json_data:
        link_loja.append(str(a['StoreUrl']))

    quantidade_de_lojas = len(nome_loja)
    for posicao in range(0, quantidade_de_lojas):
        print('.' * 50)
        print(f'〔{posicao + 1}〕{nome_loja[posicao]}')
        print(f'{descricao_loja[posicao]}')
        print('\n')
    return link_loja, quantidade_de_lojas


re_do_programa = 0
ultima_medalha = 'diamante'
ultimos_dados_corpo = ''
while True:
    re_do_programa += 1
    if re_do_programa == 1:
        print(f'{a34}━{af}' * 50)
        print(f'{abl}《1》Diamante\n'
              f'《2》Ouro\n'
              f'《3》Prata\n'
              f'《4》Bronze{af}')
        print(f'{a34}━{af}' * 50)
        print('Digite á opçao de medalha do site'.center(50))
        print(f'Ou digite {a31}"sair"{af} para sair'.center(59))
        print(f'{a34}━{af}' * 50)
        lista_medalha = ['diamante', 'ouro', 'prata', 'bronze']
        opcao = input(f'{a34}R➜ {af}')
        if opcao.isnumeric():
            opcao = int(opcao)
            if opcao in range(1, 5):
                opcao = int(opcao)
                medalha = lista_medalha[opcao - 1]
                ultima_medalha = medalha
                ultimos_dados_corpo = corpo()
            else:
                print(a31)
                print('ERRO - Ésta opção nãe é valida.'.center(44, '✘'))
                print(af)
                re_do_programa -= 1
        else:
            if opcao.lower().strip() == 'sair':
                print(f'{a33}Programa finalizado pelo usuario.{af}')
                break
            else:
                print(a31)
                print('ERRO - Digite uma opção valida.'.center(44, '✘'))
                print(af)
                re_do_programa -= 1
    else:
        print(f'{a34}━{af}' * 50)
        print(f'{abl}《1》Diamante\n'
              f'《2》Ouro\n'
              f'《3》Prata\n'
              f'《4》Bronze{af}')
        print(f'{a34}┅{af}' * 50)
        print('Digite á opçao de medalha'.center(50))
        print(f'Ou digite {a31}"sair"{af} para sair'.center(59))
        print('Ou digite "site" para abrir o link de uma loja'.center(50))
        print(f'{a34}┅{af}' * 50)
        lista_medalha = ['diamante', 'ouro', 'prata', 'bronze']
        opcao = input(f'{a34}R➜ {af}')
        if opcao.isnumeric():
            opcao = int(opcao)
            if opcao in range(1, 5):
                opcao = int(opcao)
                medalha = lista_medalha[opcao - 1]
                ultima_medalha = medalha
                ultimos_dados_corpo = corpo()
            else:
                print(a31)
                print('ERRO - Ésta opção nãe é valida.'.center(44, '✘'))
                print(af)
        else:
            if opcao.lower().strip() == 'sair':
                print(f'{a32}Programa finalizado pelo usuario.{af}')
                break
            elif opcao.lower().strip() == 'site':
                while True:
                    opcao_site = input(f'R➜ Digite o numero do site ou {a31}"sair"{af} para sair: ')
                    if opcao_site.isnumeric():
                        opcao_site = int(opcao_site)
                        if opcao_site in range(1, len(ultimos_dados_corpo[0]) + 1):
                            webbrowser.open_new(ultimos_dados_corpo[0][opcao_site - 1])
                            break
                        else:
                            print(a31)
                            print('ERRO - Este numero é invalido.'.center(44, '✘'))
                            print(af)
                    else:
                        if opcao_site.lower().strip() == 'sair':
                            break
                        else:
                            print(a31)
                            print('ERRO - Digite uma opção valida.'.center(44, '✘'))
                            print(af)

            else:
                print(a31)
                print('ERRO - Digite uma opção valida.'.center(44, '✘'))
                print(af)
