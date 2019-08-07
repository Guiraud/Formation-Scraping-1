from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os

profile = FirefoxProfile(r'/Users/mguiraud/Library/Application Support/TorBrowser-Data/Browser/o45k8lgc.default')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()
#driver = webdriver.Firefox()
driver = webdriver.Firefox(firefox_profile=profile)
driver.get("http://check.torproject.org")