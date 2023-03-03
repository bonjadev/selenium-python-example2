import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElement():
    def demo_first_element(self):
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            driver.get("https://apollon.rs")
            driver.maximize_window()
            driver.refresh()
            driver.find_element(By.LINK_TEXT,"ovde").click()
            time.sleep(8)
            driver.close()


demo_first_element = DemoFindElement()
demo_first_element.demo_first_element()

