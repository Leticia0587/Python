quantidade_atual = int(input("Qual a quantidade atual em estoque do produto? "))
quantiade_maxima = int(input("Qual a quantidade máxima em estoque do produto? "))
quantidade_minima = int(input("Qual a quantidade mínima em estoque do produto? "))
quantiade_media = (quantiade_maxima + quantidade_minima) / 2
soma_quantidade = quantidade_atual >= quantiade_media

resultado = "Não efetuar compra" if soma_quantidade else "Efetuar compra"
print(resultado)
