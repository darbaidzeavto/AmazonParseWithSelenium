from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random
from HomePage import HomePage
from SearchResultPage import SearchResultPage
from ProductAndResult import ProductPage, SaveToCSV
from NavigateBetweenPages import NavigateBetweenPages
# List of Proxy servers
ProxyServerList = ["172.67.70.187:80", "172.67.70.187:80", "192.168.105.127:3128"]
while True:
    ProductName = input("Enter the product name: ")
    data = []
    # Randomly select a proxy server from the list
    ProxyAddress = random.choice(ProxyServerList)
    # Set up the selected proxy
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = ProxyAddress
    proxy.ssl_proxy = ProxyAddress
    # Configure Chrome WebDriver with the proxy
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--proxy-server={ProxyAddress}")
    # Initialize the WebDriver with Chrome options
    driver = webdriver.Chrome(options=chrome_options)
    try:
        # Give the CSV file a unique name          
        CurrentDate = datetime.now().strftime("%Y%m%d")
        FileName = f"{ProductName}_{CurrentDate}"
        # Initialize objects for interacting with different pages and data handling.
        HomePageObj = HomePage(driver)
        SearchResultPageObj = SearchResultPage(driver)
        ProductPageObj = ProductPage(driver)
        NavigatePagesObj = NavigateBetweenPages(driver)
        SaveToCSVObj = SaveToCSV(driver)
        # Navigate and collecting data on the first page 
        HomePageObj.openAmazon()
        HomePageObj.avoidCaptcha()
        time.sleep(3)
        HomePageObj.searchProduct(ProductName)
        time.sleep(3)
        NumberOfPages = SearchResultPageObj.NumberOfPages()
        print(f"Number of available pages: {NumberOfPages}")
        first_element = SearchResultPageObj.goFirstProduct()
        first_element.click()
        data = ProductPageObj.extractDetails(data)
        NavigatePagesObj.goPreviousPage()
        time.sleep(3)  # Wait for the page to load all elements
        # Navigation and data collection on all other pages
        for i in range(1, NumberOfPages):
            NavigatePagesObj.goNextPage()
            time.sleep(3)  # Wait for the page to load all elements
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Wait for the page to load all elements
            product_urls = SearchResultPageObj.productUrls()
            for product_url in product_urls:
                driver.get(product_url)
                time.sleep(3)  # Wait for the page to load all elements
                data = ProductPageObj.extractDetails(data)
            i = i + 1
        driver.close()
        SaveToCSVObj.SaveToCSV(FileName, data)
    except:
        driver.close()
        print ('something unexpected was happend please try again')

