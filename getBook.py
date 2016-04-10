import subprocess
import os
import re
import time

subprocess.call(['sh','getPage.sh'])

archivo = open("packtpub.html", "r")
contenido = archivo.read()
if contenido!= None:
    print "Archivo abierto"


patron = re.compile('freelearning-claim\/[0-9]+\/[0-9]+')
pagina = 'https://www.packtpub.com/'
contenido = contenido.splitlines()

for l in contenido:
        #pos = lineas.find('<a href="/freelearning-claim/')
        print l
        #time.sleep(2)
        matcher = patron.search(l)
        if matcher:
            m = matcher.group(0)

print m
archivo.close()
print "Archivo cerrado"

pagina += m+'/'
print pagina
subprocess.call(['firefox',pagina])
