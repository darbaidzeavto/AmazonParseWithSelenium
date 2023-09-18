from selenium.webdriver.common.by import By
class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver
    # Click first product on the first page 
    def goFirstProduct(self):
        try:
            first_element = self.driver.find_element(By.XPATH, "//a[@class='a-link-normal s-no-outline']")
            return first_element
        except:
            print ("invalid search queries please try again")
            self.driver.close()
    # Take all products URL from the page   
    def productUrls(self):
            try:
                product_links = self.driver.find_elements(By.XPATH, "//a[@class='a-link-normal s-no-outline']")
                product_urls = []
                for link in product_links:
                    product_url = link.get_attribute("href")
                    product_urls.append(product_url)
                return product_urls
            except:
                print ("there is no products on this page ")
    # Take number of pages 
    def NumberOfPages(self):
        pagination = self.driver.find_element(By.CLASS_NAME, 's-pagination-container')
        PageElements = pagination.find_elements(By.CLASS_NAME, 's-pagination-item')
        NumberOfPages = len(PageElements) 
        return NumberOfPages
