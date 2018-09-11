#DelgadoVasquezErik No.Control 17211515

def facto(n):
    if n ==1:
        return 1
    else :
        return n*facto(n-1)
n=int(input("Ingrese el número a sacar factorial: "))
print(facto(n))
