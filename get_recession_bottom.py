#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 18:08:58 2018

@author: yanielc
"""
import pandas as pd
from get_recession_end import get_recession_end
from get_recession_start import get_recession_start

def get_recession_bottom():
    
    
    recStart = get_recession_start()
    recEnd = get_recession_end()
    
    quarter_gdp_df = pd.read_excel('gdplev.xls',usecols=[4,5,6],index_col=0,header=4).dropna()
    quarter_gdp_df.columns = ['GDP_today_$','GDP_2009_$']
    quarter_gdp_df = quarter_gdp_df[(quarter_gdp_df.index >= recStart) & (quarter_gdp_df.index <= recEnd)]
    
    bottom = quarter_gdp_df[quarter_gdp_df['GDP_2009_$'] ==quarter_gdp_df['GDP_2009_$'].min()].index[0]
    
    return bottom

if __name__ == '__main__':
    print(get_recession_bottom())