import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

Location = r'C:\Users\mpandurangan\Desktop\Crawler\TEST.csv'
Location_Out = r'C:\Users\mpandurangan\Desktop\Crawler\Output.xlsx'
df = pd.read_csv(Location,encoding = 'ISO-8859-1')

i = 0
df3 = pd.read_excel(Location_Out,sheetname='Sheet1')
for i in range(len(df)):
    search_word = df.iloc[i,0]
    df1 = pd.DataFrame({'Search Text':[search_word]})
    df1.set_index = ('Search Text')
    url = 'http://www.google.co.in/search?q='+search_word
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    soup.find_all('a')
    j = 1
    for link in soup.find_all('a'):
        html = link.get('href')
        html = html.replace('/url?q=','')
        if html.find('&sa=U') > 0 and link.text != 'Cached':

            df2 = pd.DataFrame({'Search Text':[search_word],'URL'+str(j):[html.split('&sa=U',1)[0]],'Text'+str(j):[link.text]})
            j += 1
            df2.set_index = ('Search Text')
            df1 = df1.merge(df2,on='Search Text',how='left')

    df3 = df3.append(df1)
    num = random.randint(5,15)
    time.sleep(num)
    df3.to_excel(Location_Out, sheet_name='Sheet1', index=False, header=True, startrow=1)
    i += 1

    
