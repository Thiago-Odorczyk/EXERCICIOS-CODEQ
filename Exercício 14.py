while True:
    N = int(input("Digite o número de jogadores de seu time "))
    if N < 1:
        print("O número de jogadores deve ser maior ou igual a 1")
        continue
    elif N > 105:
        print("O número máximo de jogadores no time dever de 105.")
        continue
    break
votos = []
while len(votos) < N:
    voto = int(input("Digite seu voto (1) para impeachment e (0) para arquivamento: "))
    votos.append(voto)
impeachment = votos.count(1)
arquivamento = votos.count(0)
totaldevotos = len(votos)
if impeachment >= (2/3)*totaldevotos:
    print ("Impeachment")
else:
    print ("Acusação Arquivada")
