#!/usr/bin/env python
import time, os, shutil
tmp_list = []

def confirm_func(c_files):
    for tmp_tuple in enumerate(c_files):
        file_size = os.path.getsize(tmp_tuple[1])
        shutil.copy(tmp_tuple[1], '/home/hein/BigFiles')\
                    if file_size > 20408\
                    else shutil.copy(tmp_tuple[1], '/home/hein/SmallFiles')
        tmp_list.append(tmp_tuple)
    print 'Copied!'
    file_rename_func()

def file_rename_func():
    dirlist  = []
    new_name = raw_input('Enter the name you wanna change   : ')
    for i in range(2):
        path = '/home/hein/SmallFiles/' if i is 0 else '/home/hein/BigFiles/'
        dirlist = os.listdir(path)
        tmp_list = []
        for i in range(len(dirlist)):
            if dirlist[i] is not None:
                tmp_list.append(path + dirlist[i])
                os.rename(tmp_list[i], '%s%s%s%s'%(path, new_name, '00',\
                                                   str(i+1)))
    print 'Renamed!'
