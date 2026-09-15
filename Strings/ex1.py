# Manipulação de Strings
mensagem = "Isso é texto"

print(mensagem)

# Concatenação
primeiro_nome = "Bruno"
sobrenome = "Camargo"

print(primeiro_nome + ' ' + sobrenome)

nome_completo = primeiro_nome + " " + sobrenome

print(f"Olá, {nome_completo}")

# repetir

decoracao = "-" * 10

print(decoracao)

print(decoracao + " menu " + decoracao)

# indexação
texto = "Python"

print(texto[3])

#Fatiamento - slicing
frase = "Aprender python é top"
print(frase[9:])

print(frase[9:16])
# Fatiamento começa da letra indicada no indice: termina -1 do indice final

# Comprimento de uma string
print(len(frase))

# Outra maneira de formatação

cidade = "Floripa"

msg = "Eu moro em {}".format(cidade)

print(msg)

# Mudança de case - string
texto = "Programação "

print(texto.upper()) # Maiusculo
print(texto.lower()) # minusculo
print(texto.title()) # Alterando as palavras

# limpeza de espaços em branco

msg_espaco = "       Eu quero "
print(msg_espaco)
print(msg_espaco.strip())

# Substituiaco

frase = "Eu gosto de JavaScript"

print(frase)

nova_frase = frase.replace("JavaScript", "Python")

print(nova_frase)

# Encontrar parte de um texto
texto = "Onde está minha chave?"

posicao = texto.find("chave")

print(f"A posição é {posicao}")

posicao2 = texto.find("key")

print(f"A posição é {posicao2}")

# valor de -1 fazer a logica do sistema

if posicao2 == -1:
    print("Palavra não encontrada")