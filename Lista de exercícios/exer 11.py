horas_trabalhadas = int(input("Quantas horas você trabalhou essa semana? "))
salario_por_hora = float(input("Qual o seu salário por hora trabalhada? "))
salario_semanal = 0

if horas_trabalhadas <= 40:
    salario_semanal = horas_trabalhadas * salario_por_hora
    print(f"Seu pagamento essa semana foi de R${salario_semanal}")
else:
    salario_semanal = horas_trabalhadas * (salario_por_hora * 1.5)
    print(f"Seu pagamento essa semana foi de R${salario_semanal}")
