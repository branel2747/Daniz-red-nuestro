import sys
import argparse
import os
import subprocess
import re
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
from multiprocessing import Queue
import threading
import base64
import time
#import ConfigParser
from sys import argv
#from commands import *
from getpass import getpass
from xml.dom import minidom
#from urlparse import urlparse
import urllib.parse as urlparse
from optparse import OptionParser
from time import gmtime, strftime, sleep
#from probandoxml import *
import netifaces as ni

global dircompleta

def nucljson(archivo):
	abierto=open(archivo,"r").read().split("\n")
	cont=0
	#print(len(abierto))
	if len(abierto)>0:
		for i in abierto:
			cont=cont+1
			#print(i,"hola")
			
			f=open(str(cont)+".json","w")
			f.write(i)
			f.close
			#subprocess.Popen(["firefox",str(cont)+".json"])

		lista =[]
		for j in range(cont-1):
			#print(str(j+1)+".json")
			with open(str(j+1)+".json") as file:
		    		data = json.load(file)
			lista.append(str(data["matched"])+"-->"+str(data["info"]["reference"]))
		for j1 in range(cont):
			subprocess.Popen(["rm","-r", str(j1+1)+".json"])
		return(lista)
def prueba(existe):
	try:
		m=open(existe+".txt","r")
		print("se abrio")
		m.close()
	except:
		try:
			m=open(existe+".xml","r")
			m.close()
		except:
			try:
				m=open(existe+".json","r")
				m.close()
			except:
				pass
	return

def correrprog(objetivo,progra,arch,conte):
	prog=["python3"]
	fase_1=arch		
	for i in range(len(conte)):
		for j in range(len(prog)):
			try:
				os.system("sudo %s %s -o %s -f %s" % (prog[j],progra+ conte[i],objetivo,fase_1+str(conte[i])[:-3]))  #ejecucion de programa cuando tiene -o y -f
				print("sudo %s %s -o %s -f %s" % (prog[j],progra + conte[i],objetivo,fase_1+str(conte[i])[:-3]))
			except:
				pass

def clearScr():
	os.system('clear')
def seleccionmul(path,tipo1,info):
	
	opt=""
	manlist=crearmenu(path,tipo1)
	menu=manlist[0]
	
	lista1=manlist[1]
	listob=[]
	#raw_input(manlist[1])
	
	while opt!="a" and opt!="b" and opt!="q":
		clearScr()
		print("Informacion: ")
		print(str(info))
		print(str(tipo1)+" seleccionados: ",listob)
		print(menu)
		opt=input("Seleccione--> ")
		clearScr()
		if opt=="a":
			sal=[]
			for i in listob:
				if i not in sal:
					sal.append(i)
			return(sal)
		elif opt=="b":
			clearScr()
			return(lista1)
		elif opt=="q":
			clearScr()
			return("atras")
		try:
			if lista1[int(opt)-1] in lista1:
				listob.append(lista1[int(opt)-1])
		except:
			print("No existe el/la "+ str(tipo1))
	#print(listob)
		
		
def crearmenu(path1,tipo):
	if type(path1)==str:
		lista=os.listdir(path1)
	elif type(path1)==list:
		lista=path1
	m=""
	for i in range(len(lista)):
			m=m+"{"+str(i+1)+"}--"+lista[i]+"\n"
	m=m+"{a}--Continuar con l@s " +str(tipo)+ " seleccionad@s "+"\n"
	m=m+"{b}--Automatico--(Tod@s l@s "+str(tipo)+")--"+"\n"
	m=m+"{q}--Salir"
	return ([m,lista])

