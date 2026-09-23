# Tratamento de erros e excessões
# Criar programas, que precisam estar a prova de falhas

# Try - tentando fazer algo
# Except - para tratar o erro
# Else - para uma condição positiva
# finaly - roda sempre, independente da situação

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()

except FileNotFoundError:
    print("Erro: O arquivo não existe")

else:
    print("Arquivo lido!")
    print(conteudo)

finally:
    print("Operação finalizada")
    if 'arquivo' in locals():
        # liberar memória
        arquivo.close()
        print("Arquivo fechado!")

try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
except ValueError:
    print("Entrada inválida, tente novamente")
except ZeroDivisionError:
    print("Divisão por 0!")
else:
    print("O resultado é: ", resultado)
finally:
    print("Operação concluída!")


try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
except (ValueError, ZeroDivisionError) as error:
    print("Erro: ", error)
else:
    print("O resultado é: ", resultado)
finally:
    print("Operação concluída!")