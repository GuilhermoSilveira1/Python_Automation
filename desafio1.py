from selenium import webdriver
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get("https://www.selenium.dev/")
id = navegador.find_element(By.ID, 'q')
nome = navegador.find_element(By.NAME,"q")
xpath = navegador.find_element_by_xpath("//////div")
classe = navegador.find_element_by_class_name("selenium-sponsors")

print(id)
print(nome)
print(xpath)
print(classe)

navegador.quit()