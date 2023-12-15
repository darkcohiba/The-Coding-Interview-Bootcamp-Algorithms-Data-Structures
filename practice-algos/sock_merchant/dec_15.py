
import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    socks = {}
    for sock in ar:
        if sock not in socks:
            socks[sock] = 1
        else:
            socks[sock] += 1
    count = 0
    for num in socks.values():
        count += num // 2
    return count


print(sockMerchant(7, [1, 2, 1, 2, 3, 1, 2]))