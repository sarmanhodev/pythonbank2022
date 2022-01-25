import pf


print("\n************************************")
print("|        SisBank of Python         |")
print("************************************\n")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("| 1. Conta Corrente Pessoa Física   |")
print("| 2. Conta Corrente Pessoa Jurídica |")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    


opt=int(input("\nSelecione a opção desejada? "))

if opt == 1:
    pf.pessoa_fisica() #Conta Corrente Pessoa Física

elif opt == 2:
    pf.pessoa_juridica() #Conta Corrente Pessoa Jurídica

    

    #MENU PRINCIPAL