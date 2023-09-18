#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
#

def stringmethod(para, special1, special2, list1, strfind):
    # Write your code here
    word1 = ""
    for i in para:
        if i in special1:
            word1.replace(i,"")
        else:
            continue
    print(word1)
    
    rword2 = word1[0:70:-1]
    print(rword2)
    
    print(special2.join(rword2))
    
    for i in list1:
        if i in para:
            print('Every string in {0} were present'.format(list1))
        else:
            print('Every string in {0} were not present'.format(list1))
        
    print(list(word1)[0:20])
    
    sp = word1.split()
    l = []
    for i in sp:
        if sp.count() < 3:
            l.append()
        else:
            continue
            
    if strfind in word1:
        print(len(word1)-1)

    
        
        
    
    

if __name__ == '__main__':
    para = input()

    spch1 = input()

    spch2 = input()
    
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)

    strf = input()

    stringmethod(para, spch1, spch2, qw1, strf)
