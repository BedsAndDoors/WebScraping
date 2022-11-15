
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

movie_rows = soup.findAll('tr')

for x in range(1,6):
    td = movie_rows[x].findAll('td')
    rank = td[0].text
    movie_name = td[1].text
    theater = td[6].text.replace(',','')
    gross = int(td[7].text.replace(',','').replace('$',''))
    dis = td[9].text
    avg=gross/int(theater)

    print(f'Rank: {rank}')
    print(f'Movie: {movie_name}')
    print(f'Total Gross: ${gross:,.2f}')
    print(f'Distributor: {dis}')
    print(f'Average per Theater: {avg:,.2f}')
    print('\n\n')