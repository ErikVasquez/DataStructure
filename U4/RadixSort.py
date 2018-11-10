#Delgado Vasquez Erik No.Control 17211515
from math import log10
from random import randint
import random
def listaAleatorios(n):
    global alist
    alist = [0]  * n
    for i in range(n):
        alist[i] = random.randint(0, 1000)
    return alist
def get_digit(number, base, pos):
  return (number // base ** pos) % base
def prefix_sum(array):
  for i in range(1, len(array)):
    array[i] = array[i] + array[i-1]
  return array
def radixsort(alist, base=10):
    passes = int(log10(max(alist))+1)
    output = [0] * len(alist)
    for pos in range(passes):
        count = [0] * base
        for i in alist:
            digit = get_digit(i, base, pos)
            count[digit] +=1
        count = prefix_sum(count)
        for i in reversed(alist):
            digit = get_digit(i, base, pos)
            count[digit] -= 1
            new_pos = count[digit]
            output[new_pos]=i
        alist = list(output)
    return output
print("Ingrese cuantos numeros aleatorios desea obtener")
alist=int(input())
aleatorios=listaAleatorios(alist)
print(aleatorios)
input()
#alist=[randint(0,1000) for x in range(50)]
sorted = radixsort(alist)
print("Presione cualquier letra para imprimir la lista ordenada de menor a mayor.")
input()
print (sorted)
