from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get("https://www.google.com")

time.sleep(5)
navegador.quit()