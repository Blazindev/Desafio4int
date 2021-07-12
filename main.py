import requests
import pandas as pd
import openpyxl
from numpy import datetime64
from datetime import date
from funcvaranual import varanualmortes

url = "https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.xlsx"
resp = requests.get(url)

output = open("covidData.xlsx", "wb")
output.write(resp.content)
output.close()

df = pd.read_excel("covidData.xlsx")

dfBrazil = df[(df['location'].str.contains('Brazil'))]

dfBrazil = dfBrazil.loc[0:, ['date', 'total_deaths', 'new_deaths']]

dfBrazil['date'] = dfBrazil['date'].astype(datetime64)
dfBrazil['date'] = dfBrazil['date'].dt.strftime('%d/%m/%Y')

dfBrazil = dfBrazil.rename(columns = {'date': 'Data', 'total_deaths': 'Total de mortes', 'new_deaths': 'Novas mortes no dia'})

dfBrazil = (dfBrazil.dropna())

dfBrazil.to_csv('Brazilcovidcsv1.csv', sep=';')

print(dfBrazil)
varanualmortes(dfBrazil)







