#Delgado Vasquez Erik No.Control 17211515
v = 0
ind = 0
elec = ""
stock =[]

def push(ind, v):
    stock.append(v)
    return ind +1

def peek(elec):
    if elec =="T":
        print (stock)
    else:
        elec = int(elec)
        if elec>=0 and elec<5:
            print (stock[elec])
        else:
            1
            print ("Indice fuera de rango")
while ind>=0 and ind<5:
    v = int(input("Ingrese un valor entero (" +str(ind+1)+"/5): "))
    ind = push(ind,v)

elec = str(input("Teclee ""T"" Para mostras la lista o ingrese el indice del valor que desea ver(0 a 4): "))
peek(elec)
