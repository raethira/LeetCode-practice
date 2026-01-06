class Solution:
    def stackPopForPeriod(self, stack):
        while stack and stack[-1] != '/':
            stack.pop()
          
        return stack
    
    def simplifyPath(self, path: str) -> str:
        
        components = path.split("/")        
        stack = []
        
        for c in components:
            if c == "" or c == ".":
                continue
            if c == "..":
                if stack: 
                    stack.pop()
            else:
                stack.append(c)
            
        return "/" + "/".join(stack)
    
        # Video soltuion here: https://leetcode.com/problems/simplify-path/solutions/6210383/video-stack-solution/
        
                
