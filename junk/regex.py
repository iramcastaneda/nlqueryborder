__author__ = 'Administrator'

import re

found=re.findall("abc","abc")
found2=re.search("abc","abc")
if(len(found)>0):
    print("encontrado")
    print(found[0])
