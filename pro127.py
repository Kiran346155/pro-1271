from webbrowser import BaseBrowser
from wsgiref import headers
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd


browser=webdriver.Chrome("C:/Users/venky/OneDrive/Desktop/visual studio code files/class-127/chromedriver.exe")
browser.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")

time.sleep(10)

planets_data=[]

def scrape():
    for i in range(0, 1):
        print(f'Scrapping page {i+1} ...')

       
        soup = BeautifulSoup(browser.page_source, "html.parser")
        print(soup)
        
        for tr_tag in soup.find_all("tr"):
            td_tags = tr_tag.find_all("td")



            temp_list = []

            for index, td_tag in enumerate(td_tags):

                if index == 1:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                elif(index>1): 
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
                    

            planets_data.append(temp_list)

        
        

scrape()
headers=["NAME","Bayer designiation","Distance","Spectral class","mass","Radius","Luminosity"]

df=pd.DataFrame(planets_data,columns=headers)
df.to_csv("stars.csv")
