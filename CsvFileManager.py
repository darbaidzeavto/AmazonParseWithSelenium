from selenium.webdriver.common.by import By
import pandas as pd
import os
class CsvFileManager:
    def __init__(self, driver):
        self.driver = driver
    def SaveToCSV(self, FileName, data):
        # Define the directory where you want to save the CSV file
        directory = "ProductCSVFiles"

        # Ensure the directory exists; create it if not
        os.makedirs(directory, exist_ok=True)

        # Construct the full path including the directory
        full_path = os.path.join(directory, FileName)

        # Create a DataFrame and save it to the specified path
        df = pd.DataFrame(data)
        df.to_csv(full_path, index=False)