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


#driver = webdriver.Chrome(executable_path="/Users/mguiraud/Dropbox/CC2019/Scrapping Avancé/chromedriver")
driver = webdriver.Firefox()

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
