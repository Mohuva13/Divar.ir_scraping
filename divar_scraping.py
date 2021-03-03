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

for y in year:
    y = str(y)
    yr = re.findall(r"<span class=\"vehicle-card-year font-size-1\">(.*)</span>", y)
    yr = str(yr)
    yr = yr.replace("['", "")
    yr = yr.replace("']", "")
    year_list.append(yr)

for p in price:
    p = str(p)
    pr = re.findall(r"<h4 class=\"heading-3 margin-y-1 font-weight-bold\" data-qa=\"Heading\" data-test=\"vehicleCardPricingBlockPrice\">(.*)</h4>", p)
    pr = str(pr)
    pr = pr.replace("['", "")
    pr = pr.replace("']", "")
    price_list.append(pr)
for parantez in range(len(price_list)):
    try:
        price_list.remove('[]')
    except:
        pass


for m in mil:
    m = str(m)
    mr = re.findall(r"<div\ class=\"font-size-1\ text-truncate\" data-test=\"vehicleMileage\">.*</circle></svg>(.*)</div>", m)
    mr = str(mr)
    mr = mr.replace("<!-- -->","")
    mr = mr.replace("['", "")
    mr = mr.replace("']", "")
    mil_list.append(mr)

for mo in model:
    mo = str(mo)
    mor = re.findall(r"<span\ class=\"vehicle-header-make-model\ text-truncate\">(.*)</span>", mo)
    mor = str(mor)
    mor = mor.replace("<!-- --> <!-- -->", "  ")
    mor = mor.replace("['", "")
    mor = mor.replace("']", "")
    model_list.append(mor)
