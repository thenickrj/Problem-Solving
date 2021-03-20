#Leaders in an array


#Scan all the elements from right to left in an array
#and keep track of maximum till now.
#When maximum changes its value, print it.
def leader(arr):
    size=len(arr)
    max_from_right=arr[size-1]
    print(max_from_right,end=" ")
    for i in range(size-1,-1,-1):
        #print(i,end=" ")
        if arr[i]>max_from_right:
            print(arr[i],end=" ")
            max_from_right=arr[i]

arr=[16,17,4,3,5,2]
leader(arr)

#Time Complexity: O(n)
