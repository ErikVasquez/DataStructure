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
                        
def menu():     
        colac = ColasC() 
        
        while True: 
                
                

                print("\n1.-Push \n3.-Salir")
                opc = int(input("¿Qué desea hacer? "))
                os.system("clear")
                
                if opc==1: 
                        print(index)
                        x=int(input("Ingrese elemento: ")) 
                        print("")
                        colac.push(x)

                
                elif opc==7:
                        exit()
                        
                else :
                        print("\nOpcion invalida") 
                        
menu() 
