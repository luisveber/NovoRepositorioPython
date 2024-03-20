import xmltodict
import os
import json
import pandas as pd
def pegar_info(nome_arquivo,valores):
    # print(f"Pegou as informações {nome_arquivo}")
    with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)

        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo['NFe']['infNFe']
        else:
            infos_nf = dic_arquivo['nfeProc']['NFe']['infNFe']
        numero_nota = infos_nf['@Id']
        nNF = infos_nf['ide']['nNF']
        empresa_emissora = infos_nf['emit']['xNome']
        empresa_emissora_cnpj = infos_nf['emit']['CNPJ']
        nome_cliente = infos_nf['dest']['xNome']
        endereco =  infos_nf['dest']['enderDest']['xLgr']
        if "vol" in infos_nf['transp']:
            peso = infos_nf['transp']['vol']['pesoL']
        else:
            peso = "Não informado"
        valores.append([numero_nota,nNF, empresa_emissora,empresa_emissora_cnpj,nome_cliente, endereco,peso])

lista_arquivos = os.listdir("nfs")

colunas = ["numero_nota", "nNF", "empresa_emissora", "cnpj_empresa_emissora", "nome_cliente", "endereco", "peso"]
valores = []
for arquivo in lista_arquivos:
    pegar_info(arquivo, valores)

tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel("NotasFiscais.xlsx", index=False)
