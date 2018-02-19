import urllib2
import re
import os
import string
from os.path import basename
from urlparse import urlparse
from posixpath import basename,dirname

url='https://wapking.live/top/today.html'      ## give the url here
parse_object=urlparse(url)
dirname=basename(parse_object.path)

if not os.path.exists('TopSongs'):
    os.mkdir("TopSongs")
    os.mkdir("TopSongs/"+"Today")    
os.chdir("TopSongs/Today")

urlcontent=urllib2.urlopen(url).read()
#print(urlcontent)
songurls0=re.findall('a .*?href="(/fileDownload/.*?)"',urlcontent)
#print(songurls0)
songnames=re.findall('a .*?href=".*?</div><div>(.*?)<br/>',urlcontent)
#print(songnames)

songurls=[]
n=0
for i in songurls0:
    xy=i.split('/')
    x=xy[-2]
    songurls.append("/files/download/type/128/id/"+x)
    n+=1


'''for i in songnames:
    print(i)

for i in songurls:
    print(i)'''

print("####################         Songs on disk:         #########################")
songdd=[]
for root, dirs, files in os.walk('.'):
    for file in files:
        m=os.path.join("", file)
        print(m)
        songdd.append(m)
             


#print(songurls)
print("")
print("####################         Songs on website:         #########################")
n=-1
f=0
for songurl in songurls:
    n+=1
    if(re.match(r'.*3',songnames[n],re.L)):
        print(songnames[n])
    if (songnames[n] not in songdd) and re.match(r'.*3',songnames[n],re.L):
        f+=1
        print("####################         New song found         #########################")
        print("####################          Downloading           #########################")
        try:
     
            #print("Final : ")
            #print(songurl)
            
            songurl="https://wapking.live"+songurl
            #print("Final2 : ")
            #print(songurl)
            
            songdata=urllib2.urlopen(songurl).read()
            print(songnames[n])
            filname=basename(songnames[n])
            output=open(filname,'wb')
            output.write(songdata)
            output.close()
            os.remove(filename)


        except:
            pass
print("")
print("##################        "+ " New Songs Downloaded = "+  str(f) +"      #######################")


