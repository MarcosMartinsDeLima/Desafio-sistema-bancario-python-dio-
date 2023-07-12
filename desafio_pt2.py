def menu():
    
    menu = """
    [1]-Depositar
    [2]-Sacar
    [3]-Extrato
    [4]-Criar usuario
    [5]-Criar conta
    [6]-Sair

    informe a opçao escolhida: """

    return int(input(menu))

def depositar(saldo,valor,extrato,/):
    if valor > 0 :
        saldo += valor
        extrato += f"Deposito de R${valor:.2f}\n"
        print("Deposito realizado com sucesso")
    else:
        print("Valor invalido") 
    return saldo,extrato   

def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor>saldo
    excedeu_limite= valor>limite
    excedeu_numeros_de_saque= numero_saques>limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente")
        
    elif excedeu_limite:
         print("Limite excedido")
        
    elif excedeu_numeros_de_saque:
         print("Numeros de saques excedidos")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de R${valor:.2f}\n"
        numero_saques+=1
        print("Saque realizado com sucesso!")
    else:
        print("valor invalido")

    return saldo,extrato

def extratos(saldo,/,*,extrato):
    print("\n*****************Extrato*****************") 
    print("Não foram realizadas transações" if not extrato else extrato)  
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n*****************************************")           

def criar_usuario(usuarios):
    cpf = input("informe o cpf(somente número): ")
    usuario= filtrar_usuarios(cpf,usuarios) 
    if usuario:
        print("\nJá existe um usuario com esse cpf")
        return
    else:
        nome=input("Informe seu nome completo: ")
        data_nascimento=input("Informe sua data de nascimento(dd-mm-aaaa): ")
        endereco=input("Informe seu endereço(logradouro,n*-bairro-cidade/sigla estado):")
        usuarios.append({"nome":nome,"data_de_nascimento":data_nascimento,"cpf":cpf,"endereço":endereco})
        print("Parabens! Usuario criado com sucesso")

def filtrar_usuarios(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input("informe o cpf(somente número): ")
    usuario= filtrar_usuarios(cpf,usuarios)

    if usuario:
        print("conta criada com sucesso")
        return {"agencia":agencia,"numero_da-conta":numero_conta,"usuario":usuario} 
    else:
        print("usuario nao encontrado")
    
def listar_conta(contas):
    for conta in contas:
        texto= f"""\n agencia:{conta['agencia']}
        C/C{conta['numero_conta']}
        titular{conta['nome']} """
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA='0001'
    usuarios=[]
    contas=[]
    numero_conta=0
    while True:
        
        opcao = menu()

        if opcao == 1:
            valor = float(input("\nInforme o valor:"))
            saldo,extrato = depositar(saldo,valor,extrato)  
   
        elif opcao == 2:
            valor = float(input("Digite o valor:"))
            saldo,extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,)
        
        elif opcao ==3:
            extratos(saldo,extrato=extrato)
        
        elif opcao==4:
            criar_usuario(usuarios) 
        elif opcao==5:
            conta=criar_conta(AGENCIA,numero_conta,usuarios)
            if conta:
                contas.append(conta)
                numero_conta+=1  
        
        elif opcao ==6:
            break
 
        else:
             print("Opção inválida")

main()           


