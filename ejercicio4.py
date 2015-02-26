# -*- coding: utf-8 -*-

#4. Mostrar todas las incidencias existentes en una carretera determinada ordenados por tipo.

from lxml import etree

incidencias=etree.parse('http://www.dgt.es/incidenciasXY.xml')
lista=incidencias.getroot()
carreterausuario = raw_input("Introduzca una carretera para ver las incidencias existentes en ella: ").upper()

listacausas=[]

tiposdecausa=lista.findall("incidencia/causa")
	
for causas in tiposdecausa:
	if causas not in listacausas:
		listacausas.append(causas.text)

listacausasorden = sorted(set(listacausas))

print listacausasorden
for n in listacausasorden:
	if lista[n][8].text == carreterausuario:
		print " "
		print "ID Referencia:",lista[n][13].text
		print "Tipo de incidencia:",lista[n][0].text
		print "Población:",lista[n][5].text 
		print "Causa:",n
		print "Nivel:",lista[n][7].text 
		print "Carretera:",lista[n][8].text 
		print "Sentido:",lista[n][11].text