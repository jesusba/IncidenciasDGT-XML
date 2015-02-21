# -*- coding: utf-8 -*-

#5. Mostrar todas las incidencias entre dos fechas introducidas por el usuario.

from lxml import etree

incidencias=etree.parse('http://www.dgt.es/incidenciasXY.xml')
lista=incidencias.getroot()

fechainicio = raw_input("Introduzca una fecha (DD-MM-YYYY): ").upper()
fechafin = raw_input("Introduzca otra fecha (DD-MM-YYYY): ").upper()

fechainicior = fechainicio[8:10]+"-"+fechainicio[5:8]+fechainicio[0:4]
fechafinr = fechafin[8:10]+"-"+fechafin[5:8]+fechafin[0:4]

for n in xrange(len(lista)):
	if lista[n][6].text[:9] > fechainicior and fechafinr < lista[n][6].text[:9]:
		print " "
		print "ID Referencia:",lista[n][13].text
		print "Tipo de incidencia:",lista[n][0].text
		print "Población:",lista[n][5].text 
		print "Fecha de inicio:",lista[n][6].text 
		print "Causa:",lista[n][4].text 
		print "Nivel:",lista[n][7].text 
		print "Carretera:",lista[n][8].text 
		print "Sentido:",lista[n][11].text