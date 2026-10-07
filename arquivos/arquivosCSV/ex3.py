#ler o arquivo pessoas.csv e gerar um dict
import csv

with open(r"C:/Users/Bruno/OneDrive/Documentos/ADS/2° periodo/Douglas (antes Dani)/aula9/csv/pessoas.csv", "r", encoding="utf-8") as arquivo:
    registro = csv.DictReader(arquivo)

    for linha in registro:
        print(linha["nome"], linha["idade"], linha["cidade"])