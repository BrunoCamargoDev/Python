# Dicionários
# São estruturas de dados bastante utilizadas em python, que armazena coleções utilizando o conceito chave-valor

# sintaxe:
# dicionario = {chave1: valor1, chave2: valor2, chave3: valor3, ...} declaração com chaves

aluno = {"nome": "Frederico", "nota": 3.5, }
print(aluno)
print(aluno["nome"]) # Dicionário não tem indice
print(aluno["nota"]) # Dicionário não tem indice

aluno["nota"] = 2.5 # Alterando o valor da chave nota
print(aluno)
aluno["disciplina"] = "LIP"
print(aluno)


banco_de_dados = {
    'cli_001':{"nome": "Alice", "idade": 25, "cidade": "São Paulo"},
    'cli_002':{"nome": "Bob", "idade": 30, "cidade": "Rio de Janeiro"},
    'cli_003':{"nome": "Charlie", "idade": 22, "cidade": "Belo Horizonte"}
}

print(banco_de_dados)

print(banco_de_dados['cli_002']['nome'])

banco_de_dados["cli_001"]["idade"] = 95
print(banco_de_dados["cli_001"])

# percorrer dicionário
for chave in aluno:
    print(chave)

# acessar valores do dicionario
for valor in aluno.values():
    print(valor)

# Acessar chave e valor
for chave, valor in aluno.items():
    print(chave, valor)