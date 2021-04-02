#Container With Most Water 

"""
Difficulty Level : Medium

Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of
the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Source : LeetCode
"""

def maxArea(h):
    f=0
    l=len(h)-1
    m=0 
    while(f!=l): #as long as the first and last doesn't collide.
    #Traverse the whole array to find the area with the maximum space that can contain the water
        print(min(h[f],h[l])*(l-f))
        if((min(h[f],h[l])*(l-f))>m):
            m=min(h[f],h[l])*(l-f)
            
        if(h[f]<h[l]):
            f+=1
        else:
            l-=1
    return m   
    
h= [1,8,6,2,5,4,8,3,7]    

print(maxArea(h))