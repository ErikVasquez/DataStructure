#Delgado Vasquez Erik No.Control 17211515
import random
def listaAleatorios(n):
    global alist
    alist = [0]  * n
    for i in range(n):
        alist[i] = random.randint(0, 1000)
    return alist
def shellSort(alist):
    gap=len(alist)//2
    while gap>0:
        for i in range(gap,len(alist)):
            val=alist[i]
            j=i
            while j >= gap and alist[j-gap]>val:
                alist[j]=alist[j-gap]
                j-=gap
            alist[j]=val
        gap//=2
print("Ingrese cuantos numeros aleatorios desea obtener")
alist=int(input())
aleatorios=listaAleatorios(alist)
print(aleatorios)
input()
cobra=shellSort(alist)
print("Presione cualquier letra para imprimir la lista ordenada de menor a mayor.")
input()
print(alist)
    
