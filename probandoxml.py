#!/usr/bin/env python3
#_*_ coding: utf8 _*_

import argparse #definir objetivo especifico con consola
import os
import xml2dict
#puede escanear una ip o un rango
import json
#permite la seleccion desde consola
parse=argparse.ArgumentParser()
parse.add_argument("-f","--filepath",help="Lugar donde se va a guardar el archivo")
parse=parse.parse_args()

def leerxml(log): #detectar dispositivos conectados a la red
	lista1=[]
	salida=[] 
	f=open("%s" %(log),"r").read()
	dicaleer=xml2dict.parse(f)
	necesito=["address","ports"]
	for h3 in necesito:
		if type(dicaleer["nmaprun"]["host"][h3])==list:
			for h4 in dicaleer["nmaprun"]["host"][h3]:
				if type(h4)==dict:
					#print(h4["@addr"])
					salida.append(h4["@addr"])
		if type(dicaleer["nmaprun"]["host"][h3])==dict:
			for h5 in dicaleer["nmaprun"]["host"][h3]:
				if h5=="port":
					if type(dicaleer["nmaprun"]["host"][h3][h5])==list:
						for h6 in dicaleer["nmaprun"]["host"][h3][h5]:
							#print(h6["@protocol"],h6["@portid"])
							lista1.append(h6["@protocol"]+":"+h6["@portid"])
	salida.append(lista1)
	print(salida)
	
def main():
	if  parse.filepath: #verificar si se incluyo alguna opcion
		leerxml(parse.filepath) #pasamos la opcion q pase el usuario en la linea de comando
	else:
		print("")


if __name__ == '__main__':
	main()
