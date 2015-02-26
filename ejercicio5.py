# -*- coding: utf-8 -*-

#5. Mostrar todas las incidencias entre dos fechas introducidas por el usuario.

from lxml import etree
from datetime import datetime

incidencias=etree.parse('http://www.dgt.es/incidenciasXY.xml')
lista=incidencias.getroot()

fechainicio = raw_input("Introduzca una fecha (DD-MM-YYYY): ").upper()
fechafin = raw_input("Introduzca otra fecha (DD-MM-YYYY): ").upper()

confechaini = datetime.strptime(fechainicio, "%d-%m-%Y")
confechafin = datetime.strptime(fechafin, "%d-%m-%Y")

fechas=lista.findall("incidencia/fechahora_ini")
for f in fechas:
	confechadgt=datetime.strptime(f.text, "%Y-%m-%d %H:%M")
	if confechadgt > confechaini and confechafin > confechadgt:
		print " "
		print "ID Referencia:",f.getparent().find("ref_incidencia").text	
		print "Tipo de incidencia:",f.getparent().find("tipo").text	
		print "Población:",f.getparent().find("poblacion").text	
		print "Fecha de inicio:",f.getparent().find("fechahora_ini").text	
		print "Causa:",f.getparent().find("causa").text	
		print "Nivel:",f.getparent().find("nivel").text	
		print "Carretera:",f.getparent().find("carretera").text	
		print "Sentido:",f.getparent().find("sentido").text	