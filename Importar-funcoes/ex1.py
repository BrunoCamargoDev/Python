import calculo as c
import time
# print(c.soma(20,10))
# print(c.subtracao(20,10))
# print(c.multiplicacao(20,10))
# print(c.divisao(20,10))

operacao = 1
while (operacao != 0):
    operacao = input("Qual operação? \n + soma \n - subtracao \n / divisao \n * multiplicação \n 0 fim da operacao \n Qual?: ")

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        print(c.soma(n1, n2))
        time.sleep(3)
    elif operacao == "-":
        print(c.subtracao(n1,n2))
        time.sleep(3)
    elif operacao == "/":
        print(c.divisao(n1, n2))
        time.sleep(3)
    elif operacao == "*":
        print(c.multiplicacao(n1,n2))
        time.sleep(3)
    else:
        print("Operação inválida")
        

