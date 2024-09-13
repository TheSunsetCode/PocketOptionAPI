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
        "email" : ".form-control.form-control_filled",
        "password" : ".form-control.js-f-pswd-input.form-control_filled",
        "submit" : ".btn.btn-green-light",
        "google_login" : ".social-btn.social-btn--gp"
    }):
        self.driver.get(url)
        
        time.sleep(5)

        inp1 = self.driver.find_element(By.CSS_SELECTOR, options['email'])
        inp1.send_keys(username)
        time.sleep(3)