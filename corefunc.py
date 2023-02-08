import os
import shutil
from querys import *
import re

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

def alteracao(idprojeto, nomearquivo, linhasalteradas = 'NULL', observacoes = 'NULL', nomebanco = nomebanco):
    projeto = select(nomebanco, selectprojeto.format(idprojeto))
    versaoantiga = str(projeto["VERSAO_ATUAL"])
    updateprojetosvd(idprojeto)
    versao = str(projeto["VERSAO_ATUAL"])
    nomeext = nomearquivo.split(".")
    nomenovo = nomeext[0]+" "+versao+"."+nomeext[1]
    insertalt(idprojeto, versaoantiga, nomenovo, linhasalteradas, observacoes)
    updateprojetosa(idprojeto, nomenovo)
    shutil.copy(nomearquivo, projeto["PASTA_PROJETO"]+"/"+nomenovo)

