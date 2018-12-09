
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 17:02:01 2017

@author: Talha.Iftikhar
"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html
import pandas as pd
from scrapy.http.request import Request
import re
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class QuotesSpider(CrawlSpider):
   name = "invisalign"
   allowed_domains = ['https://www.invisalign.com']
   start_urls = [
        'https://www.invisalign.com/find-a-doctor?zip=11718&searchType=adult',
    ]    
    #rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="dlPagerBottom"]/a[6]',)),callback="", follow= True),)
    
   def __init__(self):
        drivergeo = webdriver.Firefox(executable_path=r'D:\geckodriver.exe')
        self.driver = drivergeo        
            
   def parse(self, response):
        zips=pd.read_csv('ziplist/zip8_100.csv')
        zipscolumn=zips["Zip Code"]
        for zipcode in zipscolumn:
            link='https://www.invisalign.com/find-a-doctor?zip='+str(zipcode)+'&searchType=adult'
            #req=Request(url=link,callback=self.parse_details)
            #yield req
            self.driver.get(link)
            var=True
            item={}
            first=self.driver.find_elements_by_xpath('//div[@class="doctor-desktop fix"]')
            for row in first:
                    try:
                        name=row.find_element_by_xpath('div[2]/h3').text
                    except NoSuchElementException:
                        name="Missing"
                    try:
                        specialty=row.find_element_by_xpath('div[2]/div[1]').text
                    except NoSuchElementException:
                        specialty="Missing"
                    try:
                        address=row.find_element_by_xpath('div[2]/div[2]').text
                    except NoSuchElementException:
                        address="Missing"
                    try:
                        phone=row.find_element_by_xpath('div[2]/div[3]').text
                    except NoSuchElementException:
                        phone="Missing"
                    try:
                        website=row.find_element_by_xpath('div[2]/div[4]/a').text
                    except NoSuchElementException:
                        website="Missing"
                    try:
                        rating=row.find_element_by_xpath('div[3]/a[1]').text
                    except NoSuchElementException:
                        rating="Missing"
                    try:
                        IsItero2=row.find_element_by_xpath('div[3]/a[2]').text
                    except NoSuchElementException:
                        IsItero2="Missing"
                    try:    
                        hasitero=row.find_element_by_xpath('div[3]/a[3]').text
                    except NoSuchElementException:
                        hasitero="Missing"
                    
                
            ###############################################################   
                
                    item["Name"]=name
                    item["Specialty"]=specialty
                    item["Address"]=address
                    item["Phone"]=phone
                    item["website"]=website
                    item["rating"]=rating
                    item["IsITERO"]=hasitero
                    item["IsITERO2"]=IsItero2
                    item["ZipCode"]=str(zipcode)
                    yield item
            try:
                page=self.driver.find_element_by_xpath('//div[@class="dlPagerBottom"]/a[4]')
                page.click()
                first=self.driver.find_elements_by_xpath('//div[@class="doctor-desktop fix"]')
                for row in first:
                    try:
                        name=row.find_element_by_xpath('div[2]/h3').text
                    except NoSuchElementException:
                            name="Missing"
                    try:
                        specialty=row.find_element_by_xpath('div[2]/div[1]').text
                    except NoSuchElementException:
                        specialty="Missing"
                    try:
                        address=row.find_element_by_xpath('div[2]/div[2]').text
                    except NoSuchElementException:
                        address="Missing"
                    try:
                        phone=row.find_element_by_xpath('div[2]/div[3]').text
                    except NoSuchElementException:
                        phone="Missing"
                    try:
                        website=row.find_element_by_xpath('div[2]/div[4]/a').text
                    except NoSuchElementException:
                        website="Missing"
                    try:
                        rating=row.find_element_by_xpath('div[3]/a[1]').text
                    except NoSuchElementException:
                        rating="Missing"
                    try:
                        IsItero2=row.find_element_by_xpath('div[3]/a[2]').text
                    except NoSuchElementException:
                        IsItero2="Missing"
                    try:    
                        hasitero=row.find_element_by_xpath('div[3]/a[3]').text
                    except NoSuchElementException:
                        hasitero="Missing"
            
            ###############################################################   
                
                    item["Name"]=name
                    item["Specialty"]=specialty
                    item["Address"]=address
                    item["Phone"]=phone
                    item["website"]=website
                    item["rating"]=rating
                    item["IsITERO"]=hasitero
                    item["IsITERO2"]=IsItero2
                    item["ZipCode"]=str(zipcode)
                    yield item
            except NoSuchElementException:
                    var=False
        
            while var:
                try:
                    page=self.driver.find_element_by_xpath('//div[@class="dlPagerBottom"]/a[6]')
                    page.click()
                    second=self.driver.find_elements_by_xpath('//div[@class="doctor-desktop fix"]')
                    for row in second:
                        try:
                            name=row.find_element_by_xpath('div[2]/h3').text
                        except NoSuchElementException:
                            name="Missing"
                        try:
                            specialty=row.find_element_by_xpath('div[2]/div[1]').text
                        except NoSuchElementException:
                            specialty="Missing"
                        try:
                            address=row.find_element_by_xpath('div[2]/div[2]').text
                        except NoSuchElementException:
                            address="Missing"
                        try:
                            phone=row.find_element_by_xpath('div[2]/div[3]').text
                        except NoSuchElementException:
                            phone="Missing"
                        try:
                            website=row.find_element_by_xpath('div[2]/div[4]/a').text
                        except NoSuchElementException:
                            website="Missing"
                        try:
                            rating=row.find_element_by_xpath('div[3]/a[1]').text
                        except NoSuchElementException:
                            rating="Missing"
                        try:
                            IsItero2=row.find_element_by_xpath('div[3]/a[2]').text
                        except NoSuchElementException:
                            IsItero2="Missing"
                        try:    
                            hasitero=row.find_element_by_xpath('div[3]/a[3]').text
                        except NoSuchElementException:
                            hasitero="Missing"
                     
                        item["Name"]=name
                        item["Specialty"]=specialty
                        item["Address"]=address
                        item["Phone"]=phone
                        item["website"]=website
                        item["rating"]=rating
                        item["IsITERO"]=hasitero
                        item["IsITERO2"]=IsItero2
                        item["ZipCode"]=str(zipcode)
                        yield item                               
                except NoSuchElementException:
                    break
                
                
  
    
    
        '''
    def parse_start_url(self,response):
        
            link="https://www.invisalign.com/find-a-doctor?zip=11718&searchType=adult"
            req=Request(url=link,callback=self.parse_details,headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36","Referer":"https://findadentist.ada.org/search-results?address=11718"})
            yield req 
            
    def parse_details(self, response):
        for row in response.xpath('//div[@class="name-details"]'):
                   item={}
                   
                   #count = re.findall('var FirstName.+?(\d+)',response.body)[0]
                   item["Name"]=row.xpath('h3/text()').re('"FullName":"(.+)"')
                   yield item
                   
             #   item["Address"]=row.xpath('div[1]/p[2]/a/text()').extract()
                #specialty=str(row.xpath('div[2]/p[1]/text()').extract_first())
                #spstrip= specialty.strip().split(':')[1]
              #  item["Specialty"]=specialty.split(':')[-1]
               # item["Phone"]=row.xpath('div[2]/p[2]/a/text()').extract_first()
                #item["Map url"]=row.xpath('div[1]/p[2]/a/@href').extract_first()
              #  item["City"]=row.xpath('td/table/tbody/tr[1]/td[2]/p/small/span/text()').extract_first()
               # item["Date"]=row.xpath('td/table/tbody/tr[2]/td[1]/p/text()').extract_first()
               
                #'author': quote.css('small.author::text').extract_first(),
                #'tags': quote.css('div.tags a.tag::text').extract(),
      '''      
############################################33
#    def parse(self, response):
 #       page = response.url.split("/")[-2]
  #      filename = 'quotes-%s.html' % page
   #     with open(filename, 'wb') as f:
    #        f.write(response.body)
     #   self.log('Saved file %s' % filename)
     
     #rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="link pageNextPrev {page:2}"]',)),\
     #             callback="parse_page", follow= True),)
#zip_codesfile=pd.read_csv('us_postal_codes.csv')
#zip_codesfile.info()
#zip_codes=zip_codesfile["Zip Code"]
#for row in zip_codes:
 #   print(row)
        


