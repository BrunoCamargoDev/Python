def imc(p, a):
    res = p / (a ** 2)

    if res < 18.5:
        print(f"Abaixo do peso! IMC: {res:.2f}")
    elif res < 24.9:
        print(f"Peso normal! IMC: {res:.2f}")
    elif res < 29.9:
        print(f"Sobrepeso! IMC: {res:.2f}")
    else:
        print(f"Obeso! IMC: {res:.2f}")

    return res


p = float(input("Digite seu peso: "))
a = float(input("Digite sua altura: "))

imc(p, a)