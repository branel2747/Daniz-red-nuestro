#!/usr/bin/env python3
# _*_ coding: utf8 _*_

from scapy.all import *
import argparse #definir objetivo especifico con consola

#puede escanear una ip o un rango

#permite la seleccion desde consola
parse=argparse.ArgumentParser()
parse.add_argument("-o","--rango",help="Rango de direcciones a escanear")
parse.add_argument("-f","--filepath",help="Lugar donde se va a guardar el archivo")
parse=parse.parse_args()

def ip_scan(ip,log): #detectar dispositivos conectados a la red 
	#variable q contiene la capa arp
	#configura el paquete arp para escanear las direcciones
	if str(ip)[-3:]!="/24":
		ip=str(ip)+"/24"
	range_ip=ARP(pdst=ip)#recibe el rango de direcciones ip
	#ff:fff direccion mac por defecto .
	broadcast=Ether(dst="ff:ff:ff:ff:ff:ff") #trabajar en capa 3
	#construir el paquete segun las capas
	final_packet=broadcast/range_ip

#funcion para enviar y recibir paquetes: srp
	#contiene la ip de envio y recibe
	# [0] da los resultados con respuesta, con dispo conectados
	res=srp(final_packet, timeout=2, verbose=False)[0] #p: paquete a enviar, tiempo de esp
	#verbose: cantidad info q se envia pantalla
	print("Dispositivos conectados a la red: ")
	if str(log)[-4:]==".txt":
		log=log[:-4]
	f=open("%s.txt" % (log), "w")
	for n in res:
		# n[1] datos dispositivo conectado
		# psrc: direccion ip

		print("[+] HOST: {}           MAC: {}".format(n[1].psrc, n[1].hwsrc ))
		f.write(str("[+] HOST: {}           MAC: {}".format(n[1].psrc, n[1].hwsrc ))+"\n")
	f.close()
def main():
	if parse.rango and parse.filepath: #verificar si se incluyo alguna opcion
		ip_scan(parse.rango,parse.filepath) #pasamos la opcion q pase el usuario en la linea de comando
	else:
		print("Falta rango de ip")


if __name__ == '__main__':

	main()
