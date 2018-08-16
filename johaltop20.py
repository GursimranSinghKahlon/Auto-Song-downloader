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
url='https://mr-johal.com/topTracks.php?cat=Single%20Track#gsc.tab=0'

# Make path
if not os.path.exists('songdj'):
    os.mkdir("songdj")
    os.mkdir("songdj/"+"today")    
os.chdir("songdj/today")

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
	urlcontent=urllib2.urlopen(songurl).read()
	#print(urlcontent)
	songurl=re.findall('a .*?href="(.*?)"><img',urlcontent)
	#print(songurl)
	if(len(songurl)<=1):
		print('Error')
		continue
	songurl=songurl[1]
	songname=basename(songurl)
	#songname=songurl.split('/')[-1]
	print(str(n) + '. ' + str(songname))
	if (songname not in songdd):
		f+=1
		print("##############               New song found               ###################")
		print("********************          Downloading           *************************")
		try:
			
			#print("URL : ")
			#print(songurl)        
			download(songurl, songname)
			print("Downloaded")
		except:
			print("Error")
			pass
			
	print("")
print("######                "+ " New Songs Downloaded = "+  str(f) +"                ######")
