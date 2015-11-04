
# coding: utf-8

import pandas as pd
import pickle


# Reading in data, basic cleaning 

df = pd.read_csv('../datafiles/stata.csv')
df = pd.get_dummies(df['CPO']).join(df)

del df['ID2']
del df['ReportedTotal']
del df['ReportedInd']
del df['Party']
del df['CPO']
df = df.fillna(0)
df.columns = df.columns.map(lambda x: x.lower())


# Making new variables 

col_list_unitem= ['unitemind', 'unitempacs', 'unitemfor', 'unitemproxy']
col_list_item = ['itemind', 'unitempacs', 'unitemfor', 'unitemproxy']
df['unitemtotal'] = df[col_list_unitem].sum(axis=1) 
df['itemtotal'] = df[col_list_item].sum(axis=1)
df['total'] = df[['unitemtotal', 'itemtotal']].sum(axis=1)
df['unitemie'] = df[['unitemfor', 'unitemproxy']].sum(axis=1)
df['itemie'] = df[['itemfor', 'itemproxy']].sum(axis=1)
df['percunitem'] = df['unitemtotal']/df['total']
df['total'] = df['total'].apply(lambda x: float(x))
df['percpacs']= df['totalpacs']/df['total']
df['ie'] = df['iefor'] + df['ieproxy']
df['percie'] = df['ie']/df['total']
df['percind']= df['totalind']/df['total']
df['percstate']= df['instate']/df['total']


pickle.dump( df, open( "../datafiles/data.p", "wb" ) )

