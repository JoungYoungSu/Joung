# Author: Joung Young Su
# Date: Nov.28.2020.
# Data Generating Program
# from CORE PHYTON APPLICATIONS PROGRAMMING 3RD EDITION pg81

from random import randrange, choice
from string import ascii_lowercase as lc
import struct
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')
# python3 doesn't have maxint func. So just made it!!
maxint = 2 ** (struct.Struct('i').size * 8 - 1) - 1

for i in range(randrange(5, 11)):
    dtint = randrange(maxint)
    dtstr = ctime(dtint)
    llen = randrange(4, 7)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d'
          % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))
