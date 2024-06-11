import requests
url='https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-622.exe'
r=requests.get(url)
fp=open ('winrar.exe','wb')
fp.write(r.content)
fp.close()