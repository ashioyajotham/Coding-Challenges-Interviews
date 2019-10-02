#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lastLetters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING word as parameter.
#

def lastLetters(word):
    # Write your code here

    return word[-1] + " " + word[-2]

if __name__ == '__main__':

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'generate_phrases' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY phrases as parameter.
#

def generate_phrases(phrases):
    # Write your code here

    parsedPhrases = {}
    result = []

    for phrase in phrases:
        tempPhrase = phrase.split(" ")
        start = tempPhrase[0]
        middle = " ".join(tempPhrase[1:-1])
        end = tempPhrase[-1]

        if start in parsedPhrases:
            parsedPhrases[start] += [(middle, end)]
        else:
            parsedPhrases[start] = [(middle, end)]

    for phrase in phrases:
        tempPhrase = phrase.split(" ")
        start = tempPhrase[0]
        middle = " ".join(tempPhrase[1:-1])
        end = tempPhrase[-1]
        
        if end in parsedPhrases:
            for matched in parsedPhrases[end]:

                if middle == "" and matched[0] == "":
                    newPhrase =  " ".join([start, end, matched[1]])
                elif matched[0] == "":
                    newPhrase =  " ".join([start, middle, end, matched[1]])

                elif middle == "":
                    newPhrase =  " ".join([start, end, matched[0], matched[1]])
                else:    
                    newPhrase =  " ".join([start, middle, end, matched[0], matched[1]])

                result += [newPhrase]


    return result


if __name__ == '__main__':