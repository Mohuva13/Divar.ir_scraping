import mysql.connector
import re
from bs4 import BeautifulSoup
import urllib.request

def try_req(the_page):
    try:
        req = urllib.request.Request(f'https://www.truecar.com/used-cars-for-sale/listings/{brand_input}/')
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
    except:
        req = urllib.request.Request(f'https://www.truecar.com/used-cars-for-sale/listings/{brand_input}/')
        with urllib.request.urlopen(req) as response:
            the_page = response.read()

try:
    brand_input = input("Enter brand name from Truecar : ")
    brand_input = brand_input.lower()
    try:
        brand_input = brand_input.replace(" ","-")
    except:
        pass
    req = urllib.request.Request(f'https://www.truecar.com/used-cars-for-sale/listings/{brand_input}/')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    soup = BeautifulSoup(the_page, 'html.parser')

except:
    try_req(the_page)
    soup = BeautifulSoup(the_page, 'html.parser')
	
year = soup.find_all(attrs={'class':'vehicle-card-year font-size-1'})
price = soup.find_all('h4')
mil = soup.find_all(attrs={'data-test':'vehicleMileage'})
model = soup.find_all(attrs={'class':'vehicle-header-make-model text-truncate'})
year_list = []
price_list = []
mil_list = []
model_list = []