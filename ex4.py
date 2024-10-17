codigo_peca1, numero_pecas1, valor_unitario1 = input().split()
codigo_peca1 = int(codigo_peca1)
numero_pecas1 = int(numero_pecas1)
valor_unitario1 = float(valor_unitario1)

codigo_peca2, numero_pecas2, valor_unitario2 = input().split()
codigo_peca2 = int(codigo_peca2)
numero_pecas2 = int(numero_pecas2)
valor_unitario2 = float(valor_unitario2)

total = (numero_pecas1 * valor_unitario1) + (numero_pecas2 * valor_unitario2)

print(f"VALOR A PAGAR: R$ {total:.2f}")
