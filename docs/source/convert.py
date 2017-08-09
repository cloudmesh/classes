#!/usr/bin/env python
import os
import subprocess

DOCUMENTATION_SOURCE_DIR = './'
SOURCE_EXTENSION = '.md'
OUTPUT_EXTENSION = '.rst'

for root, dirs, filenames in os.walk(DOCUMENTATION_SOURCE_DIR):
    for filename in filenames:

        if filename.endswith(SOURCE_EXTENSION):
            # print (root, dirs, filename)
            source_file = os.path.join(root, filename)
            output_file = os.path.join(root, filename.replace(SOURCE_EXTENSION, OUTPUT_EXTENSION))
            source_time = os.path.getmtime(source_file)
            output_time = os.path.getmtime(output_file)
            if (source_file > output_file):

                command = 'pandoc -s {0} -o {1}'.format(source_file, output_file)
                print(command)
                subprocess.call(command.split(' '))
