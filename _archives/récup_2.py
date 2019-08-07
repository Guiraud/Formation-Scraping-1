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

Url_formulaire = "https://alternatiba.frama.io/camp-climat-inscription/#/x-signin"
Lien_connexion = 'signin'
xpath_connexion = "//*[@id=\"signin\"]"
Link_text = "Me connecter*"
xpath_username = "//*[@id='login']"
selector_username = "#login"
selector_pass = "#password"
xpath_pass = "//*[@id='password']"
driver.get(Url_formulaire)
time.sleep(10)
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_username)))

driver.find_element_by_css_selector(selector_username).click()
driver.find_element_by_xpath(xpath_username).send_keys("mehdi.guiraud@gmail.com")
driver.find_element_by_css_selector(selector_pass).click()
driver.find_element_by_xpath(xpath_pass).send_keys("othello")
time.sleep(10)


driver.close()
