import time
from datetime import datetime as dt 

host_temp = 'hosts'
host_path=r'C:\Windows\System32\drivers\etc\hosts'
redirect_ipaddress='127.0.0.1'
website_list_to_block = ['facebook.com','www.facebook.com']


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,15) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print('Working Hours..........')
        with open(host_path , 'r+') as file:
            content=file.read()
            #print(content)
            for website in website_list_to_block:
                if website in content:
                    pass
                else:
                    file.write(redirect_ipaddress+"  "+website+'\n')
    else:
        with open(host_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list_to_block):
                    file.write(line)
                file.truncate()    
            
             
        print('Not Working Hours............')    
    time.sleep(5)
