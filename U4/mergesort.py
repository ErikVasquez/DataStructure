import random
def listaAleatorios(n):
    global alist
    alist = [0]  * n
    for i in range(n):
        alist[i] = random.randint(0, 1000)
    return alist

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

print("Ingrese cuantos numeros aleatorios desea obtener")
alist=int(input())
aleatorios=listaAleatorios(alist)
print(aleatorios)
input()
mergeSort(alist)
print(alist)
