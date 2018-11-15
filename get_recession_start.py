#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:59:41 2018

@author: yanielc
"""
import pandas as pd

def get_recession_start():
    
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    
    quarter_gdp_df = pd.read_excel('gdplev.xls',usecols=[4,5,6],index_col=0,header=4).dropna()
    quarter_gdp_df.columns = ['GDP_today_$','GDP_2009_$']
    quarter_gdp_df = quarter_gdp_df[quarter_gdp_df.index >= '2000q1']
    
    #create flag
    quarter_gdp_flag = pd.DataFrame(quarter_gdp_df['GDP_2009_$'].diff())
    quarter_gdp_flag['flag'] = 0
    quarter_gdp_flag.loc[quarter_gdp_flag['GDP_2009_$'] >= 0, 'flag'] = 1
    
    #shift flag for comparisons
    quarter_gdp_flag['previous'] = quarter_gdp_flag['flag'].shift(1)
    quarter_gdp_flag['next'] = quarter_gdp_flag['flag'].shift(-1)
    quarter_gdp_flag['start'] =0
    
    quarter = quarter_gdp_flag[(quarter_gdp_flag['flag']==0) & (quarter_gdp_flag['previous'] == 1) & (quarter_gdp_flag['next'] == 0)].index[0]

    
    return quarter

if __name__ == '__main__':
    print((get_recession_start()))
    
    