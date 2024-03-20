import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from src.controler.pessoa import Pessoa, PessoaController
from src.models.pessoa import Pessoa



while True:
    decisao = int(input('Digite 1 para salvar e 2 para listar '))
    if decisao == 1:
        nome = input('Nome:')
        sobrenome = input('Sobrenome:')
        idade = input('Idade:')
        cpf = input('Cpf:')

        p1 = Pessoa(nome=nome, sobrenome=sobrenome, idade=idade, cpf=cpf)
        PessoaController.salvar_pessoa(p1)
    elif decisao == 2:
        for i in PessoaController.listar_pessoas():
            print(f'Nome : {i.nome}')
            print(f'Sobrenome : {i.sobrenome}')
            print(f'idade : {i.idade}')
            print(f'cpf : {i.cpf}')