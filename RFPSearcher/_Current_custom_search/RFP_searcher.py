'''
Date Created : 9/17/2015
TODO
Finish a text parser
Let it download more than ten ( or less )
'''
from search import *
import sys

def text_parser(sites, filters=''):
    for url,heading_type,source_type, pdf_name in sites:
        file_dir = directory+heading_type
        file_name = str(file_dir + pdf_name).strip()

def main():
    try:
        #results published/indexed in the last month and sort by date
        #for dateRestict replace m with w for week or with y for year
        #replace 2 with number you want for more of the previous (y2 = 2 years)
        param = '&sort=date&dateRestrict=m2'
        
        #what you would type in the search box (don't forget spaces where they belong)
        search_query = ('2015 "capital" OR CIP improvement replacement '+
                      'OR upgrade "security system" filetype:pdf -"uk" '+
                      '-"united nations" -"social security"')

        #do the google search and return an instance of the class
        
        
        
    except :
        print "*********Search failed*********"
        sys.exit()
    gs = GoogleSearch(search_query,param)
    print "Search Url : " + gs.search_url + "\n"   
    print "Total Number of Results : " + str(gs.total_num_results)
    print "---------Printing "+ str(len(gs.sites)) + " urls----------"
    num=1
    for url,protocol,dns_name,pdf_name in gs.sites:
        print num
        print "*"*20
        print "Download Url : " +url
        print "Protocol     : " +protocol
        print "DNS Name     : " +dns_name
        print "PDF Name     : " +pdf_name
        num+=1
    #Uncomment below to download the urls it found (It downloads the first 10 by default)
    #Made function to return more urls but have not tested yet (out of searchs)
    ##gs.download()

    
if __name__ == "__main__":
    main()



