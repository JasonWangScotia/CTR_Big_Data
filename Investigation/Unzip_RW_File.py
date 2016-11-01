'''
Created on Oct 27, 2016

@author: ywang8
'''

from zipfile import ZipFile
import os,re

in_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/Downloads/'
out_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/'

#Acquire desired date
date_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/'
date_filename = 'Date.txt'
f = open(date_folder + date_filename,'r')
date = f.readline().strip()

try:
    os.stat(out_folder + date)
except:
    os.mkdir(out_folder + date)

for (dirpath, dirnames, filenames) in os.walk(in_folder):
    for filename in [f for f in filenames if f[-4:] =='.zip']:
        f_zip = ZipFile(in_folder + filename)
        for folders in f_zip.namelist():
            match = re.search('outfiles/riskwatch',folders)
            if match:
                f_zip.extract(folders, out_folder + date + '/')