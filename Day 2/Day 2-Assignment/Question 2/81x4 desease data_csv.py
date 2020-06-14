
import numpy as np
import pandas as pd
col_list=['Disease', 'Age', 'Number', 'Start']
df=pd.read_csv('/root/Downloads/dataset.csv', usecols=col_list)
#View all colomns present
print(df['Disease'])
print(df['Age'])
print(df['Number'])
print(df['Start'])

#shape
print(df.shape)
#length
print(len(df))
#size
print(df.size)
#Dimension
print(df.ndim)
#missing values
print(df.count())
#number of non missisng values(information about entries and dataset)
print(df.info())
#type
print(type(df))
#Display 5 elements of datasheet
a=df.head(5)
print(a)
#view req. colomns we want in datasheet
print (df.loc[[10,1],['Disease','Age']])
print (df.loc[2:16,['Disease','Age']])
Disease = df.loc[df['Age']>50, 'Disease']
