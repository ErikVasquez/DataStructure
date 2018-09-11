#DelgadoVasquezErik No.Control 17211515

def fib(n):
    if n==1 or n==2:
        return n
    elif n>2:
        return fib(n - 1) + fib(n - 2)
    
n=int(input("Ingrese el número para hacer la sucesión fibonacci: "))
print("Secuencia fibonacci de " + str(n) + ": " )
