from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.ie.service import Service

class Login:
    def __init__(self) -> None:
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.driver = Chrome(service=self.service)
    def login(self, username, password, url: str = "https://pocketoption.com/en/login", is_login_with_google: bool = False):
        self.driver.get(url)