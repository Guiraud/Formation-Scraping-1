"""
Auteur : Mehdi Guiraud
Description : Exemple de récupération de données version 2
"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.get("https://www.banque-info.com/agences-bancaires/societe-generale/beaune")

Nom = driver.find_elements_by_css_selector("h1.text-center")
Adresse = driver.find_elements_by_css_selector("table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2)")
Code_postal = driver.find_elements_by_css_selector("table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)")
GPS = driver.find_elements_by_css_selector(".place-name")

print(''.join(Nom[0].text))
print(''.join(Adresse[0].text))
print(''.join(Code_postal[0].text))

driver.close()
