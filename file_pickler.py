#!/usr/bin/env python
import os, sys, subprocess, fileinput,\
cPickle, time, shutil, fnmatch, glob,\
traceback
tmp_list = []


def read_txt_file(path_dir_file,keyword):
    directory = path_dir_file.split('\n')
    print directory
    for dirct in directory:
  for m_file in os.listdir(dirct):
	    if fnmatch.fnmatchcase(m_file, keyword):
		get_file_dir(dirct, m_file)

def get_file_dir(mpath, mfile):
    print mpath, mfile
    tmp_str = os.path.join(mpath, mfile)
    tmp_list.append(tmp_str)
    file_pickler_func(tmp_list)
    print "ok2"

def file_pickler_func(mylist):
    print mylist
    mfile = open('myPickle', 'wb')
    #mfile.write('result%s'%mylist)
    cPickle.Pickler(mfile)
    cPickle.dump(mylist, mfile)
    mfile.close()
    print "ok3"
