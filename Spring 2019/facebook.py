# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = dict()
        
        max_depth = -1
        
        stack = [(root, 0)]
        
        while (stack):
            node, depth = stack.pop()
            
            if node is not None:
                max_depth = max(depth, max_depth)
                
                result.setdefault(depth, node.val)
                
                
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
                
        return [result[depth] for depth in range(max_depth + 1)]




"""
Input: "()())()"
Output: ["()()()", "(())()"]


Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).
"""

class Solution:
    def removeInvalidParentheses(self, s):
        self.ans = set()
        self.min_removed = float("inf")

        def dfs(depth, left, right, removed, cur):
            if depth == len(s):
                if left == right:
                    if removed < self.min_removed:
                        self.min_removed = removed
                        self.ans = {cur}
                    elif removed == self.min_removed:
                        self.ans.add(cur)
            else:
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth + 1, left, right, removed, cur + s[depth])
                else:
                    dfs(depth + 1, left, right, removed + 1, cur)
                    if s[depth] == "(":
                        dfs(depth + 1, left + 1, right, removed, cur + "(")
                    elif s[depth] == ")" and right < left:
                        dfs(depth + 1, left, right + 1, removed, cur + ")")

        dfs(0, 0, 0, 0, "")
        return list(self.ans)



# public class Solution {
#     ArrayList<String> result = new ArrayList<String>();
#     int max=0; 
 
#     public List<String> removeInvalidParentheses(String s) {
#         if(s==null)
#             return result;
 
#         dfs(s, "", 0, 0);
#         if(result.size()==0){
#             result.add("");
#         }
 
#         return result;
#     }
 
#     public void dfs(String left, String right, int countLeft, int maxLeft){
#         if(left.length()==0){
#             if(countLeft==0 && right.length()!=0){
#                 if(maxLeft > max){
#                     max = maxLeft;
#                 }
 
#                 if(maxLeft==max && !result.contains(right)){
#                     result.add(right);
#                 }
#             }
 
#             return;
#         }
 
#         if(left.charAt(0)=='('){
#             dfs(left.substring(1), right+"(", countLeft+1, maxLeft+1);//keep (
#             dfs(left.substring(1), right, countLeft, maxLeft);//drop (
#         }else if(left.charAt(0)==')'){
#             if(countLeft>0){
#                 dfs(left.substring(1), right+")", countLeft-1, maxLeft);
#             }
 
#             dfs(left.substring(1), right, countLeft, maxLeft);
 
#         }else{
#             dfs(left.substring(1), right+String.valueOf(left.charAt(0)), countLeft, maxLeft);
#         }
#     }
# }