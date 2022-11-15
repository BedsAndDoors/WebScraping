# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')

title = soup.title

table_rows = soup.findAll('tr')

state_worst_death = ''
state_best_death = ''
high_death_ratio = 0.0
low_death_ratio = 100.0

state_best_test = ''
state_worst_test = ''
high_test_ratio = 0.0
low_test_ratio = 100.0


for row in table_rows[2:52]:
    td = row.findAll('td')
    state = td[1].text
    tot_cases = int(td[2].text.replace(',',''))
    tot_death = int(td[4].text.replace(',',''))
    tot_test = int(td[10].text.replace(',',''))
    population = int(td[12].text.replace(',',''))
    death_rate = round((tot_death/tot_cases)*100,2)
    test_rate = round((tot_test/population)*100,2)
    print(state,'\n',death_rate,'\n',test_rate,'\n')

    if death_rate > high_death_ratio:
        state_worst_death = state
        high_death_ratio = death_rate

    if death_rate < low_death_ratio:
        state_best_death = state
        low_death_ratio = test_rate

    if test_rate > high_test_ratio:
        state_best_test = state
        high_test_ratio = test_rate

    if test_rate < low_test_ratio:
        state_worst_test = state
        low_test_ratio = test_rate

print(f'State with the worst death rate: {state_worst_death}')
print(f'Death Rate: ', {high_death_ratio},'%\n')
print(f'State with the best death rate : {state_best_death}')
print(f'Death Ratio: ', {low_death_ratio},'%\n')
print(f'State with the worst test ratio: {state_worst_test}')
print(f'Test Ratio: ', {low_test_ratio},'%\n')
print(f'State with the best test ratio : {state_best_test}')
print(f'Test Ratio: ',{high_test_ratio},'%\n')


