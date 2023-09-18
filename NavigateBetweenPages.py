from selenium.webdriver.common.by import By
class NavigateBetweenPages:
    def __init__(self, driver):
        self.driver = driver
    # Go to the Previous Page
    def goPreviousPage(self):
        self.driver.back()
    # Go To the Next Page
    def goNextPage(self):
        self.driver.find_element(By.CLASS_NAME, "s-pagination-next").click()