import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comm_lease.settings')
django.setup()

import requests
import datetime
import nums_from_string
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import requests
from myapi.models import Entries

today = datetime.datetime.today().strftime ('%Y-%m-%d')
def get_date_posted(ago_count):
  Previous_Date = datetime.datetime.today() - datetime.timedelta(days=ago_count)
  previous_d_for = Previous_Date.strftime ('%d/%m/%Y')
  return previous_d_for

data = []
cities=['Mumbai']

i=0

for city_opt in cities:
    URL ="https://www.magicbricks.com/property-for-rent/commercial-real-estate?proptype=Commercial-Office-Space,Office-ITPark-SEZ,Commercial-Shop,Commercial-Showroom&cityName="+city_opt+"&language=en"
    for pgNo in range(0, 4):
        URL = URL+"&page="+str(pgNo)
        response = requests.get(URL)
        response = response.content
        soup = bs(response, 'html.parser')
        cards = soup.find_all('div', class_='mb-srp__card')

        prop_age = "Null"
        water = "Null"
        carpet_area = "Null"
        ready_state = "Null"
        furnishing = "Null"
        washroom = "Null"
        parking = "Null"
        pantry = "Null"
        overlooking = "Null"
        facing = "Null"
        locality = "Null"
        per_sqft = "Null"
        desc = "Null"
        date_posted = "Null"

        for card in cards:
            try:
                posted_date = card.find(class_="mb-srp__card__photo__fig--post").text
                if 'today' in posted_date or 'Today' in posted_date:
                    date_posted = get_date_posted(0)
                elif 'ago' in posted_date:
                    ago_date_count = int(nums_from_string.get_nums(posted_date)[0])
                    if 'days' in posted_date:
                        date_posted = get_date_posted(ago_date_count)
                    elif 'weeks' in posted_date:
                        date_posted = get_date_posted((ago_date_count*7))
                    else:
                        date_posted = get_date_posted((ago_date_count*30))
                elif 'yesterday' in posted_date or 'Yesterday' in posted_date:
                    date_posted = get_date_posted(1)
                else:
                    date_posted = posted_date.replace('Posted: ','')
            except:
                posted_date = "Null"
            try: 
                link = card.find('a', class_='mb-srp__card__society--name')['href']
            except:
                link = "Null"
            try: 
                owner = card.find('div', class_='mb-srp__card__ads--name').text
            except:
                owner = "Null"
            bhks = card.find('h2', class_='mb-srp__card--title').text
            prop_locality = bhks.split(', ')
            bhk = prop_locality[0][0:5]
            del prop_locality[0]
            try:
                locality = prop_locality[0]
            except:
                locality = city_opt
            childs = card.find_all('div', class_='mb-srp__card__summary-commercial__list--item')
            description = card.find('div', class_='mb-srp__card--desc')
            try: 
                desc = description.find('p').text.replace('"', '')
            except:
                desc = "Null"
            price = card.find('div', class_='mb-srp__card__price--amount').text.replace('₹', '')
            try: 
                per_sqft = card.find('div', class_='mb-srp__card__price--size').text.replace('₹', '')
            except:
                per_sqft = "Null"
            for elem in childs:

                try:
                    if 'Carpet Area' in elem.text:
                        carpet_area = elem.text.replace('Carpet Area', '')
                except:
                    carpet_area = "Null"

                try:
                    if 'Overlooking' in elem.text:
                        overlooking = elem.text.replace('Overlooking', '')
                except:
                    overlooking = "Null"

                try:
                    if 'Furnishing Status' in elem.text:
                        furnishing = elem.text.replace('Furnishing Status', '')
                except:
                    furnishing = "Null"

                try:
                    if 'Parking' in elem.text:
                        parking = elem.text.replace('Parking', '')
                except:
                    parking = "Null"

                try:
                    if 'Pantry' in elem.text:
                        pantry = elem.text.replace('Pantry', '')
                except:
                    pantry = "Null"

                try:
                    if 'Facing' in elem.text:
                        facing = elem.text.replace('Facing', '')
                except:
                    facing = "Null"

                try:
                    if 'Washroom' in elem.text:
                        washroom = elem.text.replace('Washroom', '')
                except:
                    washroom = "Null"

                try:
                    if 'Water Availability' in elem.text:
                        water = elem.text.replace('Water Availability', '')
                except:
                    water = "Null"

                try:
                    if 'Property Age' in elem.text:
                        prop_age = elem.text.replace('Property Age', '')
                except:
                    prop_age = "Null"
            entry=Entries(Id=i, Date_Posted=date_posted, Proptype='Commercial Sale', Link=link, Retailer=owner, BHK=bhk, Locality=locality, City=city_opt, Price=price, Carpet_Area=carpet_area, Washroom=washroom, Facing=facing, Water_Availability=water, Property_Age=prop_age, Price_Sqft=per_sqft, Parking=parking, Pantry=pantry, Description=desc)
            entry.save()
            i=i+1
    
   
   