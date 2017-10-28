#!/bin/bash

echo '[+] Ping www.packtpub.com'
echo '[+] Parsing web https://www.packtpub.com'

curl 'https://www.packtpub.com/packt/offers/free-learning' > packtpub.html

echo "[+] Web page scrapped"
