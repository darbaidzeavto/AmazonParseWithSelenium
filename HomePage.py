from amazoncaptcha import AmazonCaptcha
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class HomePage:
    def __init__(self, driver):
        self.driver = driver
    # Open amazon in chrome
    def openAmazon(self):
        self.driver.get('https://www.amazon.com/errors/validateCaptcha')
    # Avoiding Amazon Captcha
    def avoidCaptcha(self):
        captcha = AmazonCaptcha.fromdriver(self.driver)
        solution = captcha.solve()
        self.driver.find_element(by=By.ID, value='captchacharacters').send_keys(solution, Keys.ENTER)
    # Search product on amazon.com
    def searchProduct(self, productName):
        self.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(productName, Keys.ENTER)