# Cadastrando as notas dos alunos 
import csv
from caminho import notasCaminho

aluno = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

with open(notasCaminho, "a", newline="", encoding="utf-8") as arquivo:
    registro = csv.writer(arquivo)
    registro.writerow([aluno, nota])