a = int(input("Digite o número de dias "))
anos = a/365
meses = (a % 365)/30
dias = (a % 365) % 30
print(int(anos), "ano(s)")
print(int(meses), "mes(es)")
print(int(dias), "dia(s)")
