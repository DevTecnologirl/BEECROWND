N = int(input())
horas = N // 3600
minutos = (N % 3600) // 60
segundos = N % 60
print(f"{horas}:{minutos}:{segundos}")
