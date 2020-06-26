'''
Date        : 9/17/2015
'''



import requests
import math
import os


class GoogleSearch():
    #base url with my api key
    base_url = 'https://www.googleapis.com/customsearch/v1?key=?
    #protocol types
    protocols = {
             'http':'/http//',
             'https':'/https//',    
             'Other':'/other//'}
    #entity types
    dns_names = {
             '.gov/':'U.S. Government',
             '.edu/':'U.S. Higher Education',
             '.com/':'Commercial',
             '.net/':'Network',
             '.info/':'Information',
             '.org/':'Organization',
             '.us/':'United States',
             '.mil/':'U.S. Military'}
    
    #initialization of the class
    def __init__(self, query, params='' ,num_results=10):
        self.query = query.replace(" ","+")
        self.params = params
        self.num_results = int(num_results)
        self.search_url = self.format_url()
        self.results = self.get_results()
        self.sites = self.filter_sites()
        self.total_num_results = int(self.get_num_results())
        
        if(self.num_results > 10):
            num = 11
            while(num<=self.num_results and num <= self.total_num_results):
                num+=10
                try:
                    self.sites += self.filter_sites(self.get_results('&start='+str(num)))
                except:
                    break
                        
        self.downloads = []

    def format_url(self):
        #format url
        search_url = requests.utils.quote(self.query,safe="+")
        search_url += self.params
        return GoogleSearch.base_url+search_url
        
    def get_results(self,param=''):
        results = self._get_site(param).json()
        #print results
        
        if 'error' in results.values():
            err = results['error']
            if err['code']==403:
                print "Too many searches for the day"
            else:
                print "Something unexpected happened"
                print "Error Code : " + str(err['code'])
        
        return results
    
    def _get_site(self,_param=''):
        return requests.get(self.search_url+_param)
    
    def get_num_results(self):
        info = self.results['searchInformation']
        return info['totalResults']
    
    def filter_sites(self,extras=''):
        label = ''
        ref = ''
        name = ''
        sites = []
        if extras != '':
            results = extras
        else:
            results = self.results
            
        for res in results['items']: #filter through results getting just the urls
            url = res['link'].lower()

            if '.pdf' in url:
              #find where the url ends in pdf
              end = url.find('.pdf')
            else:
              #if it somehow doesn't contain pdf then skip it
             continue

            begin = 0
            label = GoogleSearch.protocols['Other']

            #find the beginning of the url and let us know
            #what protcol is used to retrieve
            for key in reversed(sorted(GoogleSearch.protocols)):
                if key in url:
                    begin = url.find(key)
                    label = key
                    break
            if label == GoogleSearch.protocols['Other']:
                continue

            ref = 'none'

            #find the url entity (.gov or .com or ...)
            for key in GoogleSearch.dns_names:
                if key in url:
                    ref = GoogleSearch.dns_names[key]
                    break
                
            #strip white space and add the url to a list
            tmp_url = url[begin:end+4].strip()
            name = url[url.rfind("/")+1:end+4]
            name = requests.utils.unquote(name)
            name = name.replace(' ','_')

            #if it somehow is already there, do not add again
            if (tmp_url,label,ref,name) not in sites:
              sites.append((tmp_url,label,ref,name))
        return sites

    def download(self):
        # './folder' - create folder in current folder
        directory = './RFPs/'
        
        #create directory to store RFPs
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        sites = []
        if len(self.downloads)==0:
            sites = self.sites
        else:
            #this will be used for specific downloads or if we want more than the first ten
            #not in use yet
            sites = self.downloads

        for url,protocol,entity, pdf_name in sites:
            file_dir = directory+GoogleSearch.protocols[protocol]
            #create directory based on the protocol the site uses
            if not os.path.exists(file_dir):
              os.makedirs(file_dir)
            file_dir +=pdf_name
            file_dir = file_dir.strip()
            
            #See if we already have the pdf
            if os.path.exists(file_dir):
                print "*****File already in path*****"
                continue
            
            print "Downloading : " + pdf_name
            try:
              try:
                #retrieve size of file
                #could do this for all urls before and pull metadata
                heads = requests.head(url)
                size =  int(heads.headers['content-length'])
              except:
                print "*********Couldn't get size*********"
              q = requests.get(url, stream=True)
              cur_chunk = 0
              if size > 100000000: #if larger than 100MB then do not download
                print " " *10 + str(pdf_name) + ' is too large, cannot download'
                print " " *10 + str(size) + '\n'
                continue
            
              print "     size : " + str(size)
              print "           -> " +str(file_dir)
              with open(file_dir, 'wb') as f:
                  for chunk in q.iter_content(chunk_size=1024):
                      #could use below code to keep track of download progress
                      ##print str(cur_chunk) + ' / ' + str(size)
                      ##cur_chunk +=1024
                      if chunk: # filter out keep-alive new chunks                  
                          f.write(chunk)
                          f.flush()
                  f.write(q.content)       
            except:
              continue
