import re
import os
import shutil
import difflib
from querys import *


baseorig = "cfg.cvq"
orig = str(open(baseorig, "r").read())

pastaprojetos = re.search("pastaprojetos:.+", orig).group(0).split(":")[1].replace(" ", "").split(",")[0]
nomeprojetos = re.search("nomeprojetos:.+", orig).group(0).split(":")[1].replace(" ", "").split(",")[0]
nomebanco = re.search("banco:.+", orig).group(0).split(":")[1].replace(" ", "").split(",")[0]
     
selectprojeto = '''
SELECT
    *
FROM PROJETOS
WHERE
    ID_PROJETO = {}
'''

selectalt = '''
SELECT
    *
FROM ALTERACOES
WHERE
    ID_PROJETO = {}
'''

selecttudo = '''
SELECT
    *
FROM PROJETOS
'''

def iniciarfit(nomeprojetos = nomeprojetos, pastaprojetos = pastaprojetos, nomebanco = nomebanco):
        try:
            os.mkdir(pastaprojetos, 777)
            criarbanco(nomebanco)
        except Exception as e:
            print(e)

def iniciarproj(nomeproj, nomearquivo, pastaprojetos = pastaprojetos):
        try:
            pastaprojetos = pastaprojetos+"/"+nomeproj
            os.mkdir(pastaprojetos, 777)
            shutil.copy(nomearquivo, pastaprojetos)
            insertcriacao(nomeproj, pastaprojetos, nomearquivo)
        except Exception as e:
            print(e)

def linhasalteradas(arquivobase, arquivonovo):
    arquivobase = str(open(arquivobase, "r").read()).split("\n")
    arquivonovo = str(open(arquivonovo, "r").read()).split("\n")
    html_diff = difflib.HtmlDiff().make_file(arquivobase, arquivonovo)
    return html_diff

def alteracao(idprojeto, nomearquivo, observacoes = 'NULL', nomebanco = nomebanco):
    projeto = select(nomebanco, selectprojeto.format(idprojeto))
    versaoantiga = str(projeto["VERSAO_ATUAL"])
    arquivoantigo = projeto["PASTA_PROJETO"]+"/"+projeto["ARQUIVO_ATUAL"]
    linhasalt = linhasalteradas(arquivoantigo, nomearquivo)
    updateprojetosvd(idprojeto)
    versao = str(projeto["VERSAO_ATUAL"])
    nomeext = nomearquivo.split(".")
    nomenovo = nomeext[0]+" "+versao+"."+nomeext[1]
    insertalt(idprojeto, versaoantiga, nomenovo, linhasalt, observacoes)
    updateprojetosa(idprojeto, nomenovo)
    shutil.copy(nomearquivo, projeto["PASTA_PROJETO"]+"/"+nomenovo)

