import os
import sys

class Node():
	def __init__(self, data):
		self.data = data 
		self.next = None 

class Rorschach(): 
	
	def __init__(self): 
		self.root = None 
		self.end = None 
		self.ended = None 
	
	def Null(self): 
		if self.root == None: 
			return True 
		else:
			return False 
		
	def push(self,data):
		
		if self.Null() == True: 
			self.root = self.end = self.ended = Node(data) 
		else:
			temporal = self.ended 
			self.end = self.ended = temporal.next = Node(data)
			
	def peek(self): 
		temp = self.root 
		if self.Null() == True: 
			print("\nNo existen datos. ") 
		else:
			while temp != None: 
				print("[" + str(temp.data)+"] ")  
				temp = temp.next 
	
	def Search(self,item): 
		temp = self.end = self.root 
		i = False 
		while temp != None:  
			if temp.data == item:  
				i = True 
				return i 
			else:
				temp = temp.next 
	
class  Menu(): 
	
	def __init__(self): 
		self.op = None
		
	def fill(self): 
		filled = Rorschach() 
		while True: 
			print("\n1.-Guardar datos\n2.-Mostrar datos\n3.-Buscar dato\n4.-Salir")
			self.op = int(input("\nIngrese opcion: ")) 
			os.system("clear") 
			
			if self.op == 1:
				x = input("\nIngresa dato: ")
				filled.push(x)
			
			elif self.op == 2:
				filled.peek() 
			
			elif self.op == 3:
				data = input("\nIngresa dato a buscar: ")
				check = filled.Search(data) 
				if check == True: 
					print("\nDato existente") 
				else:
					print("\nNo existe dato")
					
			elif self.op == 4:
				sys.exit() 
				
			else: 
				print("\nOpcion invalida")


Imprimir = Menu() 
Imprimir.fill()
