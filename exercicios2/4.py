saldo = float(input("Saldo: "))
cheque = float(input("Cheque: "))

if cheque > saldo:
    print("Cheque não pode ser descontado")
else:
    saldo -= cheque
    print("Cheque descontado, saldo:", saldo)