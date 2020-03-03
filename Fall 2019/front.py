Write a function to return a boolean if a word is splittable.
For example, isdogread is splittable, because is dog and read are words.
idsogb is not splittable, because there isn’t a way to split it into words.
Assume you are given a function isWord that returns true / false for whether the word is valid.

owiofwefwordioweoiew
is word dog

todo

def splittable(word):
  i = 0
  
  while i < len(word):
    j = i
    while (j < len(word)):
      if (isWord(word[i:j])):
        i = j
        break
      else:
        j += 1
        
        
def splittable2(word, lookup=dict()):
  if word == "":
    return True
  i = 1
  while (i < len(word)):
    if (word[:i] in lookup and lookup[word[:i]])
    	return true
    if (isWord(word[:i])):
      isSplittable = splittable2(word[i:], lookup)
      lookup[word[:i]] = isSplittable
      return isSplittable
    else:
      lookup[word[:i]] = False
      i += 1
  
  return False
           
  
  t 1
  
  to 2
  
iod 4
i o d
i od
io d

iodn 8

i odn
io dn
iod n
idon
i od n
i o d n
i o dn
io d n


    
    