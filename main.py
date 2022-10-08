import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from gtts import gTTS
from playsound import playsound

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
time.sleep(1)

results_list = driver.find_elements(By.XPATH, "//*[@id=\"content\"]/div/div/section[1]/div/div/div/div/div/div[2]/div[4]/div")[0].text.split("\n")[1::2]
driver.quit()

dict = {}
i = 0
while i < len(results_list):
    dict[results_list[i]] = results_list[i+1]
    i += 2

#print(dict)
language = 'en'

for entry in list(dict.keys()):
    myobj = gTTS(text=entry, lang=language, slow=False)
    myobj.save("sounds.mp3")
    playsound("sounds.mp3")
    
    myobj = gTTS(text=dict[entry], lang=language, slow=False)
    myobj.save("sounds.mp3")
    playsound("sounds.mp3")

