# Strings

# Declarando string com aspas dupla
exemplo1 = "Bruno"

# Aspas simples
exemplo2 = 'Bruno'

# 3 aspas simples
exemplo3 = '''Bruno Henrique Camargo'''

# Acessando os elementos
print(exemplo1[2])

# Tamanho da string
print(len(exemplo1))
print(len(exemplo2))
print(len(exemplo3))

# Percorrer uma string pelo elemento
for elemento in exemplo1:
    print(elemento)

# Percorrer uma string pelo indice
for indice in range(len(exemplo3)):
    print(indice, exemplo3[indice])

# Fatiamento de string
print(exemplo3[2:16])

# Fatiamento de string com parametro passo
print(exemplo3[2:18:2])

# Formatando uma string com outras variaveis
reajuste = 10
inflacao = 6.5
frase = "O reajuste foi de %d %% e a inflação foi de %.2f %%." %(reajuste, inflacao)
print(frase)

# Desabilitando comandos do python
print("Instituto \\ Federal")
print("Instituto %% Federal")
print(r"Instituto \\ Federal") # Função raw - desabilita função de comando dentro de string

# Manipulando as stings
exemplo5 = exemplo1 + " " + exemplo2
print(exemplo5)

# Comparando strings
aluno1 = "Josefina"
aluno2 = "Felisberto"

# == igualmente igual
if (aluno1 == aluno2):
    print("Nomes iguais")
else:
    print("Nomes diferentes")

# > ou < - a comparação é feita com base na tabela ASCII
if (aluno1 < aluno2):
    print(aluno1 + " Vem antes que o " + aluno2)
else:
    print(aluno2 + " vem antes que o " + aluno1)

# procurando uma string em outra
if (aluno2 in exemplo3):
    print("A string está dentro da outra.")
else:
    print("A string não está dentro da outra.")

# Métodos de manipulação
# Passa pra minúsculo
print(exemplo3.lower())

# Passa pra maiúsculo
print(exemplo3.upper())

# Remove os espaços, nesse caso começo e final
msg = "    não terminei de escrever ainda   "
print(msg.strip())

#Substitui elemento x por elemento y, no caso espaço por "-"
print(msg.replace(" ", "-"))

# Cria lista separando os elementos da string quando encontrar um espaço
print(msg.split())

# Cria lista de acordo com o parametro
print(msg.split("e"))
