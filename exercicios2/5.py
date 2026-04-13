n1 = int(input("Num1: "))
n2 = int(input("Num2: "))
n3 = int(input("Num3: "))

lista = [n1, n2, n3]


if lista[0] > lista[1]:
    lista[0], lista[1] = lista[1], lista[0]
if lista[0] > lista[2]:
    lista[0], lista[2] = lista[2], lista[0]
if lista[1] > lista[2]:
    lista[1], lista[2] = lista[2], lista[1]

print("Crescente:", lista)
print("Decrescente:", lista[::-1])