class color:
	HEADER = '\033[95m'
	IMPORTANT = '\33[35m'
	NOTICE = '\033[33m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	RED = '\033[91m'
	END = '\033[0m'
	UNDERLINE = '\033[4m'
	LOGGING = '\33[34m'


class principal:
	def __init__(self):
		clearScr()
		os.system("rm -r /home/kali/Downloads/Daniz_Red/archivos/hosts/fase_2/*")
		os.system("rm -r /home/kali/Downloads/Daniz_Red/archivos/hosts/fase_1/*")
		os.system("rm -r /home/kali/Downloads/Daniz_Red/archivos/hosts/fase_3/*")
		os.system("rm -r /home/kali/Downloads/Daniz_Red/archivos/hosts/explotacion/*")
		clearScr()
		print (color.HEADER+"************************* DaNiz Red Team*************************"+ color.END+ '''
			''' + color.OKBLUE + '''
		   {1}--Comenzar analisis
		   {2}--Revisar reportes
		   {3}--Cargar modulos
		   {99}-Salir\n
			'''+color.END)
		choice = input("opcion: ")
		
		if choice == "1":
			opt2=""
			while opt2!="99":
				clearScr() 
				print (color.HEADER+"*************************** Comenzando el analisis ***************************"+color.END)
				print(color.WARNING+"Este sistema puede realizar las siguientes auditorias:"+color.END)
				print (color.OKBLUE+'''
			   {1}--Analisis a hosts
			   {2}--Analisis a paginas web
			   {3}--Analisis a Redes
			   {99}-Salir\n
				'''+color.END)
				opt2=input("Ingrese opcion: ")
				if opt2=="1":
					clearScr()
					print(color.NOTICE+'''
			En este tipo de auditoria, comienza buscando los hosts pertenecientes a la red
			o a la pagina auditada y mediante estos hosts obtener vulnerabilidades que
			posteriormente se explotaran mediante metodos varios.
			
			Por tanto, la informacion que se ingrese aqui puede ser un host que se desea 
			analizar de la red actual, una pagina web o si se deja vacio realizar
			el escaneo de la red local automaticamente.
					'''+color.END)
					obj_fase_1=""
					obj_fase_1=input("Ingrese objetivo: ")
					if obj_fase_1=="":
						ni.ifaddresses('eth0')
						ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
						listado=ip.split(".")
						sin=listado[:-1]
						obj_fase_1=str(".".join(sin))+".0/24"
						#print (ip)
		    			#contenido=os.listdir(str(os.getcwd())+"/modules/hosts/fase_1")
					contenido=""
					while contenido!="atras":
						contenido=seleccionmul((os.getcwd())+"/modules/hosts/fase_1","programas","") #accede al programa que permite seleccionar entre los programas existente u objetivos a utilizar 
						#print(contenido)
						if type(contenido) == list and len(contenido)>0:
							program=str(os.getcwd())+"/modules/hosts"  # lugar donde se encuentran los programas
							filepath=str(os.getcwd())+"/archivos/hosts" #lugar a donde van a ir los archivos encontrados y de donde tiene que salir el informe de esta parte
							programa=program+"/fase_1/"
							fase_1=filepath+"/fase_1/"
							correrprog(obj_fase_1,programa,fase_1,contenido)
							print(color.NOTICE+'''
			Se obtienen los ip referentes a la pagina o red ingresada, de manera que luego
			se pueda determinar mas informacion acerca de la direccion ingresada.
			    			'''+color.END+"\n")	
							print(color.NOTICE+"Se finalizo la primera parte de la auditoria a hosts"+color.END)
							input("Presione enter para continuar...")
							clearScr()
							input_fase_2=os.listdir(fase_1)
							print (input_fase_2)
							f2_obj=[]
							for i2 in input_fase_2:
								f2_aux = os.popen("cat %s | grep -E -o \"([0-9]{1,3}[\.]){3}[0-9]{1,3}\" " % (fase_1+i2)).read().split("\n")[:-1] #comando para conseguir ips desde un archivo cualquira
								for i3 in f2_aux:
									if i3 not in f2_obj:
										f2_obj.append(i3)
							if len(f2_obj)!=0:
								fase2obj=""
								while fase2obj!="atras":
									fase2obj=seleccionmul(f2_obj,"ips","") #accede al programa que permite seleccionar entre los programas existente u objetivos a utilizar
									#print (fase2obj," estas son las ips")
									if type(fase2obj)==list and len(fase2obj)>0:
										contenidof2=""
										while contenidof2!="atras":
											contenidof2=seleccionmul((os.getcwd())+"/modules/hosts/fase_2","programas","")
											if type(contenidof2)==list and len(contenidof2)>0: 
												
												prograf2=program+"/fase_2/"
												fase_2=filepath+"/fase_2/"
								    				#print("soy una "+ str(type(fase2obj)))
								    				#input("que eres")
							    				
												
												
												for f2 in fase2obj:
								    					correrprog(f2,prograf2,fase_2+str(f2),contenidof2)
								    				
												fase_2_fils=os.listdir(fase_2)
												fase_2_salida=[]
												for fil1 in fase_2_fils:
													
													if ".xml" in fil1:
														lista=os.popen("python3 probandoxml.py -f %s" %(fase_2+fil1)).read().replace("[","").replace("'","").replace("]]","").replace("\n","").split(",")
														#input(lista)
														#fin=[]
														#for f2i in lista:
														#	uni=fin.append(f2i.split(","))
														#for f2j in lista:
															#print(len(f2j))
														if len(lista)>=2: 
															fase_2_salida.append(["Ip: ",lista[0]," Mac: ",lista[1]," puertos =",lista[2:]])
												#print(fase_2_salida," " ,str(len(fase_2_salida)))
												
												
												obj_f3=[]
												f3_info=""
												for f2int in fase_2_salida:
													finf2=""
													#print("cuantos", len(f2int))
													for f2int2 in f2int:
														finf2=finf2+str(f2int2)
													if f2int[1] not in obj_f3:
														obj_f3.append(f2int[1])
														f3_info= f3_info + str(finf2) +"\n"
													#print(str(finf2))
												#print("*********Informacion acerca de los puertos de los objetivos*********")							
												#print(obj_f3)
												print(color.NOTICE+'''
			Mediante la obtencion de los puertos existentes en cada una de las direcciones 
			se puede determinar cuales son los mejores objetivos.
					    							'''+color.END+"\n")	
												print(color.NOTICE+"Se finalizo la segunda parte de la auditoria a hosts"+color.END)
												input("Presione enter para continuar...")
												prograf3=program+"/fase_3/"
												fase_3=filepath+"/fase_3/"						######------------>######desde aqui va la fase 3...... una vez se tienen los puertos
												fase3obj=""
												while fase3obj!="atras":
													fase3obj=seleccionmul(obj_f3,"ips",f3_info)
													contenidof3=""
													if type(fase3obj)==list and len(fase3obj)>0:
														while contenidof3!= "atras":
															contenidof3=seleccionmul((os.getcwd())+"/modules/hosts/fase_3","programas","")

															if type(contenidof3)==list and len(contenidof3)>0:
																for f3 in fase3obj:
										    							correrprog(f3,prograf3,fase_3+str(f3),contenidof3)
																print(color.NOTICE+'''
				En este punto ya se obtuvieron resultados acerca de las vulnerabilidades
				existentes en los objetivos seleccionados.
								    								'''+color.END+"\n")
																print(color.NOTICE+"Se finalizo la tercera parte de la auditoria a hosts"+color.END)
																### En esta parte se hace uso de las respuestas de nuclei para poder recomendar programas
																vulnprog=program+"/ejecutadores/" # se hace uso de fase_3
																listvulprog=os.listdir(vulnprog)
																nulist=os.listdir(fase_3)
																vulnrep=filepath+"/explotacion/"
																nucleilis=[]
																for nu in nulist:
																	print(nu)
																	if "nuclei.json" in nu:
																		
																		#nuclist.append(nu)
																		nucleilis = nucleilis + nucljson(fase_3+nu)
																nucleilist=[]
																
																for nuc in nucleilis:
																	if nuc not in nucleilist:
																		nucleilist.append(nuc)
																
																print(nucleilist)
																reco=[]
																for expr in listvulprog:
																	for resvul in nucleilist:
																		print(resvul[:-3].lower())
																		if expr[:-3].lower() in resvul.lower():
																			reco.append([expr,resvul])
																
																#input(reco)
																
																
																if len(reco)>0:
																	clearScr()
																	print('''
				Entre los programas de explotacion cargados, al compararlos con las
				vulnerabilidades encontradas se encontraron que lo siguientes programas 
				de explotacion se pueden ejecutar en el objetivo. \n
																	''')
																	input("Presione enter para continuar...")
																	for recoi in reco:
																		print(recoi[0]+"->"+recoi[1])
																	#input("si llego aqui")
																	ip=""
																	for recoj in reco:
																		clearScr()
																		for letra in recoj[1]:
																			if letra==":":
																				break
																			else:
																				ip=ip+letra
																		###el archivo no lleva .txt por que lo tiene en el programa de ejecucion
																		os.system("python3 %s -o %s -f %s" % (vulnprog+recoj[0],ip,vulnrep+str(ip)+str(recoj[0][:-3]))) 
																		os.system("less %s"%(vulnrep+str(ip)+str(recoj[0][:-3])+".txt" ))
																		print("Ataque "+str(recoj[0])+" realizado")
																		input("Presione intro para continuar...")
																		
																		
																## fin de la parte de recomendacion o ataque
																fase4obj=""
																
																while fase4obj!="atras":
																	#prograf4=program+"/fase_4/"
											    						#fase_4=filepath+"/fase_4/"
																	fase4obj= seleccionmul(fase_3,"Archivos",'''
				Llegados a este punto se tiene que saber que vulnerabilidades 
				existen en los objetivos selecciones, por ese motivo. Seleccione
				que archivos desea tener como ayuda para realizar un ataque.
																	''')
													
																	if type(fase4obj)==list and len(fase4obj)>0:
																		for lf4 in fase4obj:
																			input()
																			if lf4[-4:]==".xml" or lf4[-5:]==".html":
																				subprocess.Popen(["firefox",fase_3+lf4])
																				clearScr()
																				pass
																			elif lf4[-4:]==".txt":
																				pass
																		contenidof4=""
																		while contenidof4 != "atras":
																			print('''
				Con la informacion presentada a modo de reporte el usuario a de 
				visualizar que tipo de vulnerabilidades existen y con esta informacion 
				seleccionar con que herramienta desea explotarlas.
																			''')
																			#contenidof4=seleccionmul((os.getcwd())+"/modules/hosts//explotacion","programas","")
																			
																			os.system("msfconsole")
																			
																			
																		
																
												#raw_input("paraaaaa")
												
											
										
							#raw_input("hasta aqui")
							
					
					
					
					
									#print ("%s %s -o %s > %s" % (prog[j],programa + contenido[i],obj_fase_1,filepath+str(contenido[i])[:-3]+".txt"))
									#raw_input("Este codigo no funciono con %s" % (prog[j]))
					
					#raw_input("hasta aqui vamo")
				elif opt2=="2":
	    				print("opcion 2")
		elif choice == "2":
			
			clearScr()
		elif choice == "3":
			clearScr()
		    
		elif choice == "99":
			sys.exit()
		elif choice == "\r" or choice == "\n" or choice == "" or choice == " ":
			self.__init__()
		else:
			try:
				print(os.system(choice))
			except:
				pass
		self.__init__()
		#self.completed()
	
	def completed(self):
		input("Completado, presione enter para continuar")
		self.__init__()
		
if __name__ == "__main__":
	try:
		principal()
	except KeyboardInterrupt:
        	print(" Finishing up...\n")
        	time.sleep(0.25)



