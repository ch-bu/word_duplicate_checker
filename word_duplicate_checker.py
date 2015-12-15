# -*- coding: utf-8 -*-

import os
from docx import opendocx, getdocumenttext
from itertools import combinations
from difflib import SequenceMatcher

# Variable declaration
path = os.getcwd() + "\\files"
entries = os.listdir(path)
filenames = [os.path.join(path, entry) for entry in entries if os.path.isfile(os.path.join(path, entry))]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def document_to_text(filename, file_path):
    if filename[-5:] == ".docx":
        document = opendocx(file_path)	
        paratextlist = getdocumenttext(document)
        newparatextlist = []
        for paratext in paratextlist:
            newparatextlist.append(paratext.encode("utf-8"))
        return '\n\n'.join(newparatextlist)
    else:
        raise StandardError

duplicates = open('duplicates.txt', 'w+')

for (file1, file2) in combinations(filenames, 2):
    # try:
    #
    try:	
        text1 = document_to_text(file1, file1)
        text2 = document_to_text(file2, file2)
        similarity = similar(text1, text2)

        if similarity > .2:
            res = "%s - %s: %f" % (file1.split("\\")[-1], file2.split("\\")[-1], similarity)
            print(res)

        if similarity > .8:
            res = "%s - %s: %f" % (file1.split("\\")[-1], file2.split("\\")[-1], similarity)

            with open("duplicates.txt", "a+") as myfile:
                myfile.write(res + "\n")
    
    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        res = "Fehler bei %s - %s: %f" % (file1.split("\\")[-1], file2.split("\\")[-1], similarity)
        print(res)
        print message