numero_conta_cliente = int(input("Qual o número da sua conta? "))
saldo = int(input("Qual o seu saldo? "))
debito = int(input("Qual o seu débito? "))
credito = int(input("Qual o seu crédito? "))
saldo_atual = saldo - debito + credito
print(f"Seu saldo atual é de R${saldo_atual}")

resultado = "Saldo Positivo" if saldo_atual >= 0 else "Saldo Negativo"
print(resultado)
