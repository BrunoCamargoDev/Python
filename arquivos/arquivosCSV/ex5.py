# lendo o arquivo e incluindo cabeçalho
import csv
from caminho import alunosCaminho
with open(alunosCaminho, "r", encoding="utf-8") as arquivo:
    registro = csv.DictReader(arquivo)

    for linha in registro:
        print(linha)