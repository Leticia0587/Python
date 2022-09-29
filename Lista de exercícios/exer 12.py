salario_fixo = float(input("Qual o valor do seu salário fixo? "))
valor_vendas = float(input("Qual o valor das vendas efetuadas esse mês? "))
salario_total = 0

if valor_vendas < 20000:
    salario_total = salario_fixo + (valor_vendas * 0.03)
    print(f"R${salario_total}")
else:
    salario_total = salario_fixo + (valor_vendas * 0.03) + 600
    print("Parabéns! Você atingiu a meta e recebeu um bônus de R$600,00")
    print(f"R${salario_total}")
