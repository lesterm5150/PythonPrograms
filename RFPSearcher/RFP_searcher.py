'''
Date        : 9/15/2015

Comments:
  Creation of this file with modifications in xgoogle.search functions
  Added second prop to GoogleSearch class and modified what get_Results() returns
'''

import requests, os, sys
from xgoogle.search import GoogleSearch

#create directory to store RFPs
# './folder' - create folder in current folder
directory = './RFPs/'
#directory types
head_types = {'https':'/https//',
             'http':'/http//',
             'Other':'/other//'}
#end types of urls
end_types = {'.gov/':'gov',
             '.edu/':'edu',
             '.com/':'com',
             '.net/':'net',
             '.info/':'info'}

if not os.path.exists(directory):
    os.makedirs(directory)


def filter_sites(result):
  for r in result:
      print r['href']
  sys.exit()
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
    elif 'pdf' in url:
      #find where the url ends in pdf
      end = url.find('pdf')
    else:
      #if it somehow doesn't contain pdf then skip it
     continue
    
    #else we skip the beginning of the returned url
    #(which is 7 chars into the string)
    begin = 7
    label = head_types['Other']
    
    #find the beginning of the url and let us know it is from a certified source
    for key in head_types:
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
          
      
    tmp = res['href'][begin:end+3].strip()#strip white space and add the url to a list
    #for site in sites:
    #  if tmp in site:
    #    continue
    name = url[url.rfind("/")+1:end+3]
    name = name.replace('%','_')
    sites.append((tmp,label,ref,name))
  return sites
  

try:
  #first prop is literal search ( what you would put in the search bar )
  #second prop is added to end of url ( get )
  search_url = '2015 "capital" OR CIP improvement replacement OR upgrade "security system" filetype:pdf -"uk" -"united nations" -"social security"'
  search_url = search_url.replace('"',"%22")
  
  gs = GoogleSearch(search_url)
  gs.results_per_page = 7
  results = gs.get_results()
    
except :
  print "Search failed"

sites = filter_sites(results)
for url,_,_,_ in sites:
    print url
sys.exit()
for url,heading_type,source_type, pdf_name in sites:
  print "Downloading .... " + pdf_name
  file_dir = directory+heading_type
  if not os.path.exists(file_dir):
    os.makedirs(file_dir)
  file_dir +=pdf_name
  file_dir = file_dir.strip()
  print str(file_dir)
  #r = requests.get(sites[0], stream=True)
  try:
    #heads = requests.head(url)
    #size =  heads.headers['content-length']
    q = requests.get(url, stream=True)
    cur_chunk = 0
    #if size > 1000000000:
    #   sys.quit()
    with open(file_dir, 'wb') as f:
          for chunk in q.iter_content(chunk_size=1024):
              #print str(cur_chunk) + ' / ' + str(size)
              #cur_chunk +=1
              if chunk: # filter out keep-alive new chunks                  
                  f.write(chunk)
                  f.flush()
          f.write(q.content)
          
          
  except:
    continue
    try:
      print "Going"
    except:
      print "Gone"
