# Cadastrando as notas dos alunos 
import csv
from caminho import notasCaminho

aluno = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

with open(notasCaminho, "a", newline="", encoding="utf-8") as arquivo:
    registro = csv.writer(arquivo)
    registro.writerow([aluno, nota])
print("Registro realizado com sucesso!")

with open(notasCaminho, "r", encoding="utf-8") as arquivo:
    registro = csv.reader(arquivo)
    for linha in registro:
        print(linha)