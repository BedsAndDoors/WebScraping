import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


chapter = random.randint(1,21)

if chapter < 10:
    chapter = str(chapter).zfill(2)
elif chapter >= 10:
    chapter = str(chapter)

webpage = 'https://ebible.org/asv/JHN'+chapter+'.htm'

print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,'html.parser')
verses = soup.findAll('div',class_='main')

for verse in verses:
    verse_list = verse.text.split('.')

my_verse = random.choice(verse_list[:-5])

message = 'Chapter: ' + chapter + ' Verse:' + my_verse
print(message)

accountSID = 'AC236c69cdb975bdeea48058c9b700a4bf'
authToken = '262a37061e46f1485b21523e409bacba'
from twilio.rest import Client

TwilioNumber = '+16293484743'
myCellPhone = '+18153534197'
client = Client(accountSID,authToken)
textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,body=message)
