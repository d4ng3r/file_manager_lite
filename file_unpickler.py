#!/usr/bin/env python
import cPickle, sys, shutil, time, os, magic

def unpickler():
    unpic_file = open('myPickle', 'r')
    cPickle.Unpickler(unpic_file)
    temp = cPickle.load(unpic_file)
    unpic_file.close()
    printer(temp)
    return temp

def printer(tmp_file):
    print '%-50s%-30s%-30s%-10s%-15s\n'%('File',
                                         'Created Time',
                                         'Modified Time',
                                         'File Size',
                                         'File Info')
    for tmp_tuple in enumerate(tmp_file):
        meta_data = magic.from_file(tmp_tuple[1])
        created_time = time.ctime(os.path.getctime(tmp_tuple[1]))
        modified_time = time.ctime(os.path.getmtime(tmp_tuple[1]))
        file_size = os.path.getsize(tmp_tuple[1])
        print '%-50s%-30s%-30s%-10s%-15s'%(tmp_tuple[1],\
                                           created_time,\
                                           modified_time,\
                                           file_size,\
                                           meta_data)


