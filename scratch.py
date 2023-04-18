# first try in bank test in python    

saldoAtual = float(100)
nome = str(input("Digite seu nome "))
senha = int(111111)

digitarSenha = int(input("Digite sua senha -> "))

def inicioCaixa():
    input("Escolha uma opção: \n 1 = Saldo \n 2 = Extrato \n 3 = Saque \n 4 = Deposito \n 5 = Transferencia ")

inicioCaixa()


if digitarSenha == senha:
    print("Bem vindo ao seu banco " + nome + "! \n ")
else:
    print("Senha errada! \n tente novamente. ")


Saldo = int((1))
Extrato = int((2))
Saque = int((3))
Deposito = int((4))
Transferencia = int((5))

#opçoes dentro do caixa eletronico

opcao = (1,2,3,4,5)



 switch(opcao):
    if opcao == 1:
        return "Seu saldo atual é de " , OpSaldo() , "."
    elif opcao == 2:
        return ""
    elif opcao == 3:
        return ""
    elif opcao == 4:
        return ""
    elif opcao == 5:
        return ""
    else:
        return "Opção invalida!"

print(switch(opcao))

#Op -> opçao

def OpSaldo():
    print(saldoAtual)

OpSaldo()

def OpExtrato():
    print("Seu extrato: \n 01/02 = 12,00 \n Debito = 250,00 \n Debito = 10,12")

OpExtrato()

def OpSaque():
    if saldoAtual <= 0:
        print("Você não possui saldo suficiente, seu saldo atual é de: " + saldo + " por favor informe uma quantidade valida ou faça um depósito")

