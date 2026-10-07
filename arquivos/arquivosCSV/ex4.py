import csv
from caminho import alunosCaminho
alunos = [
    ["Leyzy",75,"ADS"],
    ["Liunerdu",48,"Engenharia"],
    ["Kerlus",97,"Matemática"]
]

with open(alunosCaminho, "w", newline="", encoding="utf-8") as arquivo:
    registro = csv.writer(arquivo)
    registro.writerows(alunos)
print("Arquivo alunos.csv foi criado com sucesso!")