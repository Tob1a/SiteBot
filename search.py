from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
import time

class search():
    def __init__(self,url,OrarioMax,OrarioMin,driver):
        self.url=url
        self.orariomax=OrarioMax
        self.orariomin=OrarioMin
        self.driver=driver


        self.driver.get(self.url)

        
        time.sleep(4)


        elem1 = self.driver.find_element(By.XPATH, '//*[@id="page-body"]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]')
        elem2 = self.driver.find_element(By.XPATH, '//*[@id="page-body"]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]')

        
        ActionChains(self.driver).drag_and_drop_by_offset(elem1, self.orariomin, 0).perform()
        ActionChains(self.driver).drag_and_drop_by_offset(elem2, self.orariomax, 0).perform()
        time.sleep(2)


        self.liberi = self.driver.find_elements(By.XPATH, "//div[@class='col-6 col-lg-8']")