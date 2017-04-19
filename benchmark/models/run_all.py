"""
run_all.py

Run all the files stating with 'model' in the current directory

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

import glob
import importlib

# select all the files starting with 'model' in the current directory and sorts it
# just give the directory path to search in a different directory
# it also splits the filename from the extension. e.g., 'model1.py' to 'model1'
filtered_files = [file_name.split('.')[0] for file_name in sorted(glob.glob('model*.py'))]

# iterating and importing the file using importlib
for name in filtered_files:
    print '### ' + name.upper() + ' ###'
    importlib.import_module(name)
