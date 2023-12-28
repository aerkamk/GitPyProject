import pandas as pd 
import numpy as np
import matplotlib.pyplot as pyplot

veriler = pd.read_csv('veriler.csv')

#ulke,boy,kilo,yas,cinsiyet
ulke=veriler[['ulke']]
boy= veriler[['boy']]
kilo= veriler[['kilo']]
yas= veriler[['yas']]
cinsiyet= veriler[['cinsiyet']]

print(ulke)