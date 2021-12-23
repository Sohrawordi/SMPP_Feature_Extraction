# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 11:36:40 2020

@author: Shaikot
"""


def raw_moment(d,m):
    #import statistics as sts
    
    s=0

        #p=sts.mean(d)
    for j in range(len(d)):
        #print(d[j],(d[j])**m)
        s=s+(d[j])**m

    return (s/len(d))
        
        











def moment(dataset):
    import pandas as pd
    #import statistics as sts
    from scipy import stats
    #import numpy as np
    #amino_acid="ACDEFGHIKLMNPQRSTWYVX"
    
    
    aaindex=pd.read_csv('Index.csv')
    colls=[]
    for i in range(len(aaindex.index)):
        #print(aaindex['Index'][i])
        index=aaindex['Index'][i]
        for j in range (1,3):
            colls.append(index+"_raw_moment_"+str(j))
            
        for j in range (2,3):
            colls.append(index+"_central_moment_"+str(j))    
            
    df=pd.DataFrame(columns=colls)
    
    
    
    
    for i in range(len(dataset.index)):
        #data_list=[]
        seq=dataset['Sequence'][i]
        row={}
       # print(seq)
        for index in range (len(aaindex.index)):
            data_list=[]
            for acid in seq:
                #print(acid,aaindex[acid][index])
                data_list.append(aaindex[acid][index])
            new_list=data_list    
            #print(data_list)    
            #new_list=np.divide(data_list,sum(data_list))
            #print(new_list)
            for m in range(1,3):
                row[aaindex['Index'][index]+"_raw_moment_"+str(m)]=raw_moment(new_list,m)
            
            
            
            for m in range(2,3):
                #print(aaindex['Index'][index]+"_central_moment_"+str(m))
                #print(stats.moment(new_list,moment=m))
                row[aaindex['Index'][index]+"_central_moment_"+str(m)]=stats.moment(new_list,moment=m)
                
                
                
                
                
                
        df=df.append(row,ignore_index=True)
    
  
    return df


#split_data_set\Raw_Samples
import pandas as pd    
positive=pd.read_csv('split_data_set/Raw_Samples/Positive.csv')
n=positive
positive=positive.sample(frac=3, replace='True')
positive=positive.reset_index(drop=True)
#positive.to_csv('Selected_Raw_sequence/Selected_positive.csv',index=False)
df=moment(positive)

print(df)

#df.to_csv('Numerical_Moment_features/positive_numerical_moment_samples.csv',index=False)


Negative=pd.read_csv('split_data_set/Raw_Samples/Negative.csv')
Negative=Negative.sample(frac=len(positive.index)/len(Negative.index))
Negative=Negative.reset_index(drop=True)
#Negative.to_csv('Selected_Raw_sequence/Selected_negative.csv',index=False)
df=moment(Negative)
print(df)
#df.to_csv('Numerical_Moment_features/negative_numerical_moment_samples.csv',index=False)







