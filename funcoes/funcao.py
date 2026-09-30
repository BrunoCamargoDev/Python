# funcao.py

def ler(frase):
    contador = 0
    for x in frase:
        if x != " ":
            contador += 1
            
    return contador

# Possibilidade mais curta
def count_carac(frase):
    return len(frase.replace(" ", ""))

# Faça uma função que inverta a frase digitada
def inverter(frase):
    frase_invertida = ""
    for x in frase:
        frase_invertida = x + frase_invertida
    return frase_invertida

# Testando a função:
texto = input("Digite um texto: ")
print(texto)
print(inverter(texto))
# print(frase[::-1])

# fazer uma função que conte as vogais

def vogais(frase):
    vogal = 0
    vogais = "AEIOU"
    for x in frase.upper():
        if x in vogais:
            vogal += 1
    return vogal

frase = input("Digite uma frase: ")
print(vogais(frase))


# Faça um programa que receba um número (>2) e apresente a quantidade digitada da sequencia de fibonacci

def fibonacci(n):
    sequencia = []
    a = 0
    b = 1
    for x in range(n):
        sequencia.append(a)
        c = a
        a = b
        b = c + b
    return sequencia

numero = int(input("digite um numero maior que 2:"))
print(fibonacci(numero))


