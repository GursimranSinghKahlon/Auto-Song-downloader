
from tqdm import tqdm
import requests
import urllib2
import re
import os
import string

def download(url,name):
	chunk_size = 1024
	r = requests.get(url, stream = True)
	total_size = int(r.headers['content-length'])
	with open(name, 'wb') as f:
		for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'KB'):
			f.write(data)

# Website
url='http://mymp3song.site/topdownload/today'      ## give the url here
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
url = urllib2.Request(url, headers=hdr)


# Make path
if not os.path.exists('TopSongs'):
    os.mkdir("TopSongs")
    os.mkdir("TopSongs/"+"Today")    
os.chdir("TopSongs/Today")

#Fetch songs online
urlcontent=urllib2.urlopen(url).read()
songurls=re.findall('a .*?href="/filedownload/(.*?)/',urlcontent)
songnames=re.findall('a .*?href=".*?</div><div>(.*?)<br/>',urlcontent)



print("####################         Songs on disk:         #########################")
songdd=[]
n=0
for root, dirs, files in os.walk('.'):
    for file in files:
	    if(file.endswith('.mp3')):
		    m=os.path.join("", file)
		    print(str(n+1) + ". " + str(m))
		    n+=1
		    songdd.append(m)
             

print("")
print("####################         Songs on website:         #########################")
n=-1
t=0
for songurl in songurls:
    n+=1
    print(str(n+1) +". "+ str(songnames[n]))
    if (songnames[n] not in songdd) and re.match(r'.*mp3',songnames[n],re.L):
        t+=1
        print("##############               New song found               ###################")
        print("********************          Downloading           *************************")
        try:
			
			songurl="http://mymp3song.site/files/download/type/128/id/" + songurl
			print(songurl)
			download(songurl,songnames[n])
			print("Download complete!")
        except:	
			print("Error")
			pass
print("")
print("##################        "+ " New Songs Downloaded = "+  str(t) +"      #######################")


