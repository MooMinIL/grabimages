## imports 

import urllib2
import re
import os
from os.path import basename
from urlparse import urlsplit
from urlparse import urlparse
from posixpath import basename,dirname
 
## function that processes url, if there are any spaces it replaces with '%20' ##
 
def process_url(raw_url):
 if ' ' not in raw_url[-1]:
     raw_url=raw_url.replace(' ','%20')
     return raw_url
 elif ' ' in raw_url[-1]:
     raw_url=raw_url[:-1]
     raw_url=raw_url.replace(' ','%20')
     return raw_url

    
root_url='https://brandonsanderson.com/books/mistborn/the-final-empire/the-final-empire-art-gallery/nggallery/page/' ## give the url here, should end with '/pages/'
pg_idx = 1
print("Parsing all images from sanderson's page: " + root_url)
EOP = False ## end of pages marker
while not EOP:
    url = root_url+format(pg_idx,'1d')
    print('Trying page #' + format(pg_idx,'1d') + '...')
    pg_idx = pg_idx+1
    
    parse_object = urlparse(url)
    dirname = basename(parse_object.path)
    if not os.path.exists('/Users/yairmaimon/Downloads/images/mist'):
        os.mkdir("/Users/yairmaimon/Downloads/images/mist")

    ## os.mkdir("/Users/yairmaimon/Downloads/images/"+dirname)
    os.chdir("/Users/yairmaimon/Downloads/images/mist/")


    urlcontent=urllib2.urlopen(url).read()
    print('Finding all the images in page...')
    imgurls=re.findall('data-src="(.*?)"',urlcontent)
    idx  = 0
    EOP = True
    for imgurl in imgurls:
        EOP = False
        idx = idx+1
        print('Getting image ' + format(idx,'1d') + ' out of ' + format(len(imgurls),'1d'))
        try:
            imgurl=process_url(imgurl)
            imgdata=urllib2.urlopen(imgurl).read()
            filname=basename(urlsplit(imgurl)[2])
            output=open(dirname+'_'+format(idx,'02d')+'_'+filname,'wb')
            output.write(imgdata)
            output.close()
            os.remove(filename)
        except:
            pass
    if EOP:
        print('Nothing Found!')
       
print('Finished!')
