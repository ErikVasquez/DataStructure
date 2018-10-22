import os 
front = 0 
rear = 0  
index = 0 

class ColasC():
        
        def __init__(self):
                self.cola = [0,0,0,0,0]
                
        def push(self,item): 
                global front  
                global rear   
                global index  
                if index == 5: 
                        print("\tCola llena") 
                else: 
                        rear = (front + index) % 5 
                        self.cola[rear] = item 
                        index += 1 
                        print("\tFront: " + str(front)) 
                        print("\tRear: "+ str(rear))
                        
        def peekfirst(self): 
                if index!=0: 
                        print("\n\tProximo dato a salir [" + str(self.cola[front]) + "]")
                else: 
                        print("\n\tNo hay dato proximo a salir, ingresa datos") 
                        
        def Peeklast(self): 
                if index!=0: 
                        print("\n\tUltimo dato a salir [" + str(self.cola[rear]) + "]")
                else: 
                        print("\n\tRegistre datos; Cola vacia") 
                        
        def peekindex(self,item): 
                z=-1 
                for i in range(0,len(self.cola)):  
                        if self.cola[i] == item: 
                                z=i 
                return z

        def  peekall(self):
                print("")
                for i,j in enumerate(self.cola): 
                        print('\t\t\t'+str([i,j]))              

                        
        def pop(self):  
                global front 
                global index 
                if index != 0: 
                        print("\n\tElemento eliminado [" + str(self.cola[front]) +"]") 
                        self.cola[front] = 0 
                        front= (front + 1) % 5 
                        print("\tFront: " + str(front)) 
                        index -= 1 
                else: 
                        print("\n\tIngrese datos, Cola vacia")

def menu():     
        colac = ColasC() 
        
        while True: 
                
                

                print("\n1.-Push \n2.-Pop\n3.-PeekFirst \n4.-Peeklast \n5.-Peekall \n6.-peekInd\n7.-Salir")
                opc = int(input("¿Qué desea hacer? "))
                os.system("clear")
                
                if opc==1: 
                        print(index)
                        x=int(input("Ingrese elemento: ")) 
                        print("")
                        colac.push(x)
                elif opc == 2: 
                        colac.pop()
                elif opc == 3: 
                        colac.peekfirst()
                
                elif opc == 4: 
                        colac.Peeklast()
                
                elif opc == 5: 
                        colac.peekall()
                
                elif opc==6: 
                        dato= int(input("\n\tIngresa dato a buscar -> "))
                        p = cola.peekindex(dato) 
                        if p != -1: 
                                print('\n\tDato [' + str(dato) +'] En posicion [' + str(p) + ']') 
                        else:
                                print("\n\tNo existe dato")
                
                elif opc==7:
                        exit()
                        
                else :
                        print("\nOpcion invalida")
                        
                        
menu() 
