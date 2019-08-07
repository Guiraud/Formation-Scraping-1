"""
Auteur : Mehdi Guiraud
Description : Exemple de remplissage de formulaire.
"""

import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
Url_formulaire = "https://agences-bancaires.banques-en-ligne.fr/banque-societe-generale-meaux-victor-hugo-16587.html"
Lien_connexion = 'signin'
#xpath_connexion = "//*[@id=\"signin\"]"
xpath_connexion = "//*[@id='coordRight']/div[1]/a"
Link_connexion = "Afficher le numéro*"
driver.get(Url_formulaire)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_connexion)))
driver.find_element_by_link_text(Link_connexion).click()
time.sleep(1)
print(driver.find_element_by_xpath(xpath_connexion).text)
#driver.find_element_by_id(Lien_connexion).click
#time.sleep(15)


driver.close()
