def favoriteVideoGenre(numUsers, userVideosWatched, numGenres, videoGenres):
    # WRITE YOUR CODE HERE
    
    wordToGenre = dict()
    
    result = dict()
    
    for genre in videoGenres.keys():
        for title in videoGenres[genre]:
            wordToGenre[title] = genre
            
    
    for name in userVideosWatched.keys():
        userDict = dict()
        userResult = []
        
        for title in userVideosWatched[name]:
            
            if(title not in wordToGenre):
                continue
            
            if (wordToGenre[title] not in userDict):
                userDict[wordToGenre[title]] = 1
            else:
                userDict[wordToGenre[title]] += 1
                
        tupleLst = sorted(userDict.items(), key=lambda x: x[1], reverse=True)
            
        if tupleLst != []:
            userMax = tupleLst[0][1]
            
            for tuple in tupleLst:
                if (tuple[1] == userMax):
                    userResult += [tuple[0]]
                else:
                    break
                
        result[name] = userResult
                
  
    return result
        
        
        
        
    