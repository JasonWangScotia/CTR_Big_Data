'''
Created on Oct 11, 2016

@author: ywang8
'''

import pandas as pd, os

import os

#Acquire desired date
date_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/'
date_filename = 'Date.txt'
f = open(date_folder + date_filename,'r')
date = f.readline().strip()

out_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/' + date + ' Results/'

summary = 'Summary' + ' ' + date + '.csv'

df_out_file = pd.DataFrame.from_csv(out_folder + 'Investigation_Result' + ' ' + date + '.csv', index_col=False)


df_groupby = df_out_file.groupby(['filename','col','error'])['error'].count()


s_out = open(out_folder + summary, 'w')

s_out.write(','.join(['Filename','Column Name','Error Code','Count()'+'\n']))


df_groupby.to_csv (out_folder + summary)

s_out.close()
