import pandas as pd
import numpy as np


def get_list_of_university_towns():
    import re
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    
    
    fh = open('university_towns.txt','r')
    uni_ls = [x.rstrip() for x in fh.readlines()]
    fh.close()
    
    #get position of states
    state_pos = []
    for x in uni_ls:
        if '[edit]' in x:
            state_pos.append(uni_ls.index(x))
            
    #make city - state pairs
    p = re.compile('\(')
    p2 = re.compile('\[')
    cities_ls = []
    for i in range(len(state_pos)-1): # this line excludes Wyoming schools (since wyoming is the last state)
        for j in range(len(uni_ls)):
            if j >= state_pos[i] and j < state_pos[i+1]:               
                if p.search(uni_ls[j]):
                    #print([uni_ls[state_pos[i]][:-6],uni_ls[j][:p.search(uni_ls[j]).start()]])
                    cities_ls.append([uni_ls[state_pos[i]][:-6].rstrip(),uni_ls[j][:p.search(uni_ls[j]).start()].rstrip()])
                elif ( not p.search(uni_ls[j]) ) and ( not p2.search(uni_ls[j]) ):
                    cities_ls.append([uni_ls[state_pos[i]][:-6].rstrip(),uni_ls[j].rstrip()]) #NEW. Should give lines without ()
            elif j > state_pos[i+1]:
                #print(cities_ls[j])
                break
    
    for x in uni_ls[state_pos[len(state_pos) -1]:]:
        if p.search(x):
            cities_ls.append([uni_ls[state_pos[len(state_pos)-1]][:-6].rstrip(),x[:p.search(x).start()].rstrip()])
     
            
    
    
    cities_df = pd.DataFrame(cities_ls,columns=["State", "RegionName"])
    
    
    #################################
    
    
    return cities_df


if __name__ == '__main__':
    print(get_list_of_university_towns().head())
    

