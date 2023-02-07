#querys
import queryfunc

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

def criarbanco(banco):
    executaquery(banco, queryprojetos)
    executaquery(banco, queryalteracoes)

def insertcriacao(nomeprojeto, pastaprojeto, aquivo_base, banco = nomebanco):
    insertcriacao = '''
    INSERT INTO PROJETOS (NOME_PROJETO, PASTA_PROJETO, ARQUIVO_BASE, DATA_CRIACAO, VERSAO_ATUAL)
    VALUES('{}', '{}', '{}', DATETIME(), 0);
    '''
    query = insertcriacao.format(nomeprojeto, pastaprojeto, arquivobase)
    executaquery(banco, query)


def insertalt(idprojeto, versaoantiga, arquivo, linhasalteradas, observacoes, banco = nomebanco):
    insertalteracao = '''
    INSERT INTO ALTERACOES (ID_PROJETO, ARQUIVO, ULTIMO_ARQUIVO, DATA_ALTERACAO, LINHAS_ALTERADAS,  OBSERVACOES, VERSAO)
    VALUES({}, '{}', IIF({}=0, (SELECT ARQUIVO_BASE FROM PROJETOS WHERE ID_PROJETO = {}), (SELECT ARQUIVO_ATUAL FROM PROJETOS WHERE ID_PROJETO = {})), DATETIME(), '{}', '{}', (SELECT VERSAO_ATUAL FROM PROJETOS WHERE ID_PROJETO = {}));
    '''
    query = insertalteracao.format(idprojeto, arquivo, versaoantiga, idprojeto, idprojeto, linhasalteradas, observacoes, idprojeto)
    executaquery(banco, query)


def updateprojetosvd(idprojeto, banco = nomebanco):
    updateprojetosvd = '''
    UPDATE PROJETOS
    SET DATA_ULTIMA_ALTERACAO = DATETIME(),
        VERSAO_ATUAL = VERSAO_ATUAL+1
    WHERE ID_PROJETO = {};
    '''
    query = updateprojetosvd.format(idprojeto)
    executaquery(banco, query)


def updateprojetosa(idprojeto, arquivoatual, banco = nomebanco):
    updateprojetosa = '''
    UPDATE PROJETOS
    SET ARQUIVO_ATUAL = '{}'
    WHERE ID_PROJETO = {};
    '''
    query = updateprojetosa.format(arquivoatual, idprojeto)
    executaquery(banco, query)
