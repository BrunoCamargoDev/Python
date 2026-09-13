#tuplas são estruturas que utilizamos para armazenar coleções ordenadas de elementos, elas são imutáveis (valores não mudam depois de criada)

#sintaxe: tupla = (elemento1, elemento2, elemento3, ...) declaração com parenteses

corolla = (2025, "chumbo")

#Coordenadas geográficas
ifsp_catanduva = (-21.14713, -48.94542)

# Relação de descontos:
descontos = (10,15,30)

# Conexão de banco de dados
connection = ("localhost", "root", "123456")

print(f"Desconto: {descontos[0]}%")
print(f"Desconto: {descontos[0:2]}%")
# descontos[2] = 8
# print(f"Desconto: {descontos[2]}%")

x, y, z = descontos
print(x)
print(y)
print(z)

n = (5,) # apenas um elemento, precisa da vírgula para ser reconhecido como tupla, caso contrário será reconhecido como inteiro
print(type(n))

#percorrer
for item in descontos:
    print(item)
