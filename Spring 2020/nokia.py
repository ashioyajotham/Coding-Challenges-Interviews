def LongestIncreasingSequence(arr):

  # code goes here
  if arr == []:
    return 0
  
  result = [1] * len(arr)

  for i in range(1, len(arr)):

    for j in range(i):
      if arr[i] > arr[j]:
        result[i] = max(result[j] + 1, result[i])
  
  return max(result)

# keep this function call here 
print(LongestIncreasingSequence(input()))



def KUniqueCharacters(str):

  # code goes here
  k = int(str[0])
  str = str[1:]

  if k == 0 or len(str) == 0:
    return ""

  count = {}
  start = 0
  longestStr = ''
  
  for i in range(len(str)):
    count[str[i]] = count.get(str[i], 0) + 1

    while start <= i and len(count) > k:
      count[str[start]] -= 1

      if count[str[start]] == 0:
        count.pop(str[start])

      start += 1
    
    if i - start + 1 > len(longestStr):
      longestStr = str[start: i + 1]
  return longestStr

# keep this function call here 
print(KUniqueCharacters(input()))