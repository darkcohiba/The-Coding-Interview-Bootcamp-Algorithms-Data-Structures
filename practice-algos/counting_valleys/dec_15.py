import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    valleys = 0
    sea_lvl= 0
    in_valley = False

    for p in path:
        if p == 'D':
            sea_lvl -= 1
        elif p == 'U':
            sea_lvl += 1
        
        if sea_lvl < 0 and not in_valley:
            valleys += 1
            in_valley = True
        elif sea_lvl >= 0:
            in_valley = False
            
    return valleys

print(countingValleys(8, "DDUUUUDD"))