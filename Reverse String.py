class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size=len(s)        
        n=size//2
        for i in range(n):        
            s[i],s[size-1-i]=s[size-1-i],s[i]
            
        print(s)