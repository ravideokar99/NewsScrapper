from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
import requests
import pandas as pd
import pickle
import pycurl 
from OracleConnection import ConnectToOracle
import pycurl
from io import BytesIO 
from dateutil.parser import parse
from flask import Flask,jsonify,request

conn=ConnectToOracle()

b_obj = BytesIO() 
crl = pycurl.Curl() 
my_url='https://economictimes.indiatimes.com/tech/technology'
# Set URL value
crl.setopt(crl.URL, my_url)

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters) 
get_body = b_obj.getvalue()

# Decode the bytes stored in get_body to HTML and print the result 
# print('Output of GET request:\n%s' % get_body.decode('utf8'))

b_obj = BytesIO() 
crl = pycurl.Curl() 
my_url2='https://economictimes.indiatimes.com/news/politics-nation'
# Set URL value
crl.setopt(crl.URL, my_url2)

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters) 
get_body2 = b_obj.getvalue()


# Decode the bytes stored in get_body to HTML and print the result 
# print('Output of GET request:\n%s' % get_body2.decode('utf8'))

b_obj = BytesIO() 
crl = pycurl.Curl() 
my_url3='https://economictimes.indiatimes.com/industry/auto/cars-uvs/articlelist/64829336.cms'
# Set URL value
crl.setopt(crl.URL, my_url3)

# Write bytes that are utf-8 encoded
crl.setopt(crl.WRITEDATA, b_obj)

# Perform a file transfer 
crl.perform() 

# End curl session
crl.close()

# Get the content stored in the BytesIO object (in byte characters) 
get_body3 = b_obj.getvalue()

# Decode the bytes stored in get_body to HTML and print the result 
# print('Output of GET request:\n%s' % get_body2.decode('utf8'))
#tech
page_soup=BeautifulSoup(get_body,"html.parser")
containers = page_soup.findAll("div",{"class":"story-box clearfix"})

#politics
page_soup2=BeautifulSoup(get_body2,"html.parser")
containers2= page_soup2.findAll("div",{"class":"botplData flt"})

#automobiles
page_soup3=BeautifulSoup(get_body3,"html.parser")
containers3 = page_soup3.findAll("div",{"class":"eachStory"})

conn.drop_table('NEWS')
conn.drop_table('NEWS_CATEGORY')
conn.create_table('CREATE TABLE NEWS(NEWS_ID NUMBER NOT NULL PRIMARY KEY,NEWS_CATEGORY_ID NUMBER,NEWS_TITLE VARCHAR2(1000),NEWS_DESC VARCHAR2(3000),NEWS_DATE VARCHAR2(100), NEWS_LINK VARCHAR2(1000))')
conn.create_table('CREATE TABLE NEWS_CATEGORY(CATEGORY_ID NUMBER, NEWS_CATEGORY VARCHAR2(100))')
count=0
for container in containers:

    cat_container = page_soup.findAll("h1",{"class":"title2"})
    cat= cat_container[0].text.split(" ")[0]
    
    title_container=container.findAll("div",{"class":"desc"})
    title=title_container[0].a["title"].replace("\'","")
    
    arcticle_date_container=container.findAll("time",{"class":"date-format"})
    arcticle_date=arcticle_date_container[0]["data-time"].replace(",","")
    dt = parse(arcticle_date)
    arc_dt=dt.strftime('%d-%m-%Y %H:%M:%S')
    
    desc_conatiner = container.findAll("div",{"class":"desc"})
    news_desc = desc_conatiner[0].p.text.replace("\'","")

    link_container=container.findAll("div",{"class":"desc"})
    news_link=my_url+ link_container[0].a["href"]
    count+=1
    print('News Number: ', count)
    print('Category: ',cat,'\n')
    print('News Title: ',title,"\n")
    print('Time: ',arc_dt,"\n")
    print('Description: ',news_desc,"\n")
    print('Link: ',news_link,"\n")
    print('*'*100)
   # arc_dt=conn.convert_to_date(arc_dt)
    conn.insert_data("NEWS",[count,1,title,news_desc,arc_dt,news_link])
conn.insert_data('NEWS_CATEGORY',[1,cat])
    

count_1=count
for container_2 in containers2:
    category_container = page_soup2.findAll("div",{"class":"clr breadCrumb contentwrapper"})
    category = category_container[0].text.split('›')[2:][0].split(' ')[0]
    
    news_title = container_2.h3.text.replace("\'","")
    desc = container_2.p.text.replace("\'","")
    date_container_2=container_2.findAll("time",{"class":"date-format"})
    date = date_container_2[0].text.replace(",","")
    ddt = parse(date)
    date_news=ddt.strftime('%d-%m-%Y %H:%M:%S')
    link = my_url+ container_2.a["href"]
    count_1+=1
    print('News Number: ',count_1 , '\n')
    print("news_category :",category, '\n')
    print("news_title :", news_title, '\n')
    print("news_desc :",desc, '\n')
    print("news_date :",date_news, '\n')
    print("news_link:",link, '\n')
    print('*' *100)
   # date_news=conn.convert_to_date(date_news)
    conn.insert_data("NEWS",[count_1,2,news_title,desc,date_news,link])
conn.insert_data('NEWS_CATEGORY',[2,category])

count_2=count_1
for container3 in containers3:
    
    cat_container3 = page_soup3.findAll("h1",{"class":"h1"})
    category3=cat_container3[0].text.split()[0]
    title3=container3.h3.text.replace("\'","")
    desc3=container3.p.text.replace("\'","")
    date3=container3.time.text.replace(",","")
    dt = parse(date3)
    d3=dt.strftime('%d-%m-%Y %H:%M:%S')
    link3=my_url3+container3.h3.a["href"]
    count_2 +=1
    print('News Number: ',count_2 , '\n')
    print("Category :",category3, '\n')
    print("Tilte :",title3, '\n')
    print("Description :",desc3, '\n')
    print("Date :",d3, '\n')
    print("Link :",link3, '\n')
    print("*"*100)
   # d3=conn.convert_to_date(d3)
    conn.insert_data("NEWS",[count_2,3,title3,desc3,d3,link3])
conn.insert_data('NEWS_CATEGORY',[3,category3])
