carros = ["Fiat", "Ford", "BMW"]

print(carros[0])
print(carros[1])
carros.append("Chevrolet")
print(carros[3])
carros[0] = "Volkswagen"

print(carros[0])

carros.remove("Ford")

# Verificação de quantos itens 
print(len(carros))