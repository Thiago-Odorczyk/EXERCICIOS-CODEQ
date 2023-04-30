while True:
    P = int(input("Digite a altura do pulo do sapo "))
    if P < 1:
       print("A altura do pulo do sapo deve ser no mínimo 1")
       continue
    elif P > 5:
        print("A altura do pulo do sapo deve ser no máximo 5")
        continue
    break
while True:
    N = int(input("Digite o número de canos "))
    if N < 2:
       print("A altura do pulo do sapo deve ser no mínimo 1")
       continue
    elif N > 100:
        print("A altura do pulo do sapo deve ser no máximo 5")
        continue
    break
AlturasN = []
continuar = True

while continuar:
    altura = input("Digite a altura do cano (ou digite 'fim' para encerrar): ")
    
    if altura == 'fim':
        continuar = False
    else:
        altura = int(altura)
        while altura > 10:
            print("A altura do cano deve ser no máximo 10.")
            altura = int(input("Digite a altura do cano (ou digite 'fim' para encerrar): "))
        
        AlturasN.append(altura)
posicao = 0
altura_atual = AlturasN[posicao]
while posicao < len(AlturasN) - 1:
    if abs(AlturasN[posicao + 1] - altura_atual) <= P:
        posicao += 1
        altura_atual = AlturasN[posicao]
    else:
        print("Game Over")
        break

if posicao == len(AlturasN) - 1:
    print("You Win!!!!!")
