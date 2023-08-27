# ler arquivos xml
import xmltodict
import os
import json

def pegar_infos(nome_arquivo):
    with open(f'nfs/{nome_arquivo}','rb') as arquivo_xml: # lendo o arquivo
        dic_arquivo = xmltodict.parse(arquivo_xml) # transformar o xlm em um dicionario
        try:
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
        except Exception as e:
            print(e)
            print(json.dumps(dic_arquivo, indent=4))


arquivos = os.listdir("nfs")

for arquivo in arquivos:
    pegar_infos(arquivo)
