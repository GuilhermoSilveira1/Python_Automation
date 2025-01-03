from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

navegador = webdriver.Chrome()
navegador.get("https://wiki.python.org/moin/FrontPage")
time.sleep(5)

search = navegador.find_element(By.ID, "searchinput")
search.send_keys("Intermediate")
time.sleep(5)
search.send_keys(Keys.RETURN)

drop_menu = Select(navegador.find_element(By.XPATH, "//*/form/div/select"))
drop_menu.select_by_visible_text("Raw Text")
time.sleep(5)

navegador.quit()