#import required libraries
import pandas as pd #to analyze data
import requests #to handle  requests
from bs4 import BeautifulSoup #to parse HTML documents

#get the response in the form of html
url = 'https://en.wikipedia.org/wiki/List_of_Indonesian_cities_by_population'
response = requests.get(url)

#parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.content, 'html.parser')

#get table with class 'wikitable sortable'
table = soup.find('table',{'class':'wikitable'})
table

#convert list to dataframe
df = pd.read_html(str(table))
df = pd.DataFrame(df[0])

print(df.head()) #print the top 5 data rows before cleaning

#drop the unwanted columns
df_clean = df.drop(["Notes"], axis=1)
#change the columns name for ease
df_clean = df_clean.rename(columns={"2020census[2]": "Pupulation (2020)","2010census[2]": "Population (2010)"})

print(df_clean.head()) #print the top 5 data rows after cleaning

#convert dataframe to csv file
df_clean.to_csv('List_of_Indonesian_cities_by_population.csv', index=False, encoding='utf-8', quoting=1)
