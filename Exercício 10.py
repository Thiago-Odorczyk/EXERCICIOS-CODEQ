QuantJogos = 0
Vitgremio = 0
Vitinter = 0
empates = 0
novo = 1
while novo ==1:
    golsGremio = int(input("Digite quantos gols fez o grêmio "))
    golsInter = int(input("Digite quantos gols fez o inter "))
    QuantJogos +=1
    if golsGremio > golsInter: Vitgremio +=1
    if golsInter > golsGremio: Vitinter +=1
    if golsInter == golsGremio: empates +=1
    novo = int(input("Novo grenal (1-sim 2-nao) "))
else: 
    print("Quantidade de grenais =",QuantJogos)
    print("Inter venceu", Vitinter,"jogos")
    print("Grêmio venceu", Vitgremio,"jogos")
    print("Jogos em empate =", empates)
if Vitgremio==Vitinter:
   print ("não houve quem venceu mais")
elif Vitgremio>Vitinter:
     print("Grêmio venceu mais jogos")
else:
    print("Inter venceu mais jogos")
