def configinicial(nomeprojetos, pastaprojetos):
    banco = pastaprojetos+"/"+nomeprojetos+".db"
    arquivo = '''
    pastaprojetos:'''+pastaprojetos+''',
    nomeprojetos:'''+nomeprojetos+''',
    banco:'''+banco+'''
    '''
    config = open("cfg.json", "w+")
    config.write(arquivo)
    config.close()


#variaveis de teste
nomebanco = "./teste3/teste3.db"
nomeprojetos = "teste3"
pastaprojetos = "./"
pastaprojeto = "./teste3"
nomeproj = "testin3"
nomearquivo = "queryteste.txt"
idprojeto = 1



from corefunc import *
iniciarproj(nomeproj, nomearquivo, pastaprojetos)


    
#configinicial(nomeprojetos, pastaprojetos)

    
    
#iniciarfit(nomeprojetos, pastaprojetos)
#iniciarproj(nomeproj, nomearquivo, pastaprojeto)
#alteracao(idprojeto)
