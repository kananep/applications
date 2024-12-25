#program that extracts data from real estate sites

import requests
from bs4 import BeautifulSoup
import pandas as pd

print('Enter Website Address:')
page_url = str(input())

for page in range(28403880,28403885,1):
    print(page_url+str(page))
    r = requests.get(page_url+str(page))
    content = r.content
    soup = BeautifulSoup(content,'html.parser')
    data = soup.find_all('div',{'data-brand-cd':'REN'})


lst = []

for item in data:
        
        dictionary = {}
        dictionary['Address'] = item.find('div',{'class':'property-address'}).text.replace(' ','').strip()    
            
        dictionary['Locality'] = item.find('div',{'class':'property-city'}).text.replace(' ','').strip()
        dictionary['Beds'] = item.find('div',{'class':'property-beds'}).find('strong').text
        try:
            dictionary['Baths'] = item.find('div',{'class':'property-baths'}).find('strong').text
        except:
                pass  
        try: 
            dictionary['Square Feet'] = item.find('div',{'class':'property-sqft'}).find('strong').text
        except:
                pass     
        dictionary['Price'] = item.find('a',{'class':'listing-price'}).text.replace('\n','').replace(' ','')
        

        lst.append(dictionary)


lst = pd.DataFrame(lst)
lst.to_csv('DataInformation.csv')


