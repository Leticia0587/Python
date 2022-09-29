primeiro_time = str(input("Digite o primeiro time de futebol: "))
segundo_time = str(input("Digite o segundo time de futebol: "))

gols_primeiro_time = int(input(f"Quantos gols o {primeiro_time} fez? "))
gols_segundo_time = int(input(f"Quantos gols o {segundo_time} fez? "))

if gols_primeiro_time == gols_segundo_time:
    print(f"""
    O jogo terminou EMPATADO com o placar de: 
    {primeiro_time} {gols_primeiro_time} x {segundo_time} {gols_segundo_time}
    """)
else:
    resultado = primeiro_time if gols_primeiro_time > gols_segundo_time else segundo_time
    print(f"O vencedor foi o {resultado} por {gols_primeiro_time} x {gols_segundo_time}")
