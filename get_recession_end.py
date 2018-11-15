#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 16:38:00 2018

@author: yanielc
"""
import pandas as pd
from get_recession_start import get_recession_start

def get_recession_end():
    
    
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    
    quarter_gdp_df = pd.read_excel('gdplev.xls',usecols=[4,5,6],index_col=0,header=4).dropna()
    quarter_gdp_df.columns = ['GDP_today_$','GDP_2009_$']
    
    recStart = get_recession_start()
    quarter_gdp_df = quarter_gdp_df[quarter_gdp_df.index >= recStart]
    
    #create flag
    quarter_gdp = pd.DataFrame(quarter_gdp_df['GDP_2009_$'].diff())
    quarter_gdp['flag'] = 0
    quarter_gdp.loc[quarter_gdp['GDP_2009_$'] >= 0, 'flag'] = 1
    
    #shift flag for comparisons
    quarter_gdp['previous'] = quarter_gdp['flag'].shift(1)
    quarter_gdp['next'] = quarter_gdp['flag'].shift(-1)
    
    onset = quarter_gdp[(quarter_gdp['flag']==1) & (quarter_gdp['previous']==0) & (quarter_gdp['next'] ==1)].index[0]
    
    pos_first_growth = quarter_gdp.index.tolist().index(onset)
    end = quarter_gdp.index.tolist()[pos_first_growth+1]
    
    return end



if __name__ == '__main__':
    
    print(get_recession_end())