distancia = float(input("Qual a distância da sua viajem: "))
print("Você esta presta a começar uma viajem de {}Km".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("E o preço da sua passagem será de R${:.2f}".format (preco))
