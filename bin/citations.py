#!/usr/bin/env python
import os
import subprocess
import re
from shutil import copyfile

class bibtex(object):

    @staticmethod    
    def citations(s):
        citations = re.findall(':cite:`.*`', s)
        return citations

    @staticmethod
    def scan(name):
        s = open(name).read()
        return bibtex.citations(s)
        
    @staticmethod
    def print(citations, file=None):
        if citations is not None:
            for cite in citations:
                if file is not None:
                    print (cite, file)
                else:
                    print (cite)

    def find_files(directory='./'):
        files = set()
        entry = []
        DOCUMENTATION_SOURCE_DIR = './'
        SOURCE_EXTENSION = '.rst'

        for root, dirs, filenames in os.walk(DOCUMENTATION_SOURCE_DIR):
            for filename in filenames:

                if filename.endswith(SOURCE_EXTENSION) and '.#' not in filename:
                    source_file = os.path.join(root, filename)
                    citations = bibtex.scan(source_file)
                    for citation in citations:
                        entry.append((citation, source_file))
                        files.add(source_file)
        return files, entry
                    

files, entry = bibtex.find_files()
for file in files:
    ref = "./docs/source/refs.bib"
    bib = file.replace(".rst", "-tmp.bib")
    
    print (ref, bib)
    copyfile(ref, bib)

"""
DOCUMENTATION_SOURCE_DIR = './'
SOURCE_EXTENSION = '.rst'

for root, dirs, filenames in os.walk(DOCUMENTATION_SOURCE_DIR):
    for filename in filenames:

        if filename.endswith(SOURCE_EXTENSION) and '.#' not in filename:
            # print (root, dirs, filename)
            source_file = os.path.join(root, filename)
            #source_time = os.path.getmtime(source_file)
            # try:
            #    output_time = os.path.getmtime(output_file)
            # except:
            #    output_time = source_time + 1
                
            #if (source_time > output_time):
            citations = bibtex.scan(source_file)

            bibtex.print(citations, source_file)
            
"""
