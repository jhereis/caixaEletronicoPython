#second bank test in pyython 

saldoAtual = 100
senha = int(1111)

Saldo = 1
Extrato = 2
Saque = 3
Deposito = 4
Transferencia = 5

nome = str(input("Digite seu nome \n"))

digitarSenha = int(input("Digite a sua senha de quatro Digitos: \n"))
if senha == digitarSenha:
    print("Bem vindo " + nome + "!")
else:
    print("Senha Invalida!")


def sq():
    print("seu saldo é de: " + saldoAtual +)
sq()]


opcoes = int(input("Escolha uma opção: \n 1 = Saldo \n 2 = Extrato \n 3 = Saque \n 4 = Deposito \n 5 = Transferencia\n"))
if opcoes == Saldo:
    print("Seu saldo atual é de:", saldoAtual , "reais.")
elif opcoes == Extrato:
    print("Seu extrato: \n Starbugs - 200,00 \n Shein - 100,56")
#elif opcoes == Saque:
 #   pri
else:
    print("Opção Invalida!")
