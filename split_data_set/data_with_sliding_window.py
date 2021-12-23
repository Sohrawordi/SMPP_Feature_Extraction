# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 09:16:27 2020

@author: Shaikot
"""


from Bio import SeqIO



#read a fasta file with protien sequence and create a dictionary of them

data_dict = SeqIO.to_dict(SeqIO.parse("Fasta_file/PhoGly_40 _fasta_file.fasta", "fasta"))


# read a fasta file that contains describtion and position of varified PTM resedues as sequence and create list of the elements
position_list = list(SeqIO.parse("Fasta_file/PhoGly_40 _position.fasta", "fasta"))

window_size=21

strim_size=int(window_size/2)

import pandas as pd
colls=["Code","Position","Sequence","Class"] 
positive=pd.DataFrame(columns=colls)
negative=pd.DataFrame(columns=colls)

#print(position_list[0].description)




for i in range(len(position_list)):
    # to convert resedues position string into individual position number 
    #print(position_list[i].id)
    s=str(position_list[i].seq)# position sequence into string
    position=s.split(",")
    #print(position_list[i].seq)
    #print()
    
    #print(data_dict[position_list[i].id].seq)
    seq=data_dict[position_list[i].id].seq # to read protien sequence from dictionary of fasta file 
    
    
    
        
    seq=str(seq)  
    #print(len(seq))
    import re  
    find_k=[x.start() for x in re.finditer('K', seq)] # crate a list of position of Lysine resedue from protien sequence
    
    test_list_set = set(position)
    for k in find_k:
        if k<strim_size or k>len(seq)-strim_size-1: # for resedue K that lies in start or end of sequence and less than upstram or downstram size 
            if k<strim_size:
                tem=""
                #print(10-k)
                for t in range(strim_size-k):
                    tem=tem+"X"
                #print(tem+seq[0:k+strim_size+1],k+1)    
                if str(k+1) in test_list_set:# if K is found in position list then this samples is kept in positive dataframe and otherwise in negative
                    
                    #see=tem+seq[0:k+10+1]
                    #print(see)
                    
                    row={"Code":position_list[i].description,"Position":k+1,"Sequence":str(tem+seq[0:k+strim_size+1]),"Class":1}
                    positive=positive.append(row,ignore_index=True)
                else:
                    row={"Code":position_list[i].description,"Position":k+1,"Sequence":str(tem+seq[0:k+strim_size+1]),"Class":0}
                    
                    negative=negative.append(row,ignore_index=True)
        
            else :
                tem=""
                for t in range(strim_size-(len(seq)-k-1)):
                    tem=tem+"X"
                #print(seq[k-strim_size:len(seq)+1]+tem,k+1)
                if str(k+1) in test_list_set:
                    
                    row={"Code":position_list[i].description,"Position":k+1,"Sequence":str(seq[k-strim_size:len(seq)+1]+tem),"Class":1}
                    positive=positive.append(row,ignore_index=True)
                else:
                    row={"Code":position_list[i].description,"Position":k+1,"Sequence":str(seq[k-strim_size:len(seq)+1]+tem),"Class":0}
                    negative=negative.append(row,ignore_index=True)
        
        else:
             #print(seq[k-strim_size:k+1+strim_size],k+1)
             #row={"Code":position_list[i].description,"Position":k+1,"Sequence":str(seq[k-10:k+1+10]),"Class":1}
             if str(k+1) in test_list_set:
                 #print(seq[k-10:k+1+10],k+1)
                 row={"Code":position_list[i].description,"Position":k+1,"Sequence":str(seq[k-strim_size:k+1+strim_size]),"Class":1}
                 positive=positive.append(row,ignore_index=True)
             else:
                 row={"Code":position_list[i].description,"Position":k+1,"Sequence":str(seq[k-strim_size:k+1+strim_size]),"Class":0}
                 negative=negative.append(row,ignore_index=True)
        

        
    
    



#print(positive)
#print(negative)


positive.to_csv('Raw_Samples/Positive.csv',index=False)
negative.to_csv('Raw_Samples/Negative.csv',index=False)


# for fata file generation
"""

fasta=["fasta"] 

fpositive=pd.DataFrame(columns=fasta)

for i in range (len(positive.index)):
    d_raw={}
    #print(positive['Code'][i],positive['Position'][i],positive['Sequence'][i])
    d_raw['fasta']=">"+positive['Code'][i]+" Position  "+str(positive['Position'][i])
    fpositive=fpositive.append(d_raw,ignore_index=True)
    #negative=negative.append(row,ignore_index=True)
    d_raw['fasta']=positive['Sequence'][i]
    fpositive=fpositive.append(d_raw,ignore_index=True)
    

fpositive.to_csv('E:/PTM_Prediction/Formylation/Uncompleted/formylation_2/Data_with_various_window/fasta_Positive.fasta',index=False)




fasta=["fasta"] 

fnegative=pd.DataFrame(columns=fasta)

for i in range (len(negative.index)):
    d_raw={}
    #print(negative['Code'][i],negative['Position'][i],negative['Sequence'][i])
    d_raw['fasta']=">"+negative['Code'][i]+" Position  "+str(negative['Position'][i])
    fnegative=fnegative.append(d_raw,ignore_index=True)
    #negative=negative.append(row,ignore_index=True)
    d_raw['fasta']=negative['Sequence'][i]
    fnegative=fnegative.append(d_raw,ignore_index=True)
    

fnegative.to_csv('E:/PTM_Prediction/Formylation/Uncompleted/formylation_2/Data_with_various_window/fasta_negative.fasta',index=False)




"""



"""
for i in range(len(positive.index)):
    seq=positive['Sequence'][i]
    if len(seq)<window_size:
        print(seq,positive['Code'][i],positive['Position'][i])
    

"""





