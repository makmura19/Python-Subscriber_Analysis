# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 17:39:11 2022

@author: XPS
"""
import pandas as pd
import math
import numpy as np

df_subs = pd.read_csv('D:/Works/2022_NextProject/Program/U60/2022_Profitability Program/02.CovMo_Output/Join_Att_byLocation.csv')
df_subs['Subscriber Count'] = df_subs['Subscriber Count'].str.replace(',','')
df_subs['Subscriber Count'] = df_subs['Subscriber Count'].astype(int)
df_subs.info()


#create additional longLat
df_subs['add_Long'] = df_subs.apply(lambda row: row.Longitude_x, axis = 1)
df_subs['add_Lat'] = df_subs.apply(lambda row: row.Latitude_x + 1, axis = 1)

#Delta Longlat
df_subs['delta_long'] = df_subs.apply(lambda row: row.Longitude_y - row.Longitude_x, axis = 1)

#Vector Site - Add Longlat
def vector_A(x,y,z,k):
    return ((x-y)**2 + (z-k)**2)**0.5


def vector_B(p,q,r,s):
    return ((p-q)**2 + (r-s)**2)**0.5


df_subs['length_of_vector_A'] = [vector_A(df_subs.Longitude_x[i], 
                                   df_subs.add_Long[i],
                                   df_subs.Latitude_x[i], 
                                   df_subs.add_Lat[i]) for i in range(len(df_subs))]

df_subs['length_of_vector_B'] = [vector_B(df_subs.Longitude_x[i],
                                df_subs.Longitude_y[i],
                                df_subs.Latitude_x[i],
                                df_subs.Latitude_y[i]) for i in range(len(df_subs))]
                                
#Dot Product of vectors
def dot_vectors(a,b,c,d,e,f):
    return ((a-b)*(a-c))+((d-e)*(d-f))


df_subs['dot_product_of_vectors'] = [dot_vectors(df_subs.Longitude_x[i],
                                                 df_subs.add_Long[i],
                                                 df_subs.Longitude_y[i],
                                                 df_subs.Latitude_x[i],
                                                 df_subs.add_Lat[i],
                                                 df_subs.Latitude_y[i]) for i in range(len(df_subs))]

#Cos alpha & arc cos alpha
def cos_alpha(x,y,z):
    return x/(y*z)


def arc_cos_alpha(x,y,z):
    return math.degrees(math.acos(x/(y*z)))


df_subs['cosinus_alpha'] = [cos_alpha(df_subs.dot_product_of_vectors[i], df_subs.length_of_vector_A[i], df_subs.length_of_vector_B[i])
                            for i in range(len(df_subs))]
df_subs['arc_cosinus_alpha'] = [arc_cos_alpha(df_subs.dot_product_of_vectors[i], df_subs.length_of_vector_A[i], df_subs.length_of_vector_B[i])
                                for i in range(len(df_subs))]
def actual_arc(x,y):
    if x > 0:
        return y
    else:
        return 180 + (180-y)
    

df_subs['actual_of_arc_cos_alpha'] = [actual_arc(df_subs.delta_long[i], df_subs.arc_cosinus_alpha[i])
                                      for i in range(len(df_subs))]

#Quadrant Info
def quadrant(x):
    if x <= 90:
        return 'Q1'
    elif x > 90 and x <= 180:
        return 'Q2'
    elif x > 180 and x <= 270:
        return 'Q3'
    else:
        return 'Q4'


df_subs['Quadrant_Flag'] = [quadrant(df_subs.actual_of_arc_cos_alpha[i]) for i in range(len(df_subs))]

#percentile 75th & pivot table
def p75(m):
    return np.percentile(m,75)


df_subs_pivot = pd.pivot_table(data = df_subs, index = ['SiteId','Quadrant_Flag'],
                               values = ['Subscriber Count'], aggfunc= ['count', p75])

#lookup of df_subs to pivot
df_subs_merged = pd.merge(df_subs,df_subs_pivot, on = ['SiteId','Quadrant_Flag'], how = 'inner')
df_subs_merged.to_csv('D:/Works/2022_NextProject/Program/U60/2022_Profitability Program/02.CovMo_Output/Output_Processing.csv', index=None)
