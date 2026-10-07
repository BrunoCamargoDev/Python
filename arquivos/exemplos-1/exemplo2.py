alunos = ["Laysy", "Heytor Jasco", "Karlus", "Fabryccio"]
with open("alunos.txt", "w") as a:
    a.write("Lista de alunos reprovados\n")
    for item in alunos:
        a.write("aluno(a): " + item + "\n")
    a.writelines(alunos)