import requests

r = requests.get('https://www.zillow.com/homes/for_sale/pmf,pf_pt/house,mobile,land_type/1-_baths/0-120000_price/0-459_mp/1742400-_lot/globalrelevanceex_sort/40.636883,-90.249939,36.824676,-96.15509_rect/7_zm/')

print(r.content)