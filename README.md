# NewsScrapper
News_scrapper built using pycurl and beautifulsoup libraries, oracle database to store the results and flask to host to result api ,finally django framework used to display the data
1- Setup your oracle instance and connect the databse with connectionoracle.py file
2- After setting the file run the News_scrapper.py file it will fetch all the articles from the economic times
3- Once the results are stored in the database run the api.py file it is a flask application to create api.
4- Once the api is hosted from localhost fetch the json in django framework.
5- The django framework will display the  whole articles in structured format.
