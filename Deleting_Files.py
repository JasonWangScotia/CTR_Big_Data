'''
Created on Oct 11, 2016

@author: ywang8
'''
import pandas as pd, os

import os

source_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/riskwatch/'

for (dirpath, dirnames, filenames) in os.walk(source_folder):
    for filename in filenames:
        file_path = source_folder + filename
        os.remove(file_path)