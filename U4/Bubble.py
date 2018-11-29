#Delgado Vasquez Erik No.Control 17211515
import random
def listaAleatorios(n):         #se crea el metodo del cual se obtendra un arreglo de elementos completamente aleatorios
    global lista        #se crea la variable global lista
    lista = [0]  * n        #se multiplica un arreglo con un elemento 0 por el numero de datos solicitados
    for i in range(n):          #se crea un for donde 
        lista[i] = random.randint(0, 1000)      #se creara un arreglo completamente aleatorio entre los numeros escogidos
    return lista                    #se devuelve el arreglo
def Bubbles(lista):             #metodo burbuja, recibe como parametro el arreglo para acomodarlo posteriormente
    bubble=0
    for i in range (0,len(lista)):      #se meten en un for el arreglo que va desde 0 hasta el largo del arreglo
        for j in range (0,len(lista)-1): #se crea un for desde 0 asta el penultimo valor del largo del arreglo
            if lista[j]>lista[j+1]:         #si la lista en j es mayor qe el siguiente valor en la lista entonces
                bubble=lista[j+1]           #se iguala la bariable bubble el valor siguiente de j
                lista[j+1]=lista[j]         #se guarda en dato de j en el dato siguiente de j
                lista[j]=bubble             #se guarda el dato de bubble en j
print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
aleatorios=listaAleatorios(n)
print(aleatorios)
input()
cobra=Bubbles(lista)
print("Presione cualquier letra para imprimir la lista ordenada de menor a mayor.")
input()
print(lista)




