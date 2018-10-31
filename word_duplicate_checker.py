# -*- coding: utf-8 -*-
#  python3.5 word_duplicate_checker.py
# https://www.mathsisfun.com/combinatorics/combinations-permutations-calculator.html

import os
import io
import docx2txt
from itertools import combinations
from tqdm import tqdm
from difflib import SequenceMatcher
import glob

# Get all docx files
filenames = [filename for filename in glob.iglob('files/**/*.docx', recursive=True)]
    
def check_plagiarism():

    # Open connection for duplicates
    duplicates = open('duplicates.txt', 'w+')

    # Check combinations of all files
    for (file1, file2) in tqdm(combinations(filenames, 2)):
        
        try:
            text1 = docx2txt.process(file1)
            text2 = docx2txt.process(file2)
        except KeyError:
            continue

        similarity = SequenceMatcher(None, text1, text2).ratio()

        # Save plagiarism cases
        if similarity > .7:
            res = "%s - %s: %f" % (file1.split("\\")[-1], file2.split("\\")[-1], similarity)
            print(res)

            # Store plagiarism
            with open("duplicates.txt", "a+") as myfile:
                myfile.write(res + "\n")
        # Potential plagiarism cases
        elif similarity > .2:
            res = "%s - %s: %f" % (file1.split("\\")[-1], file2.split("\\")[-1], similarity)
            print(res)

if __name__ == "__main__":
    check_plagiarism()