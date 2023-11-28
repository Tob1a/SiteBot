from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 

class search():
    def __init__(self,url,OrarioMax,OrarioMin,driver):
        self.url=url
        self.orariomax=OrarioMax
        self.orariomin=OrarioMin
        self.driver=driver


        driver = driver.get(self.url)


        #aspetta finche' la sbarra non e' cliccabile
        wait= WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'px-2 vue-slider vue-slider-ltr')))


        liberi = driver.find_element(By.TAG_NAME, 'row align-items-center')

        return liberi