import os
import re

def command(cmd):
    raw_output = os.popen(cmd).readlines()
    matrix = []
    
    for line in raw_output:
        line = line.strip()
        output = re.split('[\/,;\s]', line)
        matrix.append(output)
        
    return matrix
