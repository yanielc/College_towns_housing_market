#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 18:29:59 2018

@author: yanielc
"""

import pandas as pd, numpy as np

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    
    '''A quarter is a specific three month period, Q1 is January through 
    March, Q2 is April through June, Q3 is July through September, Q4 is 
    October through December.'''
    
    house_df = pd.read_csv('City_Zhvi_AllHomes.csv',index_col = [2,1]).drop(labels=['RegionID','Metro','CountyName','SizeRank'],axis=1)
    
    all_months = house_df.columns.tolist()
    needMonths = all_months[all_months.index('2000-01'):all_months.index('2016-08')+1]
    
    # cut to needed months only
    house_df = house_df[needMonths]

    #get quarter names
    months_df = pd.DataFrame(needMonths,columns=['FullDate'])
    months_df['quarter'] = months_df['FullDate'].apply(lambda x : x[:4]+'q1' if int(x[5:]) in [1,2,3] else
             (x[:4]+'q2' if int(x[5:]) in [4,5,6] else
              (x[:4]+'q3' if int(x[5:]) in [7,8,9] else
               (x[:4]+'q4' if int(x[5:]) in [10,11,12] else False) ) )  )
    quarterNames = months_df['quarter'].drop_duplicates().tolist()

    #create quarters ranges
    months_gp =[]
    for i in np.arange(0,198,3):
        temp =[]
        for j in [0,1,2]:
            temp.append(needMonths[i+j])
        months_gp.append(temp)
    months_gp.append(['2016-07', '2016-08'])
    
    #create new dataframe with quarters
    houseQuarter_df = pd.DataFrame(columns = quarterNames, index=house_df.index)
        
    for x in range(len(quarterNames)):
        houseQuarter_df[quarterNames[x]] = house_df[months_gp[x]].mean(axis=1) 
    
    # Use this dictionary to map state names to two letter acronyms
    states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}
    oldIndex = houseQuarter_df.index
    newIndex = []
    
    for i in range(len(oldIndex)):
        newIndex.append((states.get(oldIndex[i][0]),oldIndex[i][1]))
    idx = pd.MultiIndex.from_tuples(newIndex)
    houseQuarter_df.index = idx
    
    return houseQuarter_df
    
   
    
 
    
    
if __name__ == '__main__':
    
    convert_housing_data_to_quarters()
    