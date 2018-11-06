import urllib2
import re
import os
import string
from os.path import basename
from tqdm import tqdm
import requests

def download(url,name):
	chunk_size = 1024
	r = requests.get(url, stream = True)
	total_size = int(r.headers['content-length'])
	with open(name, 'wb') as f:
		for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'KB'):
			f.write(data)
			
# Website
url='https://www.djjohal.com/topTracks.php?cat=Single%20Track#gsc.tab=0'
# Make path
if not os.path.exists('songdj'):
    os.mkdir("songdj")
    os.mkdir("songdj/"+"today")    
os.chdir("songdj/today")


site=url
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

url = urllib2.Request(site, headers=hdr)

# Fetch webpage
urlcontent=urllib2.urlopen(url).read()
#print(urlcontent)
songurls=re.findall('<a class="touch"href="(.*?)">',urlcontent)
songurls=songurls[2:-3]
print(songurls)

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
f=0
n=0
for songurl in songurls:
	n+=1
	urls = urllib2.Request(songurl, headers=hdr)
	urlcontent=urllib2.urlopen(urls).read()

	songurl=re.findall('a .*?href="(.*?)"><img',urlcontent)
	print(songurl)
	if(len(songurl)<=1):
		print('Error')
		continue
	songurl=songurl[1]
	songname=basename(songurl)

	print(str(n) + '. ' + str(songname))
	
	if (songname not in songdd):
		f+=1
		print("##############               New song found               ###################")
		print("********************          Downloading           *************************")
		download(songurl, songname)
		print("Downloaded")

			
	print("")
print("######                "+ " New Songs Downloaded = "+  str(f) +"                ######")
