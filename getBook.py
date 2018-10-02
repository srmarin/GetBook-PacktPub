import subprocess
import os
import re
import time
import requests


BASE_URL = "https://www.packtpub.com/"
OFFERS_URL  = "https://www.packtpub.com/packt/offers/free-learning"
FREE_EBOOK_REGX = "freelearning-claim\/[0-9]+\/[0-9]+"


if __name__ == "__main__":

	# Is necessary because packtbub validate user-agent and discards request without this.
	user_agent = {'User-agent': 'Mozilla/5.0'}
	http_response = requests.get(OFFERS_URL, headers = user_agent)

	if http_response.status_code == 200:

		free_ebook_uri = None
		contenido = http_response.content

		if contenido!= None:
			patron = re.compile(FREE_EBOOK_REGX)
			contenido = contenido.splitlines()

			for l in contenido:
			        matcher = patron.search(l)
			        if matcher:
			            free_ebook_uri = matcher.group(0)

			if free_ebook_uri:
				pagina = BASE_URL + free_ebook_uri +'/'
				print pagina

				subprocess.call(['firefox',pagina])
