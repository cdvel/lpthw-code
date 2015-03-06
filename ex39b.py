# -*- coding: utf-8 -*-
# ciudades en Colombia

import codecs
import locale

locale.setlocale(locale.LC_ALL,"") 

ciudadxdepto = {
u'Bogotá': u"Bogotá",
u"Medellín":u"Antioquia",
u"Cali":u"Valle del Cauca",
u"Barranquilla":u"Atlántico",
u"Cartagena de Indias":u"Bolívar",
u"Cúcuta":u"Norte de Santander",
u"Bucaramanga":u"Santander",
u"Soledad":u"Atlántico",
u"Ibagué":u"Tolima",
u"Armenia":u"Quindío",
u"Villavicencio":u"Meta",
u"Soacha":u"Cundinamarca",
u"Pereira":u"Risaralda",
u"Bello":u"Antioquia",
u"Valledupar":u"Cesar",
u"Montería":u"Córdoba",
u"Pasto":u'Nariño',
u"Manizales":u"Caldas",
u"Buenaventura":u"Valle del Cauca",
u"Neiva":u"Huila ",
u"Santa":u"Marta Magdalena",
u"Palmira":u"Valle del Cauca",
u"Popayán":u"Cauca",
u"Barrancabermeja":u"Santander",
u"Sincelejo":u"Sucre",
u"Itagui":u"Antioquia",
u"Floridablanca":u"Santander",
u"Riohacha":u"La Guajira",
u"Envigado":u"Antioquia",
u"Tuluá":u"Valle del Cauca"
};

poblacion = {
u"Bogotá": 8193869,
u"Medellín": 3471481,
u"Cali": 3334714,
u"Barranquilla": 2169158,
u"Cartagena de Indias": 1189795,
u"Cúcuta": 1054666,
u"Bucaramanga": 1047479,
u"Soledad": 543474,
u"Ibagué": 548209,
u"Armenia": 321378,
u"Villavicencio": 488366,
u"Soacha": 487236,
u"Pereira": 483185,
u"Bello": 447185,
u"Valledupar": 443210,
u"Montería": 434950,
u"Pasto": 434486,
u"Manizales": 394627,
u"Buenaventura": 362054,
u"Neiva": 342148,
u"Santa": 492097,
u"Palmira": 320784,
u"Popayán": 302067,
u"Barrancabermeja": 325456,
u"Sincelejo": 271375,
u"Itagui": 264775,
u"Floridablanca": 264695,
u"Riohacha": 250236,
u"Envigado": 217343,
u"Tuluá": 209086,
}

print '-'*30
print '**Departamentos por ciudad'
print '-'*30
print 'Pasto => %s' %ciudadxdepto[u"Pasto"].encode('utf-8')
print 'Popayán => %s'% ciudadxdepto[u"Popayán"].encode('utf-8')
print 'Barranquilla => %s'% ciudadxdepto[u"Barranquilla"].encode('utf-8')

print '-'*30
print '**Poblacion por ciudad'
print '-'*30
print "Pasto => %s" % locale.format('%d', poblacion[u"Pasto"], True); 
print "Popayán => %d" % poblacion[u"Popayán"]
print "Barranquilla => %d" % poblacion[u"Barranquilla"]


print '-'*35
print '**Poblacion principles ciudades'
print '-'*35
for ciudad, habitantes in poblacion.items():
	encoded = ciudad.encode('utf-8')
	formatted = locale.format('%d', habitantes, True);
	depto = ciudadxdepto[ciudad]
	print " %s, %s = \t\t%s " % (encoded, depto.encode('utf-8'),formatted)


# obtener poblacion no existente sin error
poblacion.get(u"San Andrés", None)
if not poblacion:
	print "No hay datos sobre San Andrés"

# o usar valor por defecto
depto = ciudadxdepto.get(u'San Andrés', 'No hay datos')
print "Ciudad: San Andrés = %s" % depto;