''' Crie um dicionario chamado aluno(nome, idade, curso, nota) depois percorra e exiba as informações:
nome: fulano
idade: 98
curso: ADS
nota: 10
'''

aluno = {"nome": "Bruno", "idade": 19, "curso": "ADS", "nota": 8}

for c, v in aluno.items():
    print(c, v)
