while True:
    C = int(input("Digite o número de competidores "))
    if C < 0:
        print("O número de competidores deve ser no mínimo igual a 1")
        continue
    elif C > 1000:
        print("O número máximo de competidores dever ser no máximo de 1000.")
        continue
    break
while True:
    P = int(input("Digite o número de folhas de papel especial compradas pela Diretora "))
    if P < 0:
        print("O número de folhas deve ser no mínimo de 1")
        continue
    elif P > 1000:
        print("O número máximo de folhas é de 1000")
        continue
    break
while True:
    F = int(input("Digite a quantidade de folhas de papel especial que cada competidor deve receber "))
    if F < 1:
        print("O número de folhas deve ser no mínimo de 1")
        continue
    elif F > 105:
        print(" número máximo de folhas é de 1000")
        continue
    break
if P/F >= C:
   print ("O número de folhas compradas são suficientes")
else:
    print ("O número de folhas compradas não foram suficientes")
