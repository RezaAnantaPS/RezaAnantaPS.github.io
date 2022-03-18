from selenium import webdriver
import simplejson as json

from datetime import datetime
import time

PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.celebritynetworth.com/list/top-100-richest-people-in-the-world/")
data = []
i = 1
for item in driver.find_elements_by_class_name("top_profile"):
    print(item.text)
    for img in item.find_elements_by_tag_name("img"):
        print(img.get_attribute("src"))
        waktu = datetime.now().strftime('%d %B %Y %H:%M:%S')
        data.append(
            {
                "Rank": item.text.split("\n")[1],
                "Name": item.text.replace(" Net Worth","").split("\n")[2],
                "Net_Worth": item.text.split("\n")[3],
                "Biodata": item.text.split("\n")[4],
                "Image" : img.get_attribute("src"),
                "Waktu_Scraping" : waktu
            }
        )
hasil_scraping = open("scrapingSelenium.json","w")
json.dump(data, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.close()
