from selenium.webdriver.common.by import By
import pandas as pd
import os
class ProductPage:
    def __init__(self, driver):
        self.driver = driver
    # Parse product page 
    def extractDetails(self, data):
        # Take product name if it is avalable
        try:
            ProductNameElement = self.driver.find_element(By.XPATH, '//*[@id="productTitle"]')
            ProductName = ProductNameElement.text
        except:
            ProductName = "Product name currently unavalable"
        # Take product price if it is avalable 
        try:    
            PriceElement = self.driver.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/span[1]')
            PriceText = PriceElement.text
            MergeDollarsAndCents = PriceText.split('\n')
            ProductPrice = MergeDollarsAndCents[0] + '.' + MergeDollarsAndCents[1]
        except:
            ProductPrice = "Product price currently unavalable"
        # Take product rating if it is avalable
        try:
            ProductRatingElement = self.driver.find_element(By.XPATH, '//*[@id="acrPopover"]/span[1]/a/span')
            ProductRating = ProductRatingElement.text
        except:
            ProductRating = 'this product has no rating '
        data.append({
            "Name": ProductName,
            "Price": ProductPrice,
            "Rating": ProductRating
        })
        return data
