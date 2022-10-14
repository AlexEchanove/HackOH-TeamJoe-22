import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pyttsx3


urlpage = 'https://recsports.osu.edu/fms/facilities/rpac'
print(urlpage)
print ("Anything?")

#open Firefox
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
driver = webdriver.Firefox(firefox_options=fireFoxOptions)

#open web page
driver.get(urlpage)

# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(1)

results_list = driver.find_elements(By.XPATH, "//*[@id=\"content\"]/div/div/section[1]/div/div/div/div/div/div[2]/div[4]/div")[0].text.split("\n")[1::2]
driver.quit()

dict = {}
i = 0
while i < len(results_list):
    dict[results_list[i]] = results_list[i+1]
    i += 2

#print(dict)
engine = pyttsx3.init()
engine.setProperty('rate', 50)


for entry in list(dict.keys()):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate + 75)
    engine.say(entry)
    engine.runAndWait()
    
    engine.say(dict[entry])
    engine.runAndWait()

