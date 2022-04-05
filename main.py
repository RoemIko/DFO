#!/usr/bin/python
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import replace
from email import header
from wsgiref import headers

import requests
import schedule
from bs4 import BeautifulSoup
from requests.api import get


# Skip error, since I'm a lazy developer I didn't add a check for dir exist
def init():
    try:
        os.mkdir("cracked.io")
    except FileExistsError:
        pass


def main():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    url = "https://cracked.io/Forum-Combolists--297" #Normal URL
    urllist = "https://cracked.io/Forum-Combolists--297?page=" #URL you want to collect 10 times

    #Beginning of replaceing string, so it can save it as following output <Domain>.html
    replace_url = url
    replace_url = replace_url.replace("https://","")
    replace_url = replace_url.replace("/","")
    #End
    get_url = requests.get(url, headers=headers)
    soup = BeautifulSoup(get_url.text, 'html.parser')
    with open(r"cracked.io/" + replace_url + ".html", 'w',encoding='utf8') as file:
        file.write(str(soup))
    
    #Loop 10 times through list
    n = 11
    while n > 1:
        n = n - 1 
        #Beginning of replaceing string, so it can save it as following output <Domain>.html
        replace_urllist = urllist + str(n)
        replace_urllist = replace_urllist.replace("https://","")
        replace_urllist = replace_urllist.replace("/","")
        #End
        get_url = requests.get(urllist + str(n), headers=headers)
        soup = BeautifulSoup(get_url.text, 'html.parser')
        with open(r"cracked.io/" + replace_urllist + ".html", 'w',encoding='utf8') as file:
            file.write(str(soup)) #Retrieve html source
    schedule.every().day.at("12:00").do(main) #Schedule every day at 12:00

    # Keep it running until you press ctrl-z
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    init()
    main()
