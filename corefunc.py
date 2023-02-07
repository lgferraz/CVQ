import os
import shutil
import querys

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

def configinicial(nomeprojetos, pastaprojetos):
    banco = pastaprojetos+"/"+nomeprojetos+".db"
    arquivo = '''
    {
    'pastaprojetos':'{}',
    'nomeprojetos':'{}',
    'banco':'{}'
    }
    '''.format(nomeprojetos, pastaprojetos, banco)
    config = open("cfg.json", "w+")
    config.write(arquivo)
    config.close()

def iniciarfit(nome, pasta):
        try:
            os.mkdir(pasta+nome, 777)
            criarbanco(nome, pasta+nome)
        except e:
            print(e)

def iniciarproj(nomeproj, nomearquivo, pasta):
        try:
            pasta = pasta+"/"+nomeproj
            os.mkdir(pasta, 777)
            shutil.copy(nomearquivo, pasta)
            insertcriacao(nomeprojeto, pasta, nomearquivo)
        except e:
            print(e)

def alteracao(idprojeto, nomearquivo, banco = nomebanco, linhasalteradas = 'NULL', observacoes = 'NULL'):
    projeto = select(banco, selectprojeto.format(idprojeto))
    versaoantiga = str(projeto["VERSAO_ATUAL"])
    updateprojetosvd(idprojeto)
    versao = str(projeto["VERSAO_ATUAL"])
    nomeext = nomearquivo.split(".")
    nomenovo = nomeext[0]+" "+versao+"."+nomeext[1]
    insertalt(idprojeto, versaoantiga, nomenovo, linhasalteradas, observacoes)
    updateprojetosa(idprojeto, nomenovo)
    shutil.copy(nomearquivo, projeto["PASTA_PROJETO"]+"/"+nomenovo)

