from xpath_soup import xpath_soup
from selenium import webdriver
from urllib.request import urlretrieve
from bs4 import BeautifulSoup 

import os 
import time

class instaDown:
    def __init__ (self):
        self.StartBrowser()

    def StartBrowser(self):
        username = "USERNAME"
        password = "PASSWORD"
        
        driver_path = os.path.join(os.path.dirname(__file__), r'drivers\\geckodriver.exe')
        log_path = os.path.join(os.path.dirname(__file__), r'geckodriver.log')
        driver = webdriver.Firefox(executable_path=driver_path, log_path=log_path)
        driver.maximize_window()
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source,"html.parser")
        element_a_list = soup.select('a')
        element = next(iter(list(filter(lambda x: "Conecte-se" in x.text, element_a_list))), None)
        element = driver.find_element_by_xpath(xpath_soup(element))
        element.click()
        time.sleep(5)
        username = driver.find_element_by_css_selector(f"[name$='username']")
        password = driver.find_element_by_css_selector(f"[name$='password']")
        username.send_keys("USERNAME")
        password.send_keys("PASSWORD")
        soup = BeautifulSoup(driver.page_source,"html.parser")
        buttons_loggin_list = soup.select('button')
        btn_element = next(iter(list(filter(lambda x: "Entrar" in x.text, buttons_loggin_list))), None)
        btn_element_s = driver.find_element_by_xpath(xpath_soup(btn_element))
        btn_element_s.click()
        time.sleep(5)
        user_icon_s = driver.find_element_by_xpath("//span[@class='glyphsSpriteUser__outline__24__grey_9 u-__7']")
        user_icon_s.click()
        time.sleep(5)
        save_icon_s = driver.find_element_by_xpath("//div[@class='coreSpriteDesktopProfileSave ']")
        save_icon_s.click()
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source,"html.parser")
        lista_imgs = soup.select('img')
        src_imagens_list = list(map(lambda x: x.attrs['src'],lista_imgs))
        iterator = 0
        for x in src_imagens_list:
            urlretrieve(x, f"image_{iterator}.jpg")
            iterator = iterator +1
        print(btn_element)

    def iterator(self, numero):
        return numero+1


if __name__ == "__main__":
    instaDown()