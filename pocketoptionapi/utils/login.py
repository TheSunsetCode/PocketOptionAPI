from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
import time

class Login:
    def __init__(self) -> None:
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.driver = Chrome(service=self.service)

    def login(self, username, password, url: str = "https://pocketoption.com/en/login", is_login_with_google: bool = False, options = {
        "email" : "/html/body/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div[1]/input",
        "password" : "/html/body/div[2]/div[2]/div/div/div/div[2]/form/div[2]/div[2]/input",
        "submit" : ".btn.btn-green-light",
        "google_login" : ".social-btn.social-btn--gp"
    }):
        self.driver.get(url)
        
        time.sleep(5)

        #email
        inp1 = self.driver.find_element(By.XPATH, options['email'])
        inp1.send_keys(username)
        time.sleep(1)

        #password
        inp1 = self.driver.find_element(By.XPATH, options['password'])
        inp1.send_keys(username)
        time.sleep(3)

