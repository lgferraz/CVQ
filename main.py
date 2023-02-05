import os
import re
import shutil
import sqlite3
from sqlite3 import Error

#variaveis de teste
nomebanco = "./teste3/teste3.db"
nomeprojetos = "teste3"
pastaprojetos = "./"
pastaprojeto = "./teste3"
nomeproj = "testin3"
nomearquivo = "queryteste.txt"
idprojeto = 1

#querys
queryprojetos = '''
CREATE TABLE PROJETOS (
    ID_PROJETO INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME_PROJETO TEXT NOT NULL,
    PASTA_PROJETO TEXT NOT NULL,
    ARQUIVO_ATUAL TEXT,
    ARQUIVO_BASE TEXT NOT NULL,
    DATA_CRIACAO DATETIME NOT NULL,
    DATA_ULTIMA_ALTERACAO DATETIME,
    VERSAO_ATUAL INTENGER NOT NULL
    );
'''
queryalteracoes = '''
CREATE TABLE ALTERACOES (
    ID_ALTERACAO INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_PROJETO INTEGER NOT NULL,
    ARQUIVO TEXT NOT NULL,
    ULTIMO_ARQUIVO TEXT,
    DATA_ALTERACAO NOT NULL,
    LINHAS_ALTERADAS TEXT,
    OBSERVACOES TEXT,
    VERSAO INT
    );
'''
insertcriacao = '''
INSERT INTO PROJETOS (NOME_PROJETO, PASTA_PROJETO, ARQUIVO_BASE, DATA_CRIACAO, VERSAO_ATUAL)
VALUES('{}', '{}', '{}', DATETIME(), 0);
'''
insertalteracao = '''
INSERT INTO ALTERACOES (ID_PROJETO, ARQUIVO, ULTIMO_ARQUIVO, DATA_ALTERACAO, LINHAS_ALTERADAS,  OBSERVACOES, VERSAO)
VALUES({}, '{}', IIF({}=0, (SELECT ARQUIVO_BASE FROM PROJETOS WHERE ID_PROJETO = {}), (SELECT ARQUIVO_ATUAL FROM PROJETOS WHERE ID_PROJETO = {})), DATETIME(), '{}', '{}', (SELECT VERSAO_ATUAL FROM PROJETOS WHERE ID_PROJETO = {}));
'''

updateprojetosvd = '''
UPDATE PROJETOS
SET DATA_ULTIMA_ALTERACAO = DATETIME(),
    VERSAO_ATUAL = VERSAO_ATUAL+1
WHERE ID_PROJETO = {};
'''

updateprojetosa = '''
UPDATE PROJETOS
SET ARQUIVO_ATUAL = '{}'
WHERE ID_PROJETO = {};
'''

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
    
def criarbanco(nome, pasta):
    conn = None;
    try:
        conn = sqlite3.connect(pasta+"/"+nome+".db")
        cursor = conn.cursor()
        conn.execute(queryprojetos)
        conn.execute(queryalteracoes)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def executaquery(banco, query):
    conn = None;
    try:
        conn = sqlite3.connect(banco)
        cursor = conn.cursor()
        conn.execute(query)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def select(banco, query, resultados = 1):
    result = {}
    conn = sqlite3.connect(banco)
    cursor = conn.cursor()
    cursor.execute(query)
    linhas = cursor.fetchall()
    for linha in linhas:
        indexlinha = linhas.index(linha)
        for coluna in range(0, len(linha)):
            nomecoluna = cursor.description[coluna][0]
            conteudocoluna = linha[coluna]
            result[nomecoluna] = conteudocoluna
    conn.close()
    return result

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
            executaquery(nomebanco, insertcriacao.format(nomeproj, pasta, nomearquivo))
        except e:
            print(e)

def insertalt(idprojeto, versaoantiga, arquivo, linhasalteradas, observacoes, banco = nomebanco):
    executaquery(banco, insertalteracao.format(idprojeto, arquivo, versaoantiga, idprojeto, idprojeto, linhasalteradas, observacoes, idprojeto))

def alteracao(idprojeto, nomearquivo = nomearquivo, banco = nomebanco, linhasalteradas = 'NULL', observacoes = 'NULL'):
    projeto = select(banco, selectprojeto.format(idprojeto))
    versaoantiga = str(projeto["VERSAO_ATUAL"])
    executaquery(banco, updateprojetosvd.format(idprojeto))
    versao = str(projeto["VERSAO_ATUAL"])
    nomeext = nomearquivo.split(".")
    nomenovo = nomeext[0]+" "+versao+"."+nomeext[1]
    insertalt(idprojeto, versaoantiga, nomenovo, linhasalteradas, observacoes)
    executaquery(banco, updateprojetosa.format(nomenovo, idprojeto))
    shutil.copy(nomearquivo, projeto["PASTA_PROJETO"]+"/"+nomenovo)
    
#iniciarfit(nomeprojetos, pastaprojetos)
#iniciarproj(nomeproj, nomearquivo, pastaprojeto)
alteracao(idprojeto)
