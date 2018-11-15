import pandas as pd
from scipy import stats

from get_recession_start import get_recession_start
from get_recession_bottom import get_recession_bottom
from get_recession_end import get_recession_end
from convert_housing_data_to_quarters import convert_housing_data_to_quarters
from get_list_of_university_towns import get_list_of_university_towns



def run_ttest():
    
    '''Analysis to check behavior of real estate market during 2008 recession.
    We compute the onset, bottom, and end of the recession by looking at U.S. 
    GDP growth/decline.
    
    We get the ratio (housing price at start of recession) / (housing price
    at bottom of recession). The data is divided between university and 
    non-university towns.
    
    A t-test is run between the data points for university and non-university
    towns.
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    
                                                     
    # get timings of 2008 recession 
    recStart = get_recession_start()    
    recBot = get_recession_bottom()
    recEnd = get_recession_end()
    
    #raw data. Convert time periods to annual quarters
    houseVal_df = convert_housing_data_to_quarters()[[recStart, recBot,recEnd]]
    
    # get ratio of real estate prices at onset of recession to bottom of recession
    houseVal_df['priceRatio'] = houseVal_df[recStart] / houseVal_df[recBot]

    
    #get university towns
    uniTowns_df = get_list_of_university_towns().set_index(['State','RegionName'])
    
    #housing values for university towns
    uniVal_df = houseVal_df.loc[houseVal_df.index.isin(uniTowns_df.index) ]
    
    #housing values for non-university towns
    not_uniVal_df = houseVal_df.drop(uniTowns_df.index)
    
    # run t-test to check if the ratio of house values are different between
    # university and non-university towns
    
    p = stats.ttest_ind(uniVal_df['priceRatio'],not_uniVal_df['priceRatio'], nan_policy='omit')[1]
        
    different = True
    if p <0.01:
        different = True
    else:
        different = False
    
    better =''
    if uniVal_df['priceRatio'].mean() < not_uniVal_df['priceRatio'].mean():
        better = "university town"
    else:
        better = "non-university town" 
                                            
    return (different, p, better)

print(run_ttest())