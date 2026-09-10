# Maneira de reutilização de codigo
# Sem parametros
def saudacao():
    print("Olá, seja bem vindo!")


saudacao()

nome = input("Digite seu nome: ")
# Com parametros
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Seja bem vindo!")

saudacao_personalizada(nome)

# -------------------
def apresentacao(nome, idade, profissao):
    print(f"Dados da pessoa, nome: {nome}, idade: {idade}, profissão: {profissao}")


apresentacao("João", 30, "Engenheiro")

# return => instrução que retorna o valor pro programa

def soma(a, b):
    resultado = a + b
    return resultado
soma(5, 5)

x = 10

soma_x = x + soma(5, 5)

resultado_soma = soma(1, 99)

soma_y = 10 + resultado_soma

print(soma_y)
    
# Criar função que converte fahrenheit para celsius
def converter():
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Exemplo de uso
temperatura_celsius = converter()
print(f"A temperatura em Celsius é: {temperatura_celsius:.2f}°C")