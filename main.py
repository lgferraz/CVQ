from sys import argv
#variaveis de teste
nomebanco = "./teste3/teste3.db"
nomeprojetos = "teste3"
pastaprojetos = "."
pastaprojeto = "./teste3"
nomeproj = "testin3"
nomearquivo = "queryteste.txt"
nomearquivodois = "queryteste1.txt"
idprojeto = 1

header = '''                                                                                       
                                                                                        
        CCCCCCCCCCCCC          VVVVVVVV           VVVVVVVV               QQQQQQQQQ      
     CCC::::::::::::C          V::::::V           V::::::V             QQ:::::::::QQ    
   CC:::::::::::::::C          V::::::V           V::::::V           QQ:::::::::::::QQ  
  C:::::CCCCCCCC::::C          V::::::V           V::::::V          Q:::::::QQQ:::::::Q 
 C:::::C       CCCCCC           V:::::V           V:::::V           Q::::::O   Q::::::Q 
C:::::C                          V:::::V         V:::::V            Q:::::O     Q:::::Q 
C:::::C                           V:::::V       V:::::V             Q:::::O     Q:::::Q 
C:::::C                            V:::::V     V:::::V              Q:::::O     Q:::::Q 
C:::::C                             V:::::V   V:::::V               Q:::::O     Q:::::Q 
C:::::C                              V:::::V V:::::V                Q:::::O     Q:::::Q 
C:::::C                               V:::::V:::::V                 Q:::::O  QQQQ:::::Q 
 C:::::C       CCCCCC                  V:::::::::V                  Q::::::O Q::::::::Q 
  C:::::CCCCCCCC::::C                   V:::::::V                   Q:::::::QQ::::::::Q 
   CC:::::::::::::::C                    V:::::V                     QQ::::::::::::::Q  
     CCC::::::::::::C                     V:::V                        QQ:::::::::::Q   
        CCCCCCCCCCCCC                      VVV                           QQQQQQQQ::::QQ 
                                                                                 Q:::::Q
                                                                                  QQQQQQ                                                                                        
                         Controlador de Versões de Querys
                                           Por: Lucas S. Ferraz
'''

print(header)
try:
    from corefunc import *
    from querys import testarconect
    print("[] Arquivo cgf.cvq carregado com sucesso.\n")
except Exception as e:
    from configfunc import configinicial
    pastaprojetos = input("[] Caminho da pasta onde serão guardados os projetos: ")
    nomeprojetos = input("[] Nome da pasta onde serão guardados os projetos: ")
    configinicial(nomeprojetos, pastaprojetos)
    raise SystemExit


if testarconect() == False:
    iniciarfit()
    print("[] Pasta e banco criado com sucesso.")
else:
    print("[] Banco e pasta já encontrados, prosseguindo para CVQ.")


while True:
    op = input('''
[] 1 -> Criar projeto
[] 2 -> Listar projetos
[] 3 -> Inicializar projeto
[] 4 -> Sair
>>> ''')
    if op == "1":
        nomeproj = input("[] Nome projeto: ")
        nomearquivo = input("[] Arquivo: ")
        iniciarproj(nomeproj, nomearquivo)
    elif op == "2":
        listarproj()
    elif op == "3":
        while True:
            idprojeto = input("[] Id projeto: ")
    elif op == "4":
        break
    else:
        print("[!] Selecione uma opção válida.")






#iniciarfit(nomeprojetos, pastaprojetos)
#iniciarproj(nomeproj, nomearquivo)

#alteracao(idprojeto, nomearquivodois)
