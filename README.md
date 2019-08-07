# Formation-Scraping-1
Premier pas dans le scraping.

## Présentation :
https://cryptpad.fr/slide/#/2/slide/edit/YW8uXB0Ibdhun1Sqc2J2THj0/

L'objectif de cette formation est de vous donner les bases du scraping sur Internet.

Vous trouverez dans ce dossier plusieurs exercices résolus.

# Installation
## Python 3.7
### Windows : https://www.python.org/downloads/windows/
### Linux : 
```bash

apt install python3.7
#il est probable que vous ayez déjà Python sur votre machine. Dans ce cas tester la version en tapant :
python -V
# si vous obtenez une version supérieur à 3.6, tout va bien. Si non mettez à jour la version en tapant :
vi ~/.bash_profile  
alias python='/usr/local/bin/python3'
source ~/.bash_profile
```

### Sous Mac os X :
http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/

```
cd
mkdir Code
#installez Homebrew si ce n'est pas déjà le cas
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
#Installation de Python
brew install python
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
```
# Préparation de votre environnement 
```bash
pip install virtualenv
```
# installation des librairies utiles
```
pip install -r requirements.txt
```
# Le driver de conexion 
pour installer les drivers se reporter à la bonne version pour votre ssystème d'exploitation :
* Gecko Driver : https://github.com/mozilla/geckodriver/releases
<br>
* Chrome driver : https://chromedriver.chromium.org/

# Les exercices :
##  récup_0.py
Récupération d'un tableau
##  récup_1.py
Récupération de plusieurs champs
##  récup_2.py
Click en utilisant Firefox
##  récup_3.py
Script pour tester le driver Chrome
##  test_tor.py
Tester la présence de TOR
## get_by_tor.py
Scraping via Tor