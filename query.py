from requests import get
from os import system
from bs4 import BeautifulSoup,Tag
import asyncio

vlookf = input('Enter Python Version to Verify Download: ')

url = 'https://python.org/ftp/python/'
bs = BeautifulSoup(get(url).text,'html.parser')

flag = 0
print('Verifing Version...')
for a in bs.findAll('a'):
    if vlookf+'/' in a.contents:
        print('Version '+vlookf+' Available')
        flag = 1

if flag == 1:
    print('Getting installer for Python '+vlookf+'...')
    import urllib.request
    def dl(version):
        global url
        path = url+version+'/python-'+version+'.exe'
        urllib.request.urlretrieve(path,f"python-{version}.exe")
        print("Downloaded from URL: "+path)
    dl(vlookf)

else:
    print('Version not available...')
    system('start chrome "error.html"')
