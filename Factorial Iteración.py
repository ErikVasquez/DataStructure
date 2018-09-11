#DelgadoVasquezErik No.Control 17211515


número = int(input("Ingrese un número para obtener su factorial: "))

factorial = int(1);
print("Factorial de " + str(número) + ": ")
for i in range(2, número+1):
    factorial = factorial*i
print(factorial)


input()
