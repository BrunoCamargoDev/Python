aluno = input("Digite o nome do aluno: ")
nota1 = (input("Digite a primeira nota: "))
nota2 = (input("Digite a segunda nota: "))
media = (float(nota1) + float(nota2)) / 2

with open("nota.txt", "w") as a:
    a.write("aluno: " + aluno + "\n")
    a.write("nota1: " + nota1 + "\n")
    a.write("nota2: " + nota2 + "\n")
    a.write("média: " + str(media) + "\n")