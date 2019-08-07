"""
Auteur : Mehdi Guiraud
Description : Exemple de récupération de données
"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("https://www.paradisfiscaux20.com/liste-banques-offshore.htm")
Banques = driver.find_elements_by_css_selector("#tablepress-29")


for banque in Banques:
    print(banque.text)
driver.close()