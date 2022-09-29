'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
checker=0
def get_entropy_of_dataset(df):
  entro=0
  last_one=df.keys()[-1]
  unique_key=df[last_one].unique()
  for val in unique_key:
    tempe=df[last_one].value_counts()[val]/len(df[last_one])
    entro=entro+(-tempe*np.log2(tempe))
  print(entro)  
  if checker:
    print(entro)
  return entro

'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
  rows=df.shape[0]
  avg_info=0
  attri=df[attribute].values
  unique_key=np.unique(attri)
  for currnt in unique_key:
      temp=df[df[attribute]==currnt]
      target=temp[[temp.columns[-1]]].values
      _, count=np.unique(target, return_counts=True)
      total=np.sum(count)
      entr=0
      for freq in count:
        temp=freq/total
        if temp!=0:
          entr=entr-(temp*np.log2(temp))
      avg_info=avg_info+(entr*(np.sum(count)/rows))
      print(' ',attribute,avg_info)
  return avg_info

'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
  info_gain=get_entropy_of_dataset(df)-get_avg_info_of_attribute(df,attribute)
  print('info_gain',info_gain)
  return info_gain

#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    maxi_gain=float("-inf")
    info={}
    for attribute in df.columns[:-1]:
        temp=get_information_gain(df, attribute)
        if temp>maxi_gain:
            column=attribute
            maxi_gain=temp
        info[attribute]=temp
    return (info,column) #week 3
