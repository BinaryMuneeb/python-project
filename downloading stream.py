import requests
from tqdm import tqdm
url='https://download-cdn.jetbrains.com/idea/ideaIC-2023.1.3.exe'
r=requests.get(url,stream=True)
totalbytes=int(r.headers['Content-length'])
bytesreicved=0
progress=tqdm(total=totalbytes,unit='iB',unit_scale=True)
with open ('winrar.exe','wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        progress.update(128)
        f.write(chunk)
        bytesreicved+=128
progress.close()