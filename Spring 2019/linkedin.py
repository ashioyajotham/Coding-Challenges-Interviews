/**
 * Given a nested list of integers, returns the sum of all integers in the list weighted by their depth
 * For example, given the list {{1,1},2,{1,1}} the function should return 10 (four 1's at depth 2, one 2 at depth 1)
 * Given the list {1,{4,{6}}} the function should return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3)
 */
def depthSum (nested_list)
{
    //Implementation here

    def helper(nested_list, depth, result):

        # if nested_list.isInteger():
        #     return nested_list.getInteger() * depth
        
        # elif 

        for lst in nested_list:
            if lst.isInteger():
                result.append(lst.getInteger() * depth)
            
            else:
                helper(lst.getList(), depth + 1, result)

        return result

    return sum(helper(nested_list, 1, []))
}

public int depthSum (List<NestedInteger> input)
{
    //Implementation here
}
 
 public interface NestedInteger
{
    /** @return true if this NestedInteger holds a single integer, rather than a nested list */
    boolean isInteger();
 
    /** @return the single integer that this NestedInteger holds, if it holds a single integer
     * Return null if this NestedInteger holds a nested list */
    Integer getInteger();
 
    /** @return the nested list that this NestedInteger holds, if it holds a nested list
     * Return null if this NestedInteger holds a single integer */
    List<NestedInteger> getList();
}


/**
 * Given a nested list of integers, returns the sum of all integers in the list weighted by their reversed depth.
 * For example, given the list {{1,1},2,{1,1}} the deepest level is 2. Thus the function should return 8 (four 1's with weight 1, one 2 with weight 2)
 * Given the list {1,{4,{6}}} the function should return 17 (one 1 with weight 3, one 4 with weight 2, and one 6 with weight 1)
 */

 def depthSum (nested_list)
{
    //Implementation here

    def helper(nested_list, depth, result):

        # if nested_list.isInteger():
        #     return nested_list.getInteger() * depth
        
        # elif 

        for lst in nested_list:
            if lst.isInteger():
                result.append([lst.getInteger(),  depth])
            
            else:
                helper(lst.getList(), depth + 1, result)

        return result

    result = helper(nested_list, 1, [])
    depths = [result[i][1] for i in range(len(result))]
    # depths.sort()
    # depths = depths[::-1]
    max_depth = max(depths)

    return sum([result[i][0] * (max_depth - result[i][1]) for i in range(len(result))])
}




'''
NOTE array are *SORTED*
find_range({0 2 3 3 3 10 10},  3) should return (2,4).
    -begin = largest element that is smaller than t
    -end = smallest element that is larget than t
find_range({0 2 3 3 3 10 10},  6) should return (-1,-1).
'''

def find_range(lst, target):

    start = binarySearch(lst, 0, len(lst) - 1, target - 1)
    end = binarySearch(lst, 0, len(lst) - 1, target + 1) # target + 1??

    return (start, end)
// std::lower_bound c++


    return (-1, -1)
//0 2 3 3 3 10 10
//      m
//      3  3 10 10
//         m
//         3  10 10

def binarySearch(array, left, right, target):

    if right >= left:

        #do binary search

    else:
        return left


print('Hello world - Python!')
‘’‘

2d of integers

1 0 0 0
1 1 1 0
1 0 0 0
0 0 0 0 return 1

1 0 0 0
1 1 1 0
1 0 0 0
0 1 1 1 return 2


1 0 0 0 1 0
1 1 1 0 1 0
1 0 0 0 0 0
0 0 0 0 0 0
1's are continuous if they are adjacent via a left, right, up, or down move, but not diagonal

’‘’

def find_islands(array):
    visited = set()
    count = 0
    for x in range(len(array)):
        start = None
        for y in len(array[x]):
            if array[x][y] == 1:
                start = [x, y]

                result = dfs(array, start)

                if result not in visited:
                    visited.add(result)
                    count += 1
                
        if start == None:
            continue

    return count



def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        position = stack.pop()
        if position not in visited:
            visited.add(position)

            if position[0] - 1 >= 0 and array[position[0] - 1][position[1]] == 1:
                stack += [[position[0] - 1], position[1]]

            if position[0] + 1 < len(array) and array[position[0] + 1][position[1]] == 1:
                stack += [[position[0] + 1], position[1]]
            
            if position[1] - 1 >= 0 and array[position[0]][position[1] - 1] == 1:
                stack += [[position[0], position[1] - 1]

            if position[1] + 1 < len(array) and array[position[0][position[1] + 1] == 1:
                stack += [[position[0]], position[1] + 1]

    return visited