from cgi import test
from urllib import request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

url = 'https://www.webull.com/quote/crypto'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')

title = soup.title

table_rows = soup.findAll('tr')
# Request in case 404 Forbidden error
tablecells = soup.findAll('div',attrs={'class':'table-cell'})

#Reqs:
#Top 5 crypto
#One at a time (Not sure if this means Prof wants user input before displaying different cryptos)
#Display name, symbol, current price, percent change, previous price
#If bitcoin or ethereum fall below (40K btc) or (3K eth) have a text allert

#List Top 5 Part
#BACKGROUND INFO: I used WeBull which does not list the crypto top movers in a organized fashion like it does for stocks
#Therefore I had to gather all the percent changes into a list
#Then I removed all the values EXCEPT the top five stocks from the list
#Then it iterates through the list and checks each crypto to see if it is a top mover 
#If the crypto is a top mover, it goes through the code for the output
#Otherwise it skips that crypto
#Sorry if this is confusing code, I did not realize WeBull didn't organize its cryptos by the biggest movers until I finished the ouput section
#And instead of trying a different site I did this as a solution, which is long and confusing but it does work
#Thanks for reading

p_change = 3
count=0
p_list = []

while count < 58:
    percent = tablecells[p_change].text
    if '-' in percent:
        p_change+=10
        count+=1
    else:
        per_num = percent.replace('%','')
        plus_num = per_num.replace('+','')
        int_num = round(float(plus_num),2)
        p_list.append(int_num)
        p_change+=10
        count+=1

p_list.sort()

while len(p_list) > 5:
    p_list.pop(-0)

name = 1
current_price= 2
p_open = 5
p_change = 3
prev_close = 6
count = 0

print('\nTop Crypto Movers of the Day:\n(in no particular order)\n')

while count < 58:
    percent = tablecells[p_change].text
    per_num = percent.replace('%','')
    if '-' in per_num:
        name+=10
        current_price+=10
        p_change+=10
        p_open+=10
        prev_close+=10
        count+=1
    else:
        plus_num = per_num.replace('+','')
        if float(plus_num) in p_list:
            print(f'---------------------')
            str_name = str(tablecells[name].text)
            no_usd = str_name.replace('USD',' ')
            name_list = no_usd.split(' ')
            ticker = name_list[0]
            if len(name_list) == 3:
                comp_name = name_list[1]+' '+name_list[2]
                print(f'Cyrpto Name:          {comp_name}')
            elif len(name_list) == 2:
                print('Cyrpto Name:         ',name_list[1])
            elif len(name_list) == 4:
                comp_name = name_list[1]+' '+name_list[2]+' '+name_list[3]
                print(f'Cyrpto Name:          {comp_name}')
            print(f'Ticker Symbol:        {ticker[1:]}')
            if ',' in tablecells[current_price].text:
                cp = tablecells[current_price].text
                cpfin = cp.replace(',','')
                print(f'Current Price:        ${cpfin}')
            else:
                if round(float(tablecells[current_price].text),2) != 0:
                    print(f'Current Price:        ${round(float(tablecells[current_price].text),2)}')
                else:
                    print(f'Current Price:        ${round(float(tablecells[current_price].text),3)}')
            if round(float(tablecells[prev_close].text),2) != 0:
                print(f'Previous Day Price:   ${round(float(tablecells[prev_close].text),2)}')
            else:
                print(f'Previous Day Price:   ${round(float(tablecells[prev_close].text),3)}')
            print(f'Percent Change:       {tablecells[p_change].text}')
            print(f'---------------------\n')
            name+=10
            current_price+=10
            p_change+=10
            p_open+=10
            prev_close+=10
            count+=1
        else:
            name+=10
            current_price+=10
            p_change+=10
            p_open+=10
            prev_close+=10
            count+=1

#BTC & ETH TEXT ALERTS
#THIS DOES WORK, FEEL FREE TO SPAM MY NUMBER WITH TEXTS 

accountSID = 'AC236c69cdb975bdeea48058c9b700a4bf'
authToken = '39d0e377d84851721849bf987fa270e7'
from twilio.rest import Client

TwilioNumber = '+16293484743'
myCellPhone = '+18153534197'
client = Client(accountSID,authToken)

count=0
name=1
current_price=2
while count < len(tablecells[0:58]):
    if tablecells[name].text == 'BBTCUSDBitcoin':
        price = tablecells[current_price].text
        no_c = price.replace(',','')
        rounded = round(float(no_c),0)
        no_z = str(rounded).replace('.0','')
        fin_price = int(no_z)
        if fin_price < 40000:
            message = 'ALERT: The price of Bitcoin has dropped below $40,000'
            textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=message)
        current_price+=10
        name+=10
        count+=1
    else:
        current_price+=10
        name+=10
        count+=1

count=0
name=1
current_price=2
while count < len(tablecells[0:58]):
    if tablecells[name].text == 'EETHUSDEthereum':
        price = tablecells[current_price].text
        no_c = price.replace(',','')
        rounded = round(float(no_c),0)
        no_z = str(rounded).replace('.0','')
        fin_price = int(no_z)
        if fin_price < 3000:
            message = 'ALERT: The price of Ethereum has dropped below $3,000'
            textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=message)
        current_price+=10
        name+=10
        count+=1
    else:
        current_price+=10
        name+=10
        count+=1
        
