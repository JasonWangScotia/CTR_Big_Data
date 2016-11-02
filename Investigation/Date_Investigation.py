'''
Created on Nov 1, 2016

@author: ywang8
'''

import pandas as pd, os, re, time

import os, csv

start_time = time.time()

#Acquire desired date
date_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/'
date_filename = 'Date.txt'
f = open(date_folder + date_filename,'r')
date = f.readline().strip()

in_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/' + date + '/' + 'outfiles/riskwatch/'

out_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/' + date + ' Results/'

out_file = 'Date_Format_Investigation_Result' + ' ' + date + '.csv'

#filter out the files with bug
file_to_skip = []
for (dirpath, dirnames, filenames) in os.walk(in_folder):
    for filename in filenames:
        match = re.search(r'.*_Position_SBLOTC_D_.*',filename)
        if match:
            file_to_skip.append(filename)
            
try:
    os.stat(out_folder[:-1])
except:
    os.mkdir(out_folder[:-1])
    
    
f_out = open(out_folder + out_file,'w')

f_out.write(','.join(['filename','col','row','date' + '\n']))



for (dirpath, dirnames, filenames) in os.walk(in_folder):
    row_input = []
    for filename in [f for f in filenames if f[-4:] =='.csv' and f not in file_to_skip]:
        file_path = in_folder + filename 
        #print(filename)
        df_in_file = pd.read_csv(file_path,low_memory=False)
        for col in df_in_file.columns:
            for row in df_in_file.index:
                match = re.search(r'^(?=(.*?[0-9]{1,2}-[A-Z a-z]{3}-[0-9]{2}))\1(.*)$',str(df_in_file.at[row,col]))
                if match:
                    row_input = ','.join([filename, str(col), str(row), str(df_in_file.at[row,col]) + '\n'])
                    f_out.write(row_input)
f_out.close()        
#print("--- %s seconds ---" % (time.time() - start_time))
