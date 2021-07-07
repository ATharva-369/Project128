#this program uses bs4 and requests to fetch data from a wikipedia article about bright stars
#it stores it as a csv file using the csv module
from bs4 import BeautifulSoup
# import time
import csv
import requests
import pandas as pd

#creating a variable for our URL
URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# #requesting data
r = requests.get(URL)

# #storing our data as a html file using a function
# def save_html(html, path):
#     with open(path, 'wb') as f:
#         f.write(html)
        
# #calling the function        
# save_html(r.content, 'wiki_scrap.html')

#creating a headers list ('we will just be getting two rows of stars with their names, distances in light-years, masses and their radiuses')
headers = ['name','distance','mass','radius']
planet_data = [] #creating a planet_data list to store our final data
for i in range(0,1): #we will only be running this one time as our table is a one whole table, the for loop isn;t necessary, but just clarifies the code to use when you have multiple tables
    soup = BeautifulSoup(r.text, 'html.parser') # creating a BeautifulSoup object, bs4 is a parser which, parses or makes the data compatible to work with
    for table_tag in soup.find_all('table'):
        trtags = table_tag.find_all("tr")
        temp = []
        for i,tag in enumerate(trtags):
            if i == 0 or i == 5 or i ==7 or i ==8:
                for cells in tag.find_all('td'):
                    try:
                        temp.append(cells.contents)    
                    except:    
                        temp.append('')   
        planet_data.append(temp)
print(planet_data)