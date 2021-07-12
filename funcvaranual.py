import requests
import pandas as pd
import openpyxl
from numpy import datetime64
from datetime import date

def varanualmortes(dfBrazil):
    dfBrazilAnoAntes = dfBrazil.iloc[0:365]
    dfBrazilAnoDepois = dfBrazil.iloc[365:550]
    dfBrAntes = dfBrazilAnoAntes.select_dtypes(include=['float'])
    dfBrDepois = dfBrazilAnoDepois.select_dtypes(include=['float'])
    dfBrDepois = dfBrDepois.rename(columns={'Total de mortes': 'Total'})
    dfBrDepois = dfBrDepois.drop('Novas mortes no dia', axis=1)
    dfBrAntes = dfBrAntes.drop('Novas mortes no dia', axis=1)
    dfBrAntes = dfBrAntes.reset_index()
    dfBrDepois = dfBrDepois.reset_index()
    dfBrAntes = (dfBrAntes.dropna())
    dfBrDepois = (dfBrDepois.dropna())
    dfBrDepois = dfBrDepois.drop('index', axis=1)
    dfBrAntes = dfBrAntes.drop('index', axis=1)
    frames = [dfBrAntes, dfBrDepois]
    result = pd.concat(frames, axis=1, join="inner")

    dfconta = (((result['Total'] / result['Total de mortes']) - 1) * 100)
    dfconta = pd.DataFrame(data=dfconta, columns=["Variação Anual: Total de Mortes"])

    dfBrazilAnoAntes1 = dfBrazil.iloc[0:365]
    dfBrazilAnoDepois1 = dfBrazil.iloc[365:550]
    dfBrAntes1 = dfBrazilAnoAntes1.select_dtypes(include=['float'])
    dfBrDepois1 = dfBrazilAnoDepois1.select_dtypes(include=['float'])
    dfBrDepois1 = dfBrDepois1.rename(columns={'Novas mortes no dia': 'Total'})
    dfBrDepois1 = dfBrDepois1.drop('Total de mortes', axis=1)
    dfBrAntes1 = dfBrAntes1.drop('Total de mortes', axis=1)
    dfBrAntes1 = dfBrAntes1.reset_index()
    dfBrDepois1 = dfBrDepois1.reset_index()
    dfBrAntes1 = (dfBrAntes1.dropna())
    dfBrDepois1 = (dfBrDepois1.dropna())
    dfBrDepois1 = dfBrDepois1.drop('index', axis=1)
    dfBrAntes1 = dfBrAntes1.drop('index', axis=1)
    frames1 = [dfBrAntes1, dfBrDepois1]
    result1 = pd.concat(frames1, axis=1, join="inner")

    dfcontas = ((result1['Total'] / result1['Novas mortes no dia'] - 1) * 100)
    dfcontas1 = pd.DataFrame(data=dfcontas, columns=["Variação Anual: Novas mortes por dia"])

    concatenar = [dfconta, dfcontas1]
    dfFinal = pd.concat(concatenar, axis=1, join="inner")

    dfFinal.to_csv('Brazilvariacaoanualcovid.csv', sep=';')

    return (print(dfFinal))