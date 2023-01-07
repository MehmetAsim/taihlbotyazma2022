

from moduller.tarayici import Tarayici
from selenium.webdriver.common.by import By
from time import sleep

tarayici_nesnesi = Tarayici()
tarayici = tarayici_nesnesi.al()

tarayici.get("https://teknolojiaihl.meb.k12.tr")
tarayici.maximize_window()

baslik = tarayici.find_element(By.CLASS_NAME, "container")
print(baslik)

baslik.screenshot("./gorseller/baslik.png")
arama_kutusu = tarayici.find_element(By.CSS_SELECTOR, "#araTextBox")
arama_kutusu.send_keys("Asım Baba Pro")
sleep(2)

arama_tus = tarayici.find_element(By.ID, "araButton")
#arama_tus.click()
#sleep(3)

twitter_title = tarayici.find_element(By.NAME, "twitter:title")
print(twitter_title.get_attribute("content"))
okullarimiz = tarayici.find_element(By.LINK_TEXT, "Okullarimiz")
okullarimiz.click()
sleep(2)