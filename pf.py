import random #FUNÇÃO QUE RANDOMIZA A CAPTURA DAS CONTAS CORRENTES DO ARQUIVO CONTAS.TXT
import ast
import pywhatkit as whatsapp
from datetime import datetime

def pessoa_fisica():
    
    #CRIA CONTA DE CLIENTE
    def cria_conta(numero,titular,contato,saldo,limite,poupanca):
        
        conta={"Conta Corrente": numero,"Titular":titular,"Contato": contato,"Saldo":saldo ,"Cheque Especial":limite, "Conta Poupança": poupanca}
        
        return conta
   

    #DEPOSITA VALORES NA CONTA CORRENTE
    def deposita(conta,valor):
        conta['Saldo']+= valor

    #SACA VALORES DA CONTA CORRENTE
    def sacar(conta,valor):
        conta['Saldo'] -= valor

        if conta['Saldo'] <0:
            print("\nATENÇÃO! SALDO NEGATIVO! R${} \n".format(conta['saldo']))

    #IMPRIME EXTRATO DA CONTA CORRENTE E IMPRIME LIMITE DO CHEQUE ESPECIAL
    def extrato(conta):
        #print("Sr.(a) cliente {} da conta corrente de número {} , consulte seu saldo abaixo".format(conta['Titular'], conta['Conta Corrente']))
        print("\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("O saldo atual da conta {} é: R$ {}".format(conta['Conta Corrente'], conta['Saldo']))
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n")
        #print("\nO limite atualizado do seu cheque especial é de R${}\n".format(conta['Cheque Especial']))
        #if conta['Saldo'] <0:
          #  print("\nATENÇÃO! SALDO NEGATIVO! \n")

    #TRANSFERE VALORES DO CHEQUE ESPECIAL PARA CONTA CORRENTE
    def cheque_especial(conta,valor):
        if conta['Cheque Especial']>0:
            print("\nO valor inicial do seu cheque especial é de R$ {}".format(conta['limite']))
            conta['Cheque Especial'] -= valor
            conta['Saldo'] += valor
            print("\nO valor atualizado do limite do seu cheque especial é R${}\n Valor transferido para conta corrente com sucesso!\n".format(conta['Cheque Especial']))
        elif conta['Cheque Especial'] < valor:
            print("\nVocê não possui limite suficiente para realizar este tipo de operação!\n") 
        elif conta['Cheque Especial']< 0:
            print("\nVocê não possui mais limite para usar seu cheque especial!\n")
            
   
    
    
    print("----------------------------------------\n")
    print("|     Python BankLine - Pessoa Física    |")
    print("\n----------------------------------------")
    
    #MENU PARA O USUÁRIO ESCOLHER A OPERAÇÃO QUE DESEJA REALIZAR
    while True:
        continua = str(input("Deseja realizar mais alguma operação?: Y ou N =>  "))
        if continua.upper() == "Y":
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("| 1. Criar conta corrente pessoa física              |")
            print("| 2. Listar contas cadastradas                       |")
            print("| 3. Acessar dados dos clientes já cadastrados       |")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            opt=int(input("\nDigite a opção desejada:  "))
          
            if opt == 1:#cadastra novas contas e salva no arquivo pessoafisica.txt
                    arq = open('contas_pf.txt', 'r')
                    contas =[]
                    for linha in arq:
                                    linha = linha.strip()
                                    contas.append(linha)
                    arq.close()
                                #print(arq.read())
                    numero = random.randrange(0,len(contas)) #RANDOMIZA A CAPTURA DAS CONTAS
                    numConta = contas[numero] #VARIÁVEL QUE CAPTURA O NUMERO DA CONTA
                    nomeTitular=str(input("\nDigite o nome do titular da conta: ")) #TITULAR DA CONTA
                    nCel = str(input("\nTelefone para contato: ")) #NÚMERO DE CONTATO DO CLIENTE
                    saldoTitular=int(input("\nInsira seu saldo inicial: R$ ")) #SALDO INICIAL
                      
                    file =open('pessoafisica.txt','r') #ABERTURA E LEITURA DO ARQUIVO PESSOA FISICA
                    flag=0
                    index=0
                    
                    for line in file:
                        index +=1

                        if numConta in line:
                            flag = 1
                            break
                 
                    if flag == 0: #VERIFICA SE A CONTA JÁ EXISTE. SE NÃO, CADASTRA NOVO CLIENTE
                            #print('A conta corrente de número ', numConta,' não existe. Prossiga com o cadastro')
                            date = datetime.today().strftime('%A, %B %d, %Y  %H:%M:%S') #CAPTURA DATA E HORA
                            c1=cria_conta(numConta,	nomeTitular.upper(),nCel,saldoTitular , 2000, 0) #C1 CRIA UM NOVO CLIENTE
                            
                            conta_fisica=c1
                            arch=open('pessoafisica.txt','a')
                            arch.write("\n"+str(conta_fisica)+"\n") #salva os dados do cliente pessoa física no arquivo pessoafisica.txt
                            arch.close()
                            
                            print("\nObrigado por escolher nosso banco!\n")
                            print("\nConta cadastrada em {}".format(date))
                            extrato(c1)     
                              
                    else: #SE CONTA EXISTE, SAI DESSE MENU
                            print('A conta corrente de número ', numConta,' já encontra-se cadastrada na linha',index)
                    file.close()  

                    
            elif opt == 2: #faz a leitura dos registros gravados no arquivo pessoafisica.txt
                    arch=open('pessoafisica.txt','r') 
                    print("\n"+arch.read()+"\n") #LISTA OS CLIENTES CADASTRADOS
                    arch.close()

            elif opt == 3: #ACESSA O CADASTRO DENTRO DO ARQUIVO TXT E EFETUA O SAQUE OU DEPÓSITO
                    
                    search =str(input("\nFaça a busca pelo número da conta ou pelo nome do cliente => "))   
                    file =open('pessoafisica.txt','r+') #procura dentro do arquivo a conta digitada
                    flag=0
                    index=0
                    for line in file:
                        index +=1
                        

                        if search.upper() in line:
                            dados = ast.literal_eval(line)
                           
                            lista = line
                            lista = lista.split()
                            flag = 1
                            break

                    if flag == 0:
                            print('Conta Corrente/Cliente', search.upper(),'inexistente')
                            
                              
                    else:
                            
                            print('Conta Corrente/Cliente', search.upper(),'existente na linha ',index)
                            #OPERAÇÕES
                            print("\n 1) Sacar \n 2) Depositar \n 3) Enviar notificação \n 4) Emitir extrato")
                            var = int(input("\nEscolha uma das opções acima => "))
                            
                            if var == 1: #SACAR
                                sq=int(input("Qual valor deseja sacar? => R$ "))
                                
                                oldSaldo = dados["Saldo"] #variável oldSaldo recebe o valor que consta na conta corrente do cliente
                                resultado = oldSaldo - sq #variável resultado recebe o valor da operação feita entre o valor da conta corrente menos o valor do saque
                                
                                print(resultado)   #IMPRIMIU O NOVO SALDO, APÓS O SAQUE EFETUADO                            
                                
                                newLista = line.replace(str(oldSaldo),str(resultado).title()) 
                                
                                
                                print("\nSaque realizado com sucesso!\n")
                                print("\nSenhor(a) {}, seu saldo atual é R$ {}\n".format(dados["Titular"],resultado))#imprime extrato resumido
                                
                                file=open("pessoafisica.txt", "a")
                                file.write("\n"+str(newLista))
                                file.close()
                            
                            elif var == 2: #DEPOSITAR
                                dp=int(input("Qual valor deseja depositar? => R$ "))
                                oldSaldo = dados["Saldo"]#variável oldSaldo recebe o valor que consta na conta corrente do cliente
                                resultado = oldSaldo + dp #variável resultado recebe o valor da operação feita entre o valor da conta corrente menos o valor do saque
                                
                                print(resultado)   #IMPRIMIU O NOVO SALDO, APÓS O SAQUE EFETUADO                            
                                newLista = line.replace(str(oldSaldo),str(resultado).title())
                                print("\nDepósito  realizado com sucesso!\n")
                                print("\nSenhor(a) {}, seu saldo atual é R$ {}\n".format(dados["Titular"],resultado)) #imprime extrato resumido
                                
                                file=open("pessoafisica.txt", "a")
                                file.write("\n"+str(newLista))
                                file.close()

                            elif var == 3: #ENVIAR MENSAGEM PARA OS CLIENTES
                                celular= dados["Contato"]
                                msg=str(input("\nSua mensagem: "))
                                hora = int(input("\nHorário de envio => "))
                                minuto= int(input("\nMinuto exato => "))
                                #hour = datetime.today().strftime('%H:%M:%S')
                                #data = datetime.today().strftime('%B %d, %Y')
                                try:
                                    whatsapp.sendwhatmsg(celular, msg,hora,minuto)
                                    print("\nMensagem enviada com sucesso!\n")
                                    #print("\nMensagem enviada às {} do dia {}".format(hour,data))
                                except:
                                    print("\nDEU ERRADO!\n")

                            elif var == 4: #EMITIR EXTRATO
                                date = datetime.today().strftime('%A, %B %d, %Y  %H:%M:%S')
                                print("\n"+str(date)+"\n")
                                print("\nSeja bem-vindo Sr.(a) {}. Consulte seu extrato abaixo".format(dados["Titular"]))
                                extrato(dados)
                            
                                                           
                    file.close()   


            elif opt > 9 : #em caso de opção incorreta, retorna ao menu principal
                    print("\nOpção incorreta! Por favor, digite a opção correta!\n")

        elif continua.upper() == "N" : #CASO O USUÁRIO NÃO QUEIRA MAIS FAZER NADA, DIGITA "N" E SAI DO SISTEMA
            print("\nOBRIGADO POR USAR NOSSO BANCO! ATÉ LOGO\n")
            exit()
        elif continua.upper() != "Y" or "N":
            print("\nDigite uma opção correta!\n")




#CADASTRO DE PESSOA JURÍDICA
def pessoa_juridica():
    
    #CRIA CONTA DE CLIENTE
    def cria_conta(numero,cnpj,nome,titular,contato,saldo):
        conta={"Conta Corrente": numero,"CNPJ": cnpj,"Razão Social":nome,"Titular":titular,"Contato": contato,"Capital Social":saldo }
        return conta

   
    #DEPOSITA VALORES NA CONTA CORRENTE
    def deposita(conta,valor):
        conta['Capital Social']+= valor

    #SACA VALORES DA CONTA CORRENTE
    def sacar(conta,valor):
        conta['Capital Social'] -= valor

        if conta['Capital Social'] <0:
            print("\nATENÇÃO! SALDO NEGATIVO! R${} \n".format(conta['Capital Social']))


    #IMPRIME EXTRATO DA CONTA CORRENTE E IMPRIME LIMITE DO CHEQUE ESPECIAL
    def extrato(conta):
        print("\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
        print("O saldo atual da conta {} é: R$ {}".format(conta['Conta Corrente'], conta['Capital Social']))
        print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n")
        
       
    print("----------------------------------------\n")
    print("|   Python BankLine - Pessoa Jurídica    |")
    print("\n----------------------------------------")
    
    #MENU PARA O USUÁRIO ESCOLHER A OPERAÇÃO QUE DESEJA REALIZAR
    while True:
        continua = str(input("Deseja realizar mais alguma operação?: Y ou N =>  "))
        if continua.upper() == "Y":
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("| 1. Criar conta corrente pessoa jurídica            |")
            print("| 2. Listar contas cadastradas                       |")
            print("| 3. Acessar dados dos clientes já cadastrados       |")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            opt=int(input("\nDigite a opção desejada:  "))
                     
            if opt == 1:#cadastra novas contas e salva no arquivo pessoafisica.txt
                    #LEITURA DO ARQUIVO COM NUMERO DAS CONTAS CORRENTES PJ
                    arq = open('contas_pj.txt', 'r')
                    contas =[]
                    for linha in arq:
                                    linha = linha.strip()
                                    contas.append(linha)
                    arq.close()
   
                    numero = random.randrange(0,len(contas)) #RANDOMIZA A CAPTURA DAS CONTAS
                    numConta = contas[numero] #VARIÁVEL QUE CAPTURA O NUMERO DA CONTA
                    numCnpj = str(input("\nDigite o CNPJ: Ex. 00.000.000/0000-00 =>  "))
                    razaoSocial = str(input("\nDigite a razão social da empresa: ")) #RAZÃO SOCIAL  
                    nomeTitular=str(input("\nDigite o nome do titular da conta: ")) #TITULAR DA CONTA
                    nCel = str(input("\nTelefone para contato: ")) #NÚMERO DE CONTATO DO CLIENTE
                    capitalSocial=int(input("\nInsira seu capital social inicial: R$ ")) #SALDO INICIAL
                      
                    file =open('pessoajuridica.txt','r')
                    flag=0
                    index=0
                    
                    for line in file:
                        index +=1

                        if numConta in line:
                            flag = 1
                            break
                 
                    if flag == 0: #VERIFICA SE A CONTA JÁ EXISTE. SE NÃO, CADASTRA NOVO CLIENTE
                            #print('A conta corrente de número ', numConta,' não existe. Prossiga com o cadastro')
                            date = datetime.today().strftime('%A, %B %d, %Y  %H:%M:%S') #CAPTURA DATA E HORA
                            c1=cria_conta(numConta,numCnpj,razaoSocial.upper(), nomeTitular.upper(),nCel,capitalSocial) #C1 CRIA UM NOVO CLIENTE
                            
                            conta_juridica=c1
                            arch=open('pessoajuridica.txt','a')
                            arch.write("\n"+str(conta_juridica)+"\n") #salva os dados do cliente pessoa física no arquivo pessoafisica.txt
                            arch.close()
                            
                            print("\nObrigado por escolher nosso banco!\n")
                            print("\nConta cadastrada em {}".format(date))
                            extrato(c1)     
                              
                    else: #SE CONTA EXISTE, SAI DESSE MENU
                            print('A conta corrente de número ', numConta,' já encontra-se cadastrada na linha',index)
                    file.close()  

                    
            elif opt == 2: #faz a leitura dos registros gravados no arquivo pessoafisica.txt
                    arch=open('pessoajuridica.txt','r') 
                    print("\n"+arch.read()+"\n") #LISTA OS CLIENTES CADASTRADOS
                    arch.close()


            elif opt == 3: #ACESSA O CADASTRO DENTRO DO ARQUIVO TXT E EFETUA O SAQUE OU DEPÓSITO
                    
                    search =str(input("\nFaça a busca pelo número da conta, pela razão social ou pelo nome do cliente => "))   
                    file =open('pessoajuridica.txt','r+') #procura dentro do arquivo a conta digitada
                    flag=0
                    index=0
                    for line in file:
                        index +=1
                        
                        if search.upper() in line:
                            dados = ast.literal_eval(line)
                            lista = line
                            lista = lista.split()
                            flag = 1
                            break

                    if flag == 0:
                            print('Conta Corrente/Cliente', search.upper(),'inexistente')
                           
                              
                    else:
                            
                            print('Cadastro encontrado na linha ',index)
                            #OPERAÇÕES
                            print("\n 1) Sacar \n 2) Depositar \n 3) Enviar notificação \n 4) Emitir extrato")
                            var = int(input("\nEscolha uma das opções acima => "))
                            
                            if var == 1: #SACAR
                                sq=int(input("Qual valor deseja sacar? => R$ "))
                                
                                oldSaldo = dados["Capital Social"] #variável oldSaldo recebe o valor que consta na conta corrente do cliente
                                resultado = oldSaldo - sq #variável resultado recebe o valor da operação feita entre o valor da conta corrente menos o valor do saque
                                
                                print(resultado)   #IMPRIMIU O NOVO SALDO, APÓS O SAQUE EFETUADO                            
                                
                                newLista = line.replace(str(oldSaldo),str(resultado).title()) 
                                
                                print("\nSaque realizado com sucesso!\n")
                                print("\nSenhor(a) {}, seu saldo atual é R$ {}\n".format(dados["Titular"],resultado))#imprime extrato resumido
                                
                                file=open("pessoajuridica.txt", "a")
                                
                                file.write("\n"+str(newLista))
                                file.close()
                            
                            elif var == 2: #DEPOSITAR
                                dp=int(input("Qual valor deseja depositar? => R$ "))
                                oldSaldo = dados["Capital Social"]#variável oldSaldo recebe o valor que consta na conta corrente do cliente
                                resultado = oldSaldo + dp #variável resultado recebe o valor da operação feita entre o valor da conta corrente menos o valor do saque
                                
                                print(resultado)   #IMPRIMIU O NOVO SALDO, APÓS O SAQUE EFETUADO                            
                                newLista = line.replace(str(oldSaldo),str(resultado).title())
                                print("\nDepósito  realizado com sucesso!\n")
                                print("\nSenhor(a) {}, seu saldo atual é R$ {}\n".format(dados["Titular"],resultado)) #imprime extrato resumido
                                file=open("pessoajuridica.txt", "a")
                                file.write("\n"+str(newLista))
                                file.close()

                            elif var == 3: #ENVIAR MENSAGEM PARA OS CLIENTES
                                celular= dados["Contato"]
                                msg=str(input("\nSua mensagem: "))
                                hora = int(input("\nHorário de envio => "))
                                minuto= int(input("\nMinuto exato => "))
                                #hour = datetime.today().strftime('%H:%M:%S')
                                #data = datetime.today().strftime('%B %d, %Y')
                                try:
                                    whatsapp.sendwhatmsg(celular, msg,hora,minuto)
                                    print("\nMensagem enviada com sucesso!\n")
                                    #print("\nMensagem enviada às {} do dia {}".format(hour,data))
                                except:
                                    print("\nDEU ERRADO!\n")

                            elif var == 4: #EMITIR EXTRATO
                                date = datetime.today().strftime('%A, %B %d, %Y  %H:%M:%S')
                                print("\n"+str(date)+"\n")
                                print("\nSeja bem-vindo Sr.(a) {}. Consulte seu extrato abaixo".format(dados["Titular"]))
                                extrato(dados)
                                
                                                            
                    file.close()   


            elif opt > 9 : #em caso de opção incorreta, retorna ao menu principal
                    print("\nOpção incorreta! Por favor, digite a opção correta!\n")

        elif continua.upper() == "N" : #CASO O USUÁRIO NÃO QUEIRA MAIS FAZER NADA, DIGITA "N" E SAI DO SISTEMA
            print("\nOBRIGADO POR USAR NOSSO BANCO! ATÉ LOGO\n")
            exit()
        elif continua.upper() != "Y" or "N":
            print("\nDigite uma opção correta!\n")