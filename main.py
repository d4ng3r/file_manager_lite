#!/usr/bin/env python
import sys, os, shutil
import file_copier, file_pickler, file_unpickler

def file_pickler_func(dir_file, file_ext):
    file_pickler.read_txt_file(dir_file, file_ext)
    
def file_unpickler_func():
    mng_unpick = raw_input('Do you want to watch them(y/n)?    :')  #Comfirmed by user
    if mng_unpick is 'y':
        tmp_file = file_unpickler.unpickler()
    elif mng_unpick is 'n':
        print 'Thank you!'
    else:
        print 'Error'
    return tmp_file

def file_copier_func(file_list):    
    mng_copy = raw_input('Do you wan to copy them(y/n)?    :')  #Comfirmed by user
    if mng_copy is 'y':
        file_copier.confirm_func(file_list)
    elif mng_copy is 'n':
        print 'Thank You!'
    else:
        print 'Error!'

def file_del_func(f_list):
    mng_del = raw_input('Do you want to delete them from old place(y/n)?      :')   #Comfirmed by user
    if mng_del is 'y':
        for item in enumerate(f_list):
            os.remove(item[1])
    elif mng_del is 'n':
        print 'Thank You!'
    else:
        print 'Error!'

def manager(f_dir, f_ext, tmp_f_list):
    txt_input = (raw_input('''
Please do step by step(Recommanded).
Enter:  \'1\' to save the files\' list you have searched       :
        \'2\' to print the files\' list you have searched      :
        \'3\' to copy & rename the files you have searched    :
        \'q\' to quit                                         :    '''))
    while txt_input is 'q':
        break
    else:
        if txt_input is '1':
            file_pickler_func(f_dir, f_ext)
            print 'Pickle Saved!'
        elif txt_input is '2':
            tmp_f_list = file_unpickler_func()
        elif txt_input is '3':
            file_copier_func(tmp_f_list)
        #elif txt_input is '4':
        #    file_del_func(del_list)
        else:
            print 'Error!' 
        manager(f_dir, f_ext, tmp_f_list)#Recall function to do another function

if __name__ == '__main__':
    fpath = sys.argv[1]
    k_word = '\''+ sys.argv[2]+'\''
    data = open(fpath, 'r')
    file_dir = data.read()
    manager(file_dir, k_word, None)
