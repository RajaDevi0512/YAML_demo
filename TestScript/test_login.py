from Utilities.yaml_func import YAML_Reader
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

class Test_Sauce_YAML:
    def test_sauce_login(self):

        file_name = "C:\\Users\\rajap\\OneDrive\\Desktop\\Devi\\01_Python\\10_Selenium\\01_Practice\\10_PYYAML\\TestData\\config.yaml"

        yaml_reader = YAML_Reader(file_name)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        try:
            driver.maximize_window()
            driver.get(yaml_reader.reader()['url'])
            driver.implicitly_wait(10)


            driver.find_element(by=By.ID, value= yaml_reader.reader()['username_locator']).send_keys(yaml_reader.reader()['username'])
            driver.find_element(by=By.ID, value= yaml_reader.reader()['password_locator']).send_keys(yaml_reader.reader()['password'])
            driver.find_element(by=By.ID, value= yaml_reader.reader()['loginbutton_locator']).click()
        
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR : ", error)


        finally:
            driver.quit()
