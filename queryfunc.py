#funções de querys
import sqlite3
from sqlite3 import Error

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

def select(banco, query):
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
