primeiro_homem = int(input("Homem - Qual a sua idade? "))
segundo_homem = int(input("Homem - Qual a sua idade? "))

if primeiro_homem == segundo_homem:
    print("As idades devem ser diferentes entre si")
else:
    primeira_mulher = int(input("Mulher - Qual a sua idade? "))
    segunda_mulher = int(input("Mulher - Qual a sua idade? "))
    if primeira_mulher == segunda_mulher:
        print("As idades devem ser diferentes entre si")
    else:
        homem_mais_velho = primeiro_homem if primeiro_homem > segundo_homem else segundo_homem
        homem_mais_novo = primeiro_homem if primeiro_homem < segundo_homem else segundo_homem

        mulher_mais_velha = primeira_mulher if primeira_mulher > primeira_mulher else segunda_mulher
        mulher_mais_nova = primeira_mulher if primeira_mulher < primeira_mulher else segunda_mulher
        print(mulher_mais_nova)
        soma = homem_mais_velho + mulher_mais_nova
        produto = homem_mais_novo * mulher_mais_velha

        print(f"Soma do homem mais velho com a mulher mais nova é igual a: {soma}")
        print(f"Produto do homem mais novo com a mulher mais velha é igual a: {produto}")
