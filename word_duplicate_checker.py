# -*- coding: utf-8 -*-

import os
import io
import docx2txt
from itertools import combinations
from difflib import SequenceMatcher

# Variable declaration
path = os.getcwd() + "/files"
entries = os.listdir(path)
filenames = [os.path.join(path, entry) for entry in entries if os.path.isfile(os.path.join(path, entry))]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
    
duplicates = open('duplicates.txt', 'w+')

for (file1, file2) in combinations(filenames, 2):

    text1 = docx2txt.process(file1)
    text2 = docx2txt.process(file2)
    similarity = similar(text1, text2)
    
    # print(similarity)

    if similarity > .2:
        res = "%s - %s: %f" % (file1.split("\\")[-1], file2.split("\\")[-1], similarity)
        print(res)

    if similarity > .7:
        res = "%s - %s: %f" % (file1.split("\\")[-1], file2.split("\\")[-1], similarity)
        print(res)

        with open("duplicates.txt", "a+") as myfile:
            myfile.write(res + "\n")