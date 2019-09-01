from xpath_soup import xpath_soup
from selenium.webdriver.firefox.options import Options as FirefoxOpt
from selenium import webdriver
from urllib.request import urlretrieve
from bs4 import BeautifulSoup 


import sys
import os 
import time

class instaDown:
    def __init__ (self):
        fp = webdriver.FirefoxProfile("C:\\Users\\SEU_USUARIO_AQUI\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\NOME_DO_PERFIL.default")
        driver_path = os.path.join(os.path.dirname(__file__), r'drivers\\geckodriver.exe')
        log_path = os.path.join(os.path.dirname(__file__), r'geckodriver.log')
        options = FirefoxOpt()
        self.driver = webdriver.Firefox(firefox_options = options, executable_path=driver_path, service_log_path=log_path, firefox_profile = fp)
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        self.StartBot()

    def StartBot(self):
        user_icon_selenium = self.Search_xpath("//span[@class='glyphsSpriteUser__outline__24__grey_9 u-__7']")
        user_icon_selenium.click()
        save_icon_selenium = self.Search_xpath("//div[@class='coreSpriteDesktopProfileSave ']")
        save_icon_selenium.click()
        soup = BeautifulSoup(self.driver.page_source,"html.parser")
        lista_imgs = soup.select('img')
        src_imagens_list = list(map(lambda x: x.attrs['src'],lista_imgs))
        iterator = 0
        for x in src_imagens_list:
            urlretrieve(x, f"image_{iterator}.jpg")
            iterator = iterator +1

    def iterator(self, numero):
        return numero+1

    def Search_xpath(self, xpath):
        xpath_element_selenium = None
        while not xpath_element_selenium:
            xpath_element_selenium = next(iter(self.driver.find_elements_by_xpath(xpath)), None)
        return xpath_element_selenium

if __name__ == "__main__":
    instaDown()