'''
Created on Nov 8, 2016

@author: ywang8
'''
import pandas as pd, os, re

import os, time

in_folder = 'C:/Users/ywang8/Documents/Data Quality Testing/'
in_file = 'Underlying_Instrument D8.csv'

out_folder = 'C:/Users/ywang8/Documents/Data Quality Testing/'
out_file = 'Bond Future D8 Results.csv'


try:
    os.stat(out_folder[:-1])
except:
    os.mkdir(out_folder[:-1])
    
    
f_out = open(out_folder + out_file, 'w')

f_out.write(','.join(['Deliverable','Line Num' + '\n']))

file_path = in_folder + in_file
df_in_file = pd.read_csv(file_path)


for col in df_in_file.columns:
    for row in df_in_file.index:
        row_input = []
        deliverable = str(df_in_file.at[row,col]).strip()
        if deliverable[1] == 'I':
            if deliverable[14] != '~':
                row_input = ','.join([deliverable,str(row+2) + '\n'])
                f_out.write(row_input)
        elif deliverable[1] == 'C':
            if deliverable[11] != '~':
                row_input = ','.join([deliverable,str(row+2) + '\n'])
                f_out.write(row_input)
        elif deliverable[1] == 'S':
            if deliverable[9] != '~':
                row_input = ','.join([deliverable,str(row+2) + '\n'])
                f_out.write(row_input)
        elif deliverable[1] == 'A':
            if deliverable[9] != '~':
                row_input = ','.join([deliverable,str(row+2) + '\n'])
                f_out.write(row_input)
                
f_out.close()

            
            