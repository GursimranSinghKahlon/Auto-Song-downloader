import urllib2
import re
import os
import string
from os.path import basename

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
songurls=songurls[2:]
#print(songurls)

print("####################         Songs on disk:         #########################")
songdd=[]
for root, dirs, files in os.walk('.'):
    for file in files:
        m=os.path.join("", file)
        print(m)
        songdd.append(m)
             

print("")
print("####################         Songs on website:         #########################")
f=0
for songurl in songurls:
	
	urlcontent=urllib2.urlopen(songurl).read()
	#print(urlcontent)
	songurl=re.findall('a .*?href="(.*?)"><img',urlcontent)
	songurl=songurl[1]
	songname=basename(songurl)
	#songname=songurl.split('/')[-1]
	print(songname)
	
	if songname not in songdd:
		f+=1
		print("##############               New song found               ###################")
		print("********************          Downloading           *************************")
		try:
	 
			#print("URL : ")
			#print(songurl)        

			songdata=urllib2.urlopen(songurl).read()
			filname=songname
			output=open(filname,'wb')
			output.write(songdata)
			output.close()
			print("Downloaded")
		except:
			print("Error")
			pass
			
	print("")
print("######                "+ " New Songs Downloaded = "+  str(f) +"                ######")


