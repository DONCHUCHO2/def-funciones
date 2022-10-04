n = int(input("ingrese un valor:"))
n2 = int(input("ingrese un valor:"))

def calculo (n,n2):
    oper = (n/n2)
    return oper

print(f"el resto den la division es {n} divido entre {n2}")
print(f"el resultado del cociente es:",n/n2)

print(calculo(n,n2))