A = float(input("Digite o valor de A "))
B = float(input("Digite o valor de B "))
C = float(input("Digite o valor de C "))
delta = (B**2)-(4*A*C)
if delta >= 0 and A != 0:
    R1 = ((-B)+(delta**0.5))/(2*A)
    R2 = ((-B)-(delta**0.5))/(2*A)
    print("R1 =",round(R1, 5))
    print("R2 =",round(R2, 5))
else:
    print("impossível calcular")
