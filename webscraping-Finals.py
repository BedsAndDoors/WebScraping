from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

url = 'https://registrar.web.baylor.edu/exams-grading/fall-2022-final-exam-schedule'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')

tables = soup.findAll('table')

finals_table = tables[1]

all_finals = finals_table.findAll('tr')

myclasses_file = open('classes.csv','r')
myclasses = csv.reader(myclasses_file,delimiter=',')

for rec in myclasses:
    day = rec[0]
    time = rec[1]

    for row in all_finals:
        cell = row.findAll('td')
        if cell:
            sch_day = cell[0].text
            sch_time = cell[1].text
            exam_day = cell[2].text
            exam_time = cell[3].text

            if sch_day == day and sch_time == time:
                print(f'Class Day and time: {day} - {time}')
                print(f'Exam day and time : {exam_day} - {exam_time}')
                print()