# // Let's model the Social Network with up to 10 users. Code this out in your favorite language.
# // 1.3.1 How will we handle adding new users, removing existing users?  O(n), O(n)
# // 1.3.2 Given users X and Y, print out "Friends" if they are connected by less than or equal to 
# // 1-degree of separation -  mutual friends, or "Strangers" if there is more than 1-degree 
# // separation in the connection

# // Sample Friends List:
# // i. A is friends with C, D
# // ii. C is friends with D, A
# // iii. D is friends with E, C, A
# // iv. E is friends with B, D

# // Q1: Are A and B friends? (Strangers) A-D-E-B
# // Q2: Are A and E friends? (Friends) A-D-E

# // Map<String, HashSet>
# // {
# //   A -> [C, D]
# //   B -> [E]
# //   C -> [A, D]
# //   D -> [A, C, E]
# //   E -> [B, D]
# // }


# 1-degree => O(n)
# k-degrees => O(n ^ k)
# visited nodes => Set
def areFriends(x, y): # O(n)
    x_friends = users[x] # [A, B]
    
    if y in x_friends: # O(1)
        return True
    
    for user in x_friends: # O(n)
        user_friends = users[user]
        
        if y in user_friends: # O(1)
            return True
            
    return False