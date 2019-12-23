from requests import get
from os import system
from bs4 import BeautifulSoup,Tag

url = 'https://python.org/ftp/python/'
bs = BeautifulSoup(get(url).text,'html.parser')

vlookf = input('Enter Python Version to Verify Download: ')
flag = 0
print('Verifing Version...')
for a in bs.findAll('a'):
    if vlookf+'/' in a.contents:
        print('Version '+vlookf+' Available')
        flag = 1

if flag == 1:
    print('Downloading Python '+vlookf+' with Google Chrome')
    system('start chrome "'+url+vlookf+'/python-'+vlookf+'.exe"')

else:
    print('Version not available...')
    system('start chrome "error.html"')
