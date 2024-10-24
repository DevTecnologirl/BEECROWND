N = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
quantidade_notas = {}
valor_restante = N
for nota in notas:
    quantidade = valor_restante // nota  
    quantidade_notas[nota] = quantidade
    valor_restante -= quantidade * nota  
print(N)
for nota in notas:
    print(f"{quantidade_notas[nota]} nota(s) de R$ {nota},00")
