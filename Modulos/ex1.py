# Modulos
# Estao = importa
# NAO ESTAO = Instala com gerenciador de deps. pip

import math
numero = 16
raiz_quadrada = math.sqrt(numero)

print(f"A raiz quadrada de {numero} é {raiz_quadrada}")

from math import pi
print(f"O valor do pi é {pi}")

# biblioteca toa = import
# parcial, especificas = from x import y,z...

import math as m
print(f"o cosseno de 0 é {m.cos(0)}")

# Geralmente os imports ficam no topo do arquivo pra melhor visualizar

import random
dado = random.randint(1, 6)

print(f"O número é: {dado}")

# datas = datetime
from datetime import datetime
agora = datetime.now()
print(agora)

# Sistema operacional = os
import os

arquivos = os.listdir('.')

# . => diretorio (pasta) atual

print(f"Os arquivos desta pasta são: {arquivos}")


# ------------------------------
import sys

print(f"A versão do python é {sys.version}")