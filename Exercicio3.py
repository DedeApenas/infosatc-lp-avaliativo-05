for x in range(0,4): 
    nomeSobrenome = input("Digite seu Nome e Sobrenome:")
    while (len(nomeSobrenome)<3): 
        print("Nome e Sobrenome invalidos(minimo de 3 caracteres)")
        nomeSobrenome = input("Digite seu Nome e Sobrenome:")
    cpf = input("Digite seu CPF:")
    endereco = input("Digite seu Endereço: ")
    celular = input("Digite seu numero de Celular:")
    senha = input("Digite sua Senha(No minimo 5 Letras 1 Caracter especial e 1 Numero):")
    while (len(senha)<5) or(senha.isalnum() == True or senha.isalpha() == True): 
            senha = input("Senha invalida")
    email = input("Digite seu E-mail:")
    for x in email: 
        if ("@" in email): 
            break
    else:
        print("Email invalido(formato correto: email@email)")
    dados = {"Nome e Sobrenome:{}".format(nomeSobrenome), "CPF:{}".format(cpf), "Endereço:{}".format(endereco), "Senha:{}".format(senha), "Email:{}".format(email)}
    print(dados)
    total=0
    total=total+1
    if(total==1):
        conta={}
        conta=dados.copy()
        print("Sua conta foi definida com o nome:",nomeSobrenome)
    saldoTotal=0
    depositar=0
    sacar=0 

    def operacoes():
            saldoTotal=0      
            for x in range(0,4): 
                operacoes = int(input("Operações:\n1-Depositar\n2-Sacar\n3-Conferir Saldo\n4-Transferir\n5-Encerrar Conta\nDigite o numero correspondente:"))
                if (operacoes == 1): 
                    depositar = float(input("Quanto você deseja depositar?:"))
                    saldoTotal = saldoTotal + depositar
                    print("O seu saldo é de:",saldoTotal)
                    while(depositar < 0): 
                        depositar = float(input("Erro no deposito(Deposite apenas numeros positivos)"))
                        if(depositar >= 0): 
                            saldoTotal = saldoTotal + depositar
                            print("O seu saldo é de:",saldoTotal)
                        else:
                            pass  
                elif(operacoes == 2): 
                        sacar = float(input("Qual será o valor de saque?:"))
                        saldoTotal = saldoTotal - sacar
                        while (sacar > saldoTotal): 
                         sacar = float(input("Saldo insuficiente para o saque"))
                        saldoTotal = saldoTotal - sacar
                elif(operacoes == 3): 
                        print("Seu saldo é de:",saldoTotal)
                elif(operacoes == 4): 
                        transferir = float(input("Qual o valor para a transferencia?:"))
                        saldoTotal = saldoTotal - transferir
                elif(operacoes == 5): 
                        encerrar = input("Encerrar conta?")
                        if (encerrar == "Sim"): 
                            print("Conta Encerrada")    
                            break
                
    operacoes()

  