#DelgadoVasquezErik No.Control 17211515

fibonacci=[]
x=0
y=1
num = int(input("Numero de elementos:"))
for n in range(num):
    fibonacci.append(x+y)
    aux = x + y
    x = y
    y = aux
print(fibonacci)
