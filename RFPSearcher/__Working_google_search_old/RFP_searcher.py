'''
Date        : 9/17/2015


TODO
put functions in GoogleSearch class for filtering
'''

import requests, os, sys
import bs4
from search import *
import urllib

# './folder' - create folder in current folder
directory = './RFPs/'
#directory types
head_types = {'http':'/http//',
             'https':'/https//',    
             'Other':'/other//'}
#end types of urls
end_types = {'.gov/':'gov',
             '.edu/':'edu',
             '.com/':'com',
             '.net/':'net',
             '.info/':'info'}

#create directory to store RFPs
if not os.path.exists(directory):
    os.makedirs(directory)


def filter_sites(results):

  #return url, url label, url type, and name
  label = ''
  ref = ''
  name = ''
  sites = []
  for res in results: #filter through results getting just the urls
    url = res['href']
    
    if 'webcache.googleusercontent' in url:
      #we skip references to usercontent because an url was returned of the google result
      #that contained a reference to the previous url and can be skipped
      continue
    elif '.pdf' in url:
      #find where the url ends in pdf
      end = url.find('.pdf')
    else:
      #if it somehow doesn't contain pdf then skip it
     continue
    
    #skip the beginning of the returned url
    #(which is 7 chars into the string as a BeautifulSoup standard)
    begin = 7
    label = head_types['Other']
    
    #find the beginning of the url and let us know it is from a certified source
    for key in reversed(sorted(head_types)):
        if key in url:
            begin = url.find(key)
            label = head_types[key]
            break
    if label == head_types['Other']:
        continue
    
    ref = 'none'
    
    #find the url source
    for key in end_types:
        if key in url:
            ref = end_types[key]
            break
     #replace res['href'] with url   
    tmp = res['href'][begin:end+4].strip()#strip white space and add the url to a list
    name = url[url.rfind("/")+1:end+4]
    name = name.replace('%','_')
    if (tmp,label,ref,name) not in sites:
      sites.append((tmp,label,ref,name))
  return sites

def download(sites):
  for url,heading_type,source_type, pdf_name in sites:
    file_dir = directory+heading_type
    if not os.path.exists(file_dir):
      os.makedirs(file_dir)
    file_dir +=pdf_name
    file_dir = file_dir.strip()
    print "Downloading : " + pdf_name
    try:
      try:
        heads = requests.head(url)
        size =  int(heads.headers['content-length'])
      except:
        print "*********Couldn't get size*********"
      q = requests.get(url, stream=True)
      cur_chunk = 0
      if size > 50000000: #if larger than 50MB then do not download
        print " " *10 + str(pdf_name) + ' is too large, cannot download'
        print " " *10 + str(size) + '\n'
        continue
      print "     size : " + str(size)
      print "           -> " +str(file_dir)
      with open(file_dir, 'wb') as f:
          for chunk in q.iter_content(chunk_size=1024):
              ##print str(cur_chunk) + ' / ' + str(size)
              ##cur_chunk +=1024
              if chunk: # filter out keep-alive new chunks                  
                  f.write(chunk)
                  f.flush()
          f.write(q.content)       
    except:
      continue

def text_parser(sites, filters=''):
    for url,heading_type,source_type, pdf_name in sites:
        file_dir = directory+heading_type
        file_name = str(file_dir + pdf_name).strip()

def main():
    try:
        param = '&tbs=qdr:m'#results published/indexed in the last month
        search_url = '2015 "capital" OR CIP improvement replacement OR upgrade "security system" filetype:pdf -"uk" -"united nations" -"social security"'
        #do the google search and return the results
        gs = GoogleSearch(search_url,param)
        results = gs.get_results()
        
    except :
        print "*********Search failed*********"
        print results
    #filter results for urls
    sites = filter_sites(results)
    
    #download the urls
    download(sites)

    text_parser(sites)
    
if __name__ == "__main__":
    main()

