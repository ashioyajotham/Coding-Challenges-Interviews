#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'barterMarket' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER comicBooks
#  2. INTEGER coins
#  3. INTEGER coinsNeeded
#  4. INTEGER coinsOffered
#

def barterMarket(comicBooks, coins, coinsNeeded, coinsOffered):
    # Write your code here
    total_fiction = 0

    while (comicBooks > 0 and coins >= coinsNeeded):
        total_fiction += 1
        comicBooks -= 1
        coins -= coinsNeeded

        while(coins < coinsNeeded and comicBooks > 0):
            comicBooks -= 1
            coins += coinsOffered
  
  	# too slow :(
    # canTrade = coins // coinsNeeded
    # total_fiction += min(canTrade, comicBooks)
    # comicBooks -= min(canTrade, comicBooks)
    # coins -= coinsNeeded * canTrade
    

    # if (comicBooks > 1):
    #     print('can sell to get more money')
    #     coins += (comicBooks * coinsOffered)
    #     canTrade = coins // coinsNeeded

    #     total_fiction += min(canTrade, comicBooks)
    #     comicBooks -= min(canTrade, comicBooks)


    return total_fiction    

    
if __name__ == '__main__':



#!/bin/python3

import sys
import os
from urllib.request import Request
from urllib.request import urlopen
from urllib.error import URLError
import json


# Complete the function below.
# Base url: https://jsonmock.hackerrank.com/api/movies/search/?Title=

import json
import http.client

def  getMovieTitles(substr):
    titles = []
    conn = http.client.HTTPSConnection('jsonmock.hackerrank.com')
    conn.request("GET", '/api/movies/search/?Title=' + substr)
    resp = conn.getresponse()
    
    data = json.loads(resp.read())

    if data['total_pages'] > 1:
        print('more than one page')
        for i in range (1, data['total_pages'] + 1):
            conn.request("GET", '/api/movies/search/?Title=' + substr + '&page=' + str(i))
            resp = conn.getresponse()

            temp = json.loads(resp.read())

            for d in temp['data']:
                titles += [d['Title']]
        
        titles.sort()
        return titles
        
    
    else:
        for d in data['data']:
            titles += [d['Title']]
        
        titles.sort()
        return titles

f = open(os.environ['OUTPUT_PATH'], 'w')
    

try:
    _substr = str(input())
except:
    _substr = None

res = getMovieTitles(_substr)
for res_cur in res:
    f.write( str(res_cur) + "\n" )

f.close()







#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'restock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY itemCount
#  2. INTEGER target
#

def restock(itemCount, target):
    # Write your code here
    total = 0
    i = 0
    temp = target
    while (temp > 0 and i < len(itemCount)):
        total += itemCount[i]
        temp -= itemCount[i]
        i += 1

    
    return abs(total - target)
if __name__ == '__main__':
