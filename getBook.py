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
contenido = contenido.splitlines()

for l in contenido:
        matcher = patron.search(l)
        if matcher:
            m = matcher.group(0)
archivo.close()
print "Archivo cerrado"

pagina = 'https://www.packtpub.com/'
pagina += m+'/'
print pagina

subprocess.call(['firefox',pagina])
