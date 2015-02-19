# -*- coding: utf-8 -*-

# 3. Contar las incidencias de cada nivel.

from lxml import etree

incidencias=etree.parse('http://www.dgt.es/incidenciasXY.xml')
lista=incidencias.getroot()

acumverde = 0
acumamarillo = 0
acumrojo = 0
acumnegro = 0

for n in xrange(len(lista)):
	if lista[n][7].text == 'VERDE':
		acumverde = acumverde+1
	elif lista[n][7].text == 'AMARILLO':
		acumamarillo = acumamarillo+1
	elif lista[n][7].text == 'ROJO':
		acumrojo = acumrojo+1
	elif lista[n][7].text == 'NEGRO':
		acumnegro = acumnegro+1

print "Incidencias de nivel verde:",acumverde
print "Incidencias de nivel amarillo:",acumamarillo
print "Incidencias de nivel rojo:",acumrojo
print "Incidencias de nivel negro:",acumnegro