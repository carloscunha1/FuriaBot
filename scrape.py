from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

# Set up the WebDriver
service = Service()  
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Example usage

  url = 'https://books.toscrape.com/'
  driver.get(url)