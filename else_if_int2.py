numero_int = input("Digite um número inteiro: ")

if not numero_int.isdigit():
    print("Isso não é um número inteiro")
else:
    numero_int = int(numero_int)

    if not numero_int % 2 == 0:
        print(numero_int, "é ímpar")
    else:
        print(numero_int,"é par")