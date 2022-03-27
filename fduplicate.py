#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib

hash_dict = {}  # hash : [<itm_list>]
hash_path = {}  # hash : [<itm_list>]
counter   = {}  # hash : counter
RAPORT = ''   # folder list + summary

# folder to check:
CHECK_PATH = r'c:\check_folder'
# path to log results:
LOG_PATH = r'c:\result.txt'


# /*------------------------
def lst_file(path='', step=0):
    if path:
        global RAPORT
        for filename in os.listdir(path):
            f = os.path.join(path, filename)
            if os.path.isfile(f):
                type("{0}{1}".format(' '*step,f))
                RAPORT += "{0}{1}\n".format(' '*step,f)
                hashcollector(f)
            else:
                RAPORT += "{0}\\\n".format(' '*step)
                lst_file(f, step+1)
    else:
        print('podaj sciezke...')

def hashcollector(fname):
    itm = hashlib.md5()
    # /* for small files for now
    with open(fname, 'rb') as fp:
        fdata = fp.read()
        if fdata:
            itm.update(fdata)
    
    if itm.hexdigest() in hash_dict.keys():
        hash_dict[itm.hexdigest()].append(fname.split('\\')[-1:][0])
    else:
        hash_dict[itm.hexdigest()] = fname.split('\\')[-1:]


lst_file(CHECK_PATH)

with open(LOG_PATH, 'w', encoding="utf-8") as resultf:
    for key in hash_dict.keys():
        if counter[key] > 1:
            resultf.write("----\n{0}: {1}\n -> {2}\n".format(counter[key], key, '\n'.join(hash_dict[key])))
