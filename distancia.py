tempo, velocidade = map(int, input().split())
distancia = tempo * velocidade
litros = distancia / 12
print(f"{litros:.3f}")
