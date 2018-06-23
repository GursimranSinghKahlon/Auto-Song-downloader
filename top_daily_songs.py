
from tqdm import tqdm
import requests
import urllib
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
url='http://mymp3song.me/topdownload/today'      ## give the url here

# Make path
if not os.path.exists('TopSongs'):
    os.mkdir("TopSongs")
    os.mkdir("TopSongs/"+"Today")    
os.chdir("TopSongs/Today")

#Fetch songs online
urlcontent=urllib.urlopen(url).read()
#print(urlcontent)
songurls=re.findall('a .*?href="/filedownload/(.*?)/',urlcontent)
songnames=re.findall('a .*?href=".*?</div><div>(.*?)<br/>',urlcontent)
#print(songnames)



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
			songurl="http://mymp3song.me/files/download/type/128/id/" + songurl
			print(songurl)
			download(songurl,songnames[n])
			print("Download complete!")
			f.close()
        except:	
			print("Error")
			pass
print("")
print("##################        "+ " New Songs Downloaded = "+  str(t) +"      #######################")


