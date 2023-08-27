# ler arquivos xml
import xmltodict
import os
import pandas as pd
import numpy
import openpyxl


def pegar_infos(nome_arquivo,valores):
    with open(f'nfs/{nome_arquivo}','rb') as arquivo_xml: # lendo o arquivo
        dic_arquivo = xmltodict.parse(arquivo_xml) # transformar o xlm em um dicionario
        if "NFe" in dic_arquivo:
            infos_nf = dic_arquivo["NFe"]["infNFe"]
        else:
            infos_nf = dic_arquivo["nfeProc"]["NFe"]['infNFe']
        numero_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf['emit']['xNome']
        nome_cliente = infos_nf['dest']['xNome']
        endereco = infos_nf['dest']['enderDest']
        if "vol" in infos_nf['transp']:
            peso = infos_nf['transp']['vol']['pesoB']
        else:
            peso = "Não informado"
        valores.append([numero_nota,empresa_emissora,nome_cliente,endereco,peso])


arquivos = os.listdir("nfs")

# Criando uma tablea
colunas = ["numero_nota","empresa_emissora","nome_cliente","endereco","peso"]
valores = []

for arquivo in arquivos:
    pegar_infos(arquivo,valores)

tabela = pd.DataFrame(columns=colunas,data=valores)
tabela.to_excel("NotasFicais.xlsx",index= False) # Criando tabela no excel