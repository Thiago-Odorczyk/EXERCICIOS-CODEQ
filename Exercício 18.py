import math

print("Olá Amélia! Empolgada para mais um Natal? Vou te ajudar a fazer a decoração de sua nova árvore.")

while True:
    B = int(input("Para começar, Amélia, digite o valor de bolinhas que você já possui: "))
    if B <= 1 or B >= 103:
        print("O valor de bolinhas deve estar entre 1 e 102.")
        continue
    break

while True:
    G = int(input("Quantos galhos sua nova árvore possui? "))
    if G <= 100 or G >= 1000:
        print("O valor de G deve estar entre 101 e 999.")
        continue
    elif G % 2 != 0:
        G = math.floor(G/2)*2
        print("O número de galhos foi ajustado para", G)
    break

metade = G/2
if metade > B:
    quantfalta = metade - B
    print("Faltam", quantfalta, "bolinhas.")
else:
    print("Amélia tem todas as bolinhas necessárias.")
