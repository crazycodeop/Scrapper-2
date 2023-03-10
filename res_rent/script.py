import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'res_rent.settings')
django.setup()

import requests
import datetime
import nums_from_string
from bs4 import BeautifulSoup as bs
import requests
from myapi.models import Entries

today = datetime.datetime.today().strftime ('%Y-%m-%d')
def get_date_posted(ago_count):
  Previous_Date = datetime.datetime.today() - datetime.timedelta(days=ago_count)
  previous_d_for = Previous_Date.strftime ('%d/%m/%Y')
  return previous_d_for

cities=['Mumbai', 'Gurgaon','Noida','Ghaziabad','Greater-Noida','Bangalore','Pune','Hyderabad','Kolkata','Chennai',
        'New-Delhi','Ahmedabad','Navi-Mumbai','Thane','Faridabad','Bhubaneswar','Bokaro-Steel-City','Vijayawada','Vrindavan', 'Bhopal',
        'Gorakhpur','Jamshedpur','Agra','Allahabad','Jodhpur''Aurangabad','Jaipur','Mangalore','Nagpur','Guntur','Navsari','Palghar','Salem','Haridwar','Durgapur',
        'Madurai','Manipal','Patna','Ranchi','Raipur','Sonipat','Kottayam','Kozhikode','Thrissur','Tirupati','Trivandrum','Trichy','Udaipur','Vapi','Varanasi',
        'Vadodara','Visakhapatnam','Surat','Kanpur','Kochi','Mysore','Goa','Bhiwadi','Lucknow','Nashik','Guwahati','Chandigarh','Indore','Coimbatore','Dehradun']

i=0

for city_opt in cities:
    URL = "https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName="+city_opt+"&language=en"
    for pgNo in range(0, 11):

        URL = URL+"&page="+str(pgNo)
        response = requests.get(URL)
        response = response.content
        soup = bs(response, 'html.parser')
        cards = soup.find_all('div', class_='mb-srp__card')

        locality = 'Null'
        furnishing = 'Null'
        carpet_area = 'Null'
        facing = 'Null'
        floor = 'Null'
        tenant = 'Null'
        car_parking = 'Null'
        society = 'Null'
        desc = 'Null'
        date_posted = 'Null'

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
            childs = card.find('div', class_='mb-srp__card__summary__list')
            description = card.find('div', class_='mb-srp__card--desc')
            try: 
                desc = description.find('p').text.replace('"', '')
            except:
                desc = "Null"
            rent = card.find('div', class_='mb-srp__card__price--amount').text.replace('???', '')
            for elem in childs.contents:
                try:
                    if elem.get('data-summary') == 'facing':
                        facing = elem.text.replace('facing', '')
                except:
                    facing= 'Null'
                try:
                    if elem.get('data-summary') == 'tenent-preffered':
                        tenant = elem.text.replace('Tenant Preferred', '')
                except:
                    tenant= 'Null'
                try:
                    if elem.get('data-summary') == 'floor':
                        floor = elem.text.replace('Floor', '')
                except:
                    floor= 'Null'
                try:
                    if elem.get('data-summary') == 'society':
                        society = elem.text.replace('Society', '')
                except:
                    society= 'Null'
                try:    
                    if elem.get('data-summary') == 'furnishing':
                        furnishing = elem.text.replace('Furnishing', '')  
                except:
                    furnishing = 'Null'
                try: 
                    if elem.get('data-summary') == 'parking':
                        car_parking = elem.text.replace('Car Parking', '')
                except:
                    car_parking = 'Null'
                try:
                    if elem.get('data-summary') == 'carpet-area':
                        carpet_area = elem.text.replace('Carpet Area', '')
                except:
                    carpet_area= 'Null'
            entry=Entries(Id=i, Date_Posted=date_posted, Proptype='rent', Link=link, Owner=owner, BHK=bhk, Locality=locality, City=city_opt, Rent=rent, Carpet_Area=carpet_area, Furnishing=furnishing, Facing=facing, Tenant=tenant, Floor=floor, Description=desc)
            entry.save()
            i=i+1