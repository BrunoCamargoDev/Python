#array []
# tupla ()
# dicionarios {}, como chaves e valores
# set, sem chaves e valores, somente itens

aluno = {
    "nome": "Bruno",
    "profissao": "Dev",
    "idade": 19
}

# "nome_da_chave": "valor", 12, []

print(aluno["nome"])

print(f"O nome dele é {aluno["nome"]} e sua profissão é {aluno["profissao"]}")

aluno["nota"] = 15
aluno["profissao"] = "Engenheiro"

print(aluno)

# remoção
del aluno["profissao"]

print(aluno)

# conjunto (set)
lista = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7]

lista_unica = set(lista)

print(lista)

print(lista_unica)

lista_unica.add(8)
lista_unica.add(6)

lista_unica.remove(2)

print(lista_unica)

# uniao de conjuntos
lista_b = {1, 3, 5}

uniao = lista_unica.union(lista_b)

print(uniao)

# interseção

intersecao = lista_unica.intersection(lista_b)

print(intersecao)

# diferença

diferenca = lista_unica.difference(lista_b)

print(diferenca)


# Exercicio

# criar função que vai adicionar a nota da prova A a um aluno

def adicionar_nota(aluno):
    aluno["prova_a"] = int(input("Digite a nota A:"))

aluno_teste = {"Nome": "joão"}

print(aluno_teste)

# verificar as palavras unicas de uma frase (set)

frase = input("Digite uma frase:")

palavras = frase.split()

print(palavras)

palavras_unicas = set(palavras)

print((palavras_unicas))