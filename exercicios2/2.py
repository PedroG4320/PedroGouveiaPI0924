n1 = int(input("Num1: "))
n2 = int(input("Num2: "))
n3 = int(input("Num3: "))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print("Maior:", maior)
print("Menor:", menor)