def configinicial(nomeprojetos, pastaprojetos):
    banco = pastaprojetos+"/"+nomeprojetos+"/"+nomeprojetos+".db"
    print(banco)
    arquivo = '''
    pastaprojetos:'''+pastaprojetos+"/"+nomeprojetos+''',
    nomeprojetos:'''+nomeprojetos+''',
    banco:'''+banco+'''
    '''
    config = open("cfg.cvq", "w+")
    config.write(arquivo)
    config.close()
    print("Arquivo de configuração criado com os seguintes parâmetros\n", arquivo)