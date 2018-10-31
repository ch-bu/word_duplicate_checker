# Plagiarism checker for docx-files

This python scripts finds cases of plagiarism for a bunch of word files.

## How to use

* Store all docx-files in the directory `files`. The docx-files can also be in subdirectory. The script is recursive.

```
python3.5 word_duplicate_checker.py
```

All cases of plagiarism are then stored in `duplicates.txt`

## Algorithm

The algorithm checks for all possible file combinations: n! / (2! (n - 2)!). 500 texts take about 1.5 hours.