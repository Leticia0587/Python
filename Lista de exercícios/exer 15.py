litros_vendidos = int(input("Quantos litros foram vendidos? "))
tipo_combustivel = str(input("Qual o tipo de combustível? A - álcool ou G - gasolina "))
litro_gasolina = 7.30
litro_alcool = 5.90

if tipo_combustivel == "A":
    valor_total = litros_vendidos * litro_alcool
    print(f"O valor total é de R${valor_total}")
else:
    valor_total = litros_vendidos * litro_gasolina
    print(f"O valor total é de R${valor_total}")
