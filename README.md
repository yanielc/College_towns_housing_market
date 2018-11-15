# College_towns_housing_market


    Analysis to check behavior of real estate market during 2008 recession.
    We compute the onset, bottom, and end of the recession by looking at U.S. 
    GDP growth/decline.
    
    We get the ratio (housing price at start of recession) / (housing price
    at bottom of recession). The data is divided between university and 
    non-university towns.
    
    A t-test is run between the data points for university and non-university
    towns.
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p
    is equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should is either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).

    Use housing_tttest_analysis.py to run analysis.


   university_towns.txt: containst list towns with universities in the US
   
   City_Zhvi_AllHomes.csv: contains housing values on a monthly basis for cities in the US
   
   gdplev.xls: contains GDP data
