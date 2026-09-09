# tupla - cria (1, 2, 3) e não pode ser alterada
cores = ("azul", "verde", "vermelho")
print(cores)
print(cores[1])

for cor in cores:
    print("Cor: ", cor)

print(len(cores))

if "vermelho" in cores:
    print("Achei")

# cores.append("teste")

