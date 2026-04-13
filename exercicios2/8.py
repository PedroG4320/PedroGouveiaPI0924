soma = 0
notas = []

for i in range(10):
    n = float(input(f"Nota {i+1}: "))
    notas.append(n)
    soma += n

media = soma / 10

contador = 0
for n in notas:
    if n >= media:
        contador += 1

print("Média:", media)
print("Notas >= média:", contador)