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
			self.end.next = self.ended.next = self.root
		else:
			temporal = self.ended 
			self.end = self.ended = temporal.next = Node(data)
			self.end.next = self.ended.next = self.root
		

class  Menu(): 
	
	def __init__(self): 
		self.op = None
		
	def fill(self): 
		filled = Rorschach() 
		while True: 
			print("\n1.-Guardar datos\n2.-Salir")
			self.op = int(input("\nIngrese opcion: ")) 
			os.system("clear")
			
			if self.op == 1:
				x = input("\nIngresa dato: ")
				filled.push(x)

			elif self.op == 2:
				sys.exit() 
				
			else: 
				print("\n\tOpcion invalida")


Imprimir = Menu()
Imprimir.fill()
