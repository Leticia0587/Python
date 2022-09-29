numero_um = int(input("Insira um valor inteiro: "))
numero_dois = int(input("Insira o segundo valor inteiro: "))

if numero_um == numero_dois:
    print("Esse número já foi utilizado!")
else:
    numero_tres = int(input("Insira o terceiro valor inteiro: "))
    lista = [numero_um, numero_dois, numero_tres]
    if numero_tres == numero_dois or numero_tres == numero_um:
        print("Esse número já foi utilizado!")
    else:
        resultado = max(lista)
        print(f"O maior valor é: {resultado}")
