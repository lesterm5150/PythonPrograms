'''

Date        : 9/17/2015

'''

import requests
from bs4 import *
import math

class GoogleSearch():
    base_url = 'https://google.com/search?q='
    def __init__(self, query,params='' ,num_results=10):
        self.query = query
        self.params = params
        self.num_results = int(num_results)

    def get_results(self):
        global base_url
        search_url = self.query.replace(" ","+")
        search_url = search_url.replace('"','%22')
        search_url = search_url.replace(':','%3A')
        search_url += self.params
        full_url = GoogleSearch.base_url+search_url
        print full_url
        result = requests.get(full_url)
        beaut =  BeautifulSoup(result.content, "html.parser")
        div_search = beaut.find('div', id='search')
        bound= div_search.findAll('a', href=True)
        
        #what if there are not more than 10 ( or asked for ) results available ( check boundaries )
        if self.num_results > 10:
            num_results = math.ceil(self.num_results)
            num = 10
            while(num < num_results+1):
                extend = '&start=' + str(num)
                result = requests.get(full_url+extend)
                beaut =  BeautifulSoup(result.content, "html.parser")
                div_search = beaut.find('div', id='search')
                bound+= div_search.findAll('a', href=True)
                num+=10
            
        
        return bound