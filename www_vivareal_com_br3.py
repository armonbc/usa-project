import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
import re
import os

class WwwVivarealCom3BrSpider(CrawlSpider):
    name = 'www_vivareal_com_br3'
    allowed_domains = ['glue-api.vivareal.com']
    headers = {
        'X-domain':'www.vivareal.com.br'
    }
    start_urls=[]
    current_json={}
    url_1= 'https://glue-api.vivareal.com/v2/listings?bedrooms='
    url_2=20
    url_3='&business=SALE&facets=amenities&unitTypes=&unitSubTypes=&unitTypesV3=&usageTypes=&listingType=USED&parentId=null&categoryPage=RESULT&includeFields=search(result(listings(listing(displayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2CunitTypes%2CnonActivationReason%2CpropertyType%2CunitSubTypes%2Cid%2Cportal%2CparkingSpaces%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2Cbedrooms%2CpricingInfos%2CshowPrice%2Cstatus%2CadvertiserContact%2CvideoTourLink%2CwhatsappNumber%2Cstamps)%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones)%2Cmedias%2CaccountLink%2Clink))%2CtotalCount)%2Cpage%2CseasonalCampaigns%2CfullUriFragments%2Cnearby(search(result(listings(listing(displayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2CunitTypes%2CnonActivationReason%2CpropertyType%2CunitSubTypes%2Cid%2Cportal%2CparkingSpaces%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2Cbedrooms%2CpricingInfos%2CshowPrice%2Cstatus%2CadvertiserContact%2CvideoTourLink%2CwhatsappNumber%2Cstamps)%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones)%2Cmedias%2CaccountLink%2Clink))%2CtotalCount))%2Cexpansion(search(result(listings(listing(displayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2CunitTypes%2CnonActivationReason%2CpropertyType%2CunitSubTypes%2Cid%2Cportal%2CparkingSpaces%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2Cbedrooms%2CpricingInfos%2CshowPrice%2Cstatus%2CadvertiserContact%2CvideoTourLink%2CwhatsappNumber%2Cstamps)%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones)%2Cmedias%2CaccountLink%2Clink))%2CtotalCount))%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones%2Cphones)%2Cfacets%2Cdevelopments(search(result(listings(listing(displayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2CunitTypes%2CnonActivationReason%2CpropertyType%2CunitSubTypes%2Cid%2Cportal%2CparkingSpaces%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2Cbedrooms%2CpricingInfos%2CshowPrice%2Cstatus%2CadvertiserContact%2CvideoTourLink%2CwhatsappNumber%2Cstamps)%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones)%2Cmedias%2CaccountLink%2Clink))%2CtotalCount))%2Cowners(search(result(listings(listing(displayAddressType%2Camenities%2CusableAreas%2CconstructionStatus%2ClistingType%2Cdescription%2Ctitle%2CunitTypes%2CnonActivationReason%2CpropertyType%2CunitSubTypes%2Cid%2Cportal%2CparkingSpaces%2Caddress%2Csuites%2CpublicationType%2CexternalId%2Cbathrooms%2CusageTypes%2CtotalAreas%2CadvertiserId%2Cbedrooms%2CpricingInfos%2CshowPrice%2Cstatus%2CadvertiserContact%2CvideoTourLink%2CwhatsappNumber%2Cstamps)%2Caccount(id%2Cname%2ClogoUrl%2ClicenseNumber%2CshowAddress%2ClegacyVivarealId%2Cphones)%2Cmedias%2CaccountLink%2Clink))%2CtotalCount))&size='
    url_4=1
    url_5='&from='
    url_6=0
    url_7='&q=&developmentsSize=5&__vt=mtc%3Adefault&levels=LANDING&ref=&pointRadius=&isPOIQuery='
    start_urls.append(url_1+str(url_2)+url_3+str(url_4)+url_5+str(url_6)+url_7)

    def start_requests(self):
        self.logger.debug("\n\n"+self.start_requests.__name__+"\nLoading...."+"\n\n")
        for url in self.start_urls:
            yield Request(url,headers=self.headers, callback=self.parse_all)

    def parse_all(self,response):
        self.current_json = response.json()
        #self.logger.debug(response.xpath('.//h1[@class="h1-search-text"]'))
        self.logger.debug("\n\n Parsing items...\n\n"+response.url+"\n\n")
        if "search" in self.current_json:
            self.total_count=self.current_json['search']['totalCount']
            infos = self.current_json['search']['result']['listings'][0]
            print('\n\n')
            self.logger.debug(self.url_6)
            yield{
                'Full Address': self.sanitize(infos['link']['data']['state']+", "+infos['link']['data']['city']),
                'Short Address': self.sanitize(infos['link']['data']['state']+", "+infos['link']['data']['city']),
                'Bedroom Qty': self.sanitize(infos['listing']['bedrooms']),
                'Price': self.sanitize(infos['listing']['pricingInfos'][0]['price']),
                'Lot Size (sq m)': self.sanitize(infos['listing']['totalAreas']),
                'Interior Area / Living Area size(sq.m.)': self.sanitize(infos['listing']['totalAreas']),
                'Type': self.sanitize(infos['listing']['unitTypes']),
                'Link': self.sanitize('https://www.vivareal.com.br'+infos['link']['href']),
                'Property Description': self.sanitize(infos['listing']['description'])
            }
            print('Next is ...\n\n')
            if self.url_6 <= self.total_count and self.current_json['search']['result']['listings']:
                self.url_6+=1
                next_page = self.url_1+str(self.url_2)+self.url_3+str(self.url_4)+self.url_5+str(self.url_6)+self.url_7
                yield scrapy.Request(next_page, headers=self.headers, callback=self.parse_all)
            elif self.url_2<=200 and not self.current_json['search']['result']['listings']:
                self.url_6=1
                self.url_2+=1
                next_page = self.url_1+str(self.url_2)+self.url_3+str(self.url_4)+self.url_5+str(self.url_6)+self.url_7
                yield scrapy.Request(next_page, headers=self.headers, callback=self.parse_all)

    #Function name to prevent returning NoneType
    def sanitize(self,value):
        if not value or None:
            return "Not Found"
        if isinstance(value, list):
           if value:
           	return value[0]
        return value

'''
["Instruction 1 of 1"]
** 1.) To scrape, use the following command:

scrapy crawl 'www_vivareal_com_br3' -s DOWNLOAD_DELAY=2 -s URLLENGTH_LIMIT=5000 -O 'www_vivareal_com_br3.csv'

** Note:
* You CAN change the csv filename from 'www_vivareal_com_br3.csv' to 'anyname.csv'
* You CANNOT CHANGE the spider name 'www_vivareal_com_br3' not unless you edit the same in the 'name' variable above
'''
