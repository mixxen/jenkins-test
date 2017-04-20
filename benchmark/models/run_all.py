"""
run_all.py

Run all the files stating with 'model' in the current directory

AlgorithmHub. All rights reserved.
https://www.algorithmhub.com/
"""

import glob
import importlib
import sys
import ast
import json


class Logger(object):
    """
    For logging in the output to a log file.
    """

    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass

sys.stdout = Logger()
# select all the files starting with 'model' in the current directory and sorts it
# just give the directory path to search in a different directory
# it also splits the filename from the extension. e.g., 'model1.py' to 'model1'
filtered_files = [file_name.split('.')[0] for file_name in sorted(glob.glob('model*.py'))]

# iterating and importing the file using importlib
for name in filtered_files:
    print '### ' + name.upper() + ' ###'
    importlib.import_module(name)

# To get the response of all the models
with open('logfile.log') as f:
    next = False
    all_results = {}
    for line in f:
        if next:
            all_results[model_name] = ast.literal_eval(line)
        if '###' in line:
            model_name = line.split()[1].lower()
        if 'RESPONSE' in line:
            next = True
        else:
            next = False

print 'Combined results in JSON'
print json.dumps(all_results, ensure_ascii=False)
