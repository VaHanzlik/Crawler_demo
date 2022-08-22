# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 2022

@author: vhanzlik
"""

import requests
from ..helpers.log import setup_logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import os 

import logging
logger = logging.getLogger(__name__) ## module logger


class Crawler_bot ():
    """The main crawler class

    """
    def __init__(self, in_url:str, max_depth:int = 3):
    
        self.max_depth = max_depth
        self.discovered = []
        self.to_visit = [{"url" : in_url,"depth" : 0, "parent_url" : ""}]
        

    def __check_if_visited(self, new_url:str)->bool:
        """Private method for checking visited URLS list.

        Args:
            new_url (string): String with url which should be checked if it was visited.

        Returns:
            bool: Returns True if the checked address is in the visited urls list.
        """
        found = any([new_url == sublist.get("url") for sublist in self.discovered])
        
        return found


    def __checkout_url(self, url:str, in_depth:int)->dict:
        """Downloads all not visited URL links from a webpage.

        Args:
            url (str): Url which should be searched 
            in_depth (int): Parameter for checking if the new pages reached the
                            allowed depth from the first page.

        Returns:
            list: List of dicts with information about the new pages. 
        """
        depth = in_depth+1
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        list_of_urls_to_add = []
        for link in soup.find_all('a'):
            link_url = link.get('href',"0")
            if link_url[-1] == "/":
                link_url = urljoin(url, link_url)
                list_of_urls_to_add.append(link_url)
        list_of_urls_to_add = set(list_of_urls_to_add)
        for page in list_of_urls_to_add:
            if page[0:5].upper() =="HTTPS":
                if not(self.__check_if_visited(new_url = page)):
                    logger.info(f"Adding {page} in the to_visit list ")
                    self.to_visit.append({"url" : page,
                                            "depth" : depth,
                                            "parent_url" : url})
        
    def crawl(self):
        """The main crawling function for inspecting web pages
        
        Args:
            None

        Returns:
            list: the discovered attribute
        
        """

        logger.info("Start Crawling:")

        try:
            while self.to_visit:
                url_dict = self.to_visit.pop(0)
                
                self.discovered.append(url_dict)
                url_depth = url_dict.get("depth")
                if int(url_depth) <= int(self.max_depth):
                    self.__checkout_url(url_dict.get("url"), url_dict.get("depth"))
            
            logger.info(f"Crawling ended. {str(len(self.discovered))}")
        except Exception as ex:
            logger.error(f"Something wrong happened: {ex}")
    
    def dump_data(self, save_path:str):
        """Saves the results in new JSON file.

        Args:
            save_path (str): path for the result file location
        """

        if not os.path.exists("data"):
            os.makedirs("data")

        save_path = os.path.join("data",save_path)
        logger.info(f"Dumping the result in: {save_path}")
        json_data = json.dumps(self.discovered, indent=4)
        logger.info(f"Results have been successfully saved.")
        with open(save_path, "w+") as outfile:
            outfile.write(json_data)


if __name__ == '__main__':

    from crawler_src.helpers.log import logger_init
    logger_init() ## init root logger
    logger = logging.getLogger(__name__) ## module logger
    logger.info("Running extractor.py as main")
    



