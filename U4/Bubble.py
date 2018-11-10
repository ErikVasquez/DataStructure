#Delgado Vasquez Erik No.Control 17211515
import random
def listaAleatorios(n):
    global lista
    lista = [0]  * n
    for i in range(n):
        lista[i] = random.randint(0, 1000)
    return lista
def Bubbles(lista):
    bubble=0
    for i in range (0,len(lista)):
        for j in range (0,len(lista)-1):
            if lista[j]>lista[j+1]:
                bubble=lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=bubble
print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
aleatorios=listaAleatorios(n)
print(aleatorios)
input()
cobra=Bubbles(lista)
print("Presione cualquier letra para imprimir la lista ordenada de menor a mayor.")
input()
print(lista)




