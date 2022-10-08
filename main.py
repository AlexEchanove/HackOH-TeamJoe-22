import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

urlpage = 'https://recsports.osu.edu/fms/facilities/rpac'
print(urlpage)
print ("Anything?")

#open Firefox
driver = webdriver.Firefox()

#open web page
driver.get(urlpage)

# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(10)


results = driver.find_elements(By.XPATH, "//*[@id=\"content\"]/div/div/section[1]/div/div/div/div/div/div[2]/div[4]/div")

print("MAde it ehERHE")
for result in results:
    result_text = result.text
    print(result_text)

driver.quit()