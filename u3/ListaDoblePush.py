import os
import sys

class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None

class Rorschach(): 
    
    def __init__(self): 
        self.root = None 
        self.due = None 

    
    def Null(self): 
        if self.root == None: 
            return True 
        else:
            return False

    def Lpush(self,data):
        if self.Null() == True: 
            self.root = self.due = Node(data) 
        else:
            temp = Node(data)
            temp.next = self.root
            self.root.prev = temp
            self.root = temp
        
    def Rpush(self,data):
        if self.Null() == True: 
            self.root = self.due = Node(data) 
        else:
            temporal = self.due
            self.due = temporal.next = Node(data)
            self.due.prev = temporal
        

class  Menu(): 
    
    def __init__(self): 
        self.op = None
        
    def fill(self): 
        filled = Rorschach() 
        while True: 
            print("\n1.-Ingresar datos por izquierda\n2.-Ingresar datos por derecha\n3.-Salir")
            self.op = int(input("\nIngrese opcion: ")) 
            os.system("clear")
            
            if self.op == 1:
                data = input("\nIngrese dato: ")
                filled.Lpush(data)
                
            elif self.op == 2:
                data = input("\nIngrese dato: ")
                
                filled.Rpush(data)

            elif self.op == 3:
                sys.exit() 
                
            else: 
               print("\nOpcion invalida.")
            


Imprimir = Menu()
Imprimir.fill()
