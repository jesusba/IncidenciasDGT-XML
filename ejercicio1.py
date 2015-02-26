# -*- coding: utf-8 -*-

# 1. Mostrar todas las incidencias existentes.

from lxml import etree

incidencias=etree.parse('http://www.dgt.es/incidenciasXY.xml')
lista=incidencias.getroot()

listaincidencias=lista.findall("incidencia")

for n in listaincidencias:
	print " "
	print "ID Referencia:",n.getparent().find("incidencia/ref_incidencia").text	
	print "Tipo de incidencia:",n.getparent().find("incidencia/tipo").text	
	print "Población:",n.getparent().find("incidencia/poblacion").text	
	print "Fecha de inicio:",n.getparent().find("incidencia/fechahora_ini").text	
	print "Causa:",n.getparent().find("incidencia/causa").text	
	print "Nivel:",n.getparent().find("incidencia/nivel").text	
	print "Carretera:",n.getparent().find("incidencia/carretera").text	
	print "Sentido:",n.getparent().find("incidencia/sentido").text	