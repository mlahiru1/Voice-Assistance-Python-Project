from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class infow():
    def __init__(self):
        self.service = Service('C:/chromedriver/chromedriver.exe')
        self.options = Options()
        # Specify the path to the Chrome browser binary if it's not in the default location
        self.options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")

assist = infow()
assist.get_info("hello")
