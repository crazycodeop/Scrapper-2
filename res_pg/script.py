import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'res_pg.settings')
django.setup()

import requests
import datetime
from bs4 import BeautifulSoup
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
    URL = "https://www.magicbricks.com/property-for-rent/residential-paying-guest?cityName=" + city_opt

    response = requests.get(URL)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    cards = soup.find_all('div', class_='mb-srp__card')

    posted_by = None
    sharing_type = []
    pg_for = None
    charges = None
    pg_name = None
    link = None
    locality = None
    desc = None
    date_posted = None

    for card in cards:
        pg_for = card.find('span', class_='m-srp-card__info__gender').text

        try:
            link = card.find(attrs={'itemprop': 'url'})
            link = 'https://www.magicbricks.com/' + link.get('content')
        except:
            link = None

        res = requests.get(link)
        res = res.content
        res_soup = BeautifulSoup(res, 'html.parser')

        dep_amt = res_soup.find('div', class_='pg-prop-details__info__grid--value').text.replace('₹', '')

        try: 
            pg_name = card.find('meta', attrs={'itemprop': 'name'})
            pg_name = pg_name.get('content')
        except:
            pg_name = None
        try: 
            desc = card.find('meta', attrs={'itemprop': 'description'})
            desc = desc.get('content')
        except:
            desc = None

        charges = card.find('div', class_='m-srp-card__price').text.replace('₹', '')
        charges = charges.replace('\\n', '')
        charges = charges[0:8] + 'Onwards'

        try: 
            temp = card.find('span', attrs={'class': 'hidden'})
            posted_by = temp.get('data-advname')
            sharing_type = temp.get('data-avail').replace('\\', '')
            locality = temp.get('data-pglocality')
        except:
            pass
        entry=Entries(Id=i, Posted_by=posted_by, PG_for=pg_for, Proptype='PG', Link=link, Owner=pg_name, City=city_opt, Locality=locality, Charges=charges, Description=desc)
        entry.save()