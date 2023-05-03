p = int(input("Jogador 1 escolha se vai querer par (digite 1) ou ímpar (digite 0) "))
while True:
    j1 = int(input("Jogador 1 jogue seu número para disputa "))
    if j1 < 0:
        print("O número escolhido deve ser no mínimo igual a 1")
        continue
    elif j1 > 100:
        print("O número escolhido máximo deve ser no máximo de 100.")
        continue
    break
while True:
    j2 = int(input("Jogador 2 jogue seu número para disputa "))
    if j2 < 0:
        print("O número escolhido deve ser no mínimo igual a 1")
        continue
    elif j2 > 100:
        print("O número escolhido máximo deve ser no máximo de 100.")
        continue
    break
r = int(input("Jogador 1 você deseja roubar nesta jogada? 1-sim e 0-não "))
a = int(input("Jogador 2 você deseja acusar o jogador 1 de roubo nesta jogada? 1-sim e 0-não "))
s = j1 + j2
if r == 1 and a == 1:
    print ("Jogador 2 descobriu a tentativa de roubo do jogador 1. Parabéns jogador 2 você ganhou!!")
elif r == 1 and a == 0:
    print ("Jogador 2 não descobriu a tentativa de roubo do jogador 1. Parabéns jogador 1 você ganhou!!")
elif r == 0 and a == 1:
    print ("Jogador 2 você acusou injustamente o jogador 1 de roubo. Parabéns jogador 1 você ganhou")
else:
    if p == 1:
        if s%2:
            print ("Número ímpar! Parabéns Jogador 2 ganhou" )
        else:
            print ("Número par! Parabéns Jogador 1 ganhou")
    else:
        if s%2:
            print ("Número ímpar! Parabéns Jogador 1 você ganhou")
        else:
            print ("Número par! Parabéns jogador 2 você ganhou")

