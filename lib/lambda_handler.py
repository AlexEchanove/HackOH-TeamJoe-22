import json
import requests
from bs4 import BeautifulSoup as bs
import time

def lambda_handler(event, context):
    url = "https://recsports.osu.edu/fms/facilities/rpac"
    page = requests.get(url)
    soup = bs(page.content, "html.parser")
    job_elements = soup.find_all("div", class_="c-meter")
    print("test")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from OHI/O!')
    }
