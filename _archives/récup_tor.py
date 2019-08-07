"""
Auteur : Mehdi Guiraud
Description : Exemple de connexion avec TOR
brew services start tor
brew services stop tor
"""
#base_socks_port=9050
#base_control_port=8118
"""
tor \
 --CookieAuthentication 0 \
 --HashedControlPassword "" \
 --ControlPort 8128 \
 --PidFile tor.pid \
 --SocksPort 9050 \
 --DataDirectory data/tor
"""

"""
tor \
 --RunAsDaemon 1 \
 --CookieAuthentication 0 \
 --HashedControlPassword "" \
 --ControlPort 8118 \
 --PidFile tor.pid \
 --SocksPort 9050 \
 --DataDirectory data/tor
"""

import selenium
import time
from lxml import etree
import urllib
import urllib.request
from lxml.cssselect import CSSSelector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxy_support = urllib.request.ProxyHandler({'http' : '127.0.0.1:8128'})

#proxy_support = urllib.ProxyHandler({"http" : "127.0.0.1:8128"} )
xpath_capture = "id('ContainerMain')/nav[2]/ul/li[1]/span[2]/b/text()"
opener = urllib.request.build_opener(proxy_support) 
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0')]

check_torproject = "http://whatismyipaddress.com/"
x_tor = "//html//body//div[@id='outertop']//div[@id='main']//div[@id='wrap']//div[@id='section_content_full']//div[@id='main_content']//div[@id='section_left']//div[2]/text()"
html = opener.open(check_torproject).read()
parser = etree.HTMLParser()
tree = etree.parse(StringIO.StringIO(html), parser)
Ip_address = tree.xpath(x_tor)
print(Ip_address)
if Ip_address == "77.247.181.163":
	print("Erreur de proxy - on sort ")
	exit

"""
html = opener.open(lien).read()
parser = etree.HTMLParser()
tree = etree.parse(StringIO.StringIO(html), parser)
texte_a_capturer = tree.xpath(xpath_a_capturer)

#
css_catch = CSSSelector('div.content')
XUrl = tree.xpath(URL)

Url_formulaire = "https://framaforms.org/formulaire-de-test-pour-le-scraping-1564989476"
driver.get(Url_formulaire)
time.sleep(1 )
login = "#edit-submitted-comme-un-login"
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login)))
print("Présent !")
driver.find_element_by_css_selector(login).click()
driver.find_element_by_css_selector(login).send_keys("mehdi.guiraud@gmail.com")
time.sleep(10)

driver.close()
"""