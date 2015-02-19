# -*- coding: utf-8 -*-

# 1. Mostrar todas las incidencias existentes.

from lxml import etree

incidencias=etree.parse('http://www.dgt.es/incidenciasXY.xml')
lista=incidencias.getroot()

for n in xrange(len(lista)):
        print " "
        print "ID Referencia:",lista[n][13].text
        print "Tipo de incidencia:",lista[n][0].text
        print "Población:",lista[n][5].text 
        print "Causa:",lista[n][4].text 
        print "Nivel:",lista[n][7].text 
        print "Carretera:",lista[n][8].text 
        print "Sentido:",lista[n][11].text