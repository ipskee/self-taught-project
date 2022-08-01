# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 01:52:22 2022

@author: hkbbo
"""
import requests
from bs4 import BeautifulSoup
import csv

def main():    
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    
    title = []
    results = soup.find_all('td', class_='titleColumn')
    for item in results:
        title.append(item.get_text(strip=True))
    
    rating = []
    results = soup.find_all('td', class_='ratingColumn imdbRating')
    for item in results:
        rating.append(item.get_text(strip=True))
    
    link = []
    results = soup.find_all('td', class_='titleColumn')
    for item in results:
        poo = item.a.get('href')
        link_text = "https://www.imdb.com" + poo
        link.append(link_text)
    final =[]
    for i in range(0,250):
        temp = {}
        temp["Title"] = title[i]
        temp["Rating"] = rating[i]
        temp["Link"] = link[i]
        final.append(temp) 
        
    fields = ["Title", "Link", "Rating"]
    
    with open('in_hausIMDB111.csv','w') as file:
        writer = csv.DictWriter(file, fields)
        writer.writeheader()
        writer.writerows(final)
        
main()        