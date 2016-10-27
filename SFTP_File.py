
'''
Created on Oct 25, 2016

@author: ywang8
'''

import paramiko, os, time, re

t1 = time.time()

#Unix login file location
pass_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/'
pass_filename = 'rw_unix.txt'

#get password for server
f = open(pass_folder + pass_filename,'r')
this_host = f.readline().strip()
this_username = f.readline().strip()
this_pass = f.readline().strip()
f.close()


out_folder = 'C:/Users/ywang8/Documents/Side Project/For Matt/'

#server data
server_path_list = [['/opt/ctr/ctr/ctrapp/ctr/ctrarchive/compress/','Downloads']]

#get filenames from ctr unix server
paramiko.util.log_to_file('ssh.log') #turns on logging for access the unix file using ssh/smtp

#connect to the server
ssh = paramiko.SSHClient() 
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(this_host, username=this_username, password=this_pass)
stdin, stdout, stderr = ssh.exec_command('ls -l')
sftp = ssh.open_sftp()

for this_map in server_path_list:
    this_server = this_map[0]
    this_local = this_map[1]
    
    try:
        os.stat(out_folder + this_local)
    except:
        os.mkdir(out_folder + this_local)
    
    serverfile_list = sftp.listdir(path=this_server)
    for serverfile in serverfile_list:
#Find the file start with ctrdata-data_out on Oct-24-16
        match = re.search('ctrdata-data_out-24-OCT-16',serverfile)
        if match:
            sftp.get(this_server + str(serverfile), out_folder + this_local + '/' + str(serverfile))
            
            