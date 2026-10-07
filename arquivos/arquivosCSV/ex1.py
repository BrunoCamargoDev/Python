# criando arquivos .csv
import csv
from caminho import pessoasCaminho
pessoas = [
    ["nome", "idade", "cidade"],
    ["Layzy", "28", "São Paulo"],
    ["Leunardu", "74", "Novo Horizonte"],
    ["Karlus", "55", "Catanduva mesmo"]
]

with open(pessoasCaminho, "w", newline="", encoding="utf-8") as arquivo:
    registro = csv.writer(arquivo)
    registro.writerows(pessoas)
print("O arquivo pessoas.csv foi criado com sucesso!")