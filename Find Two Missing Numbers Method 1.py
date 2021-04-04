def findTwoMissingNumbers1(arr, n):
    print("Two Missing Numbers are")

    for i in range(1, n + 1):
        if i not in arr:
            print(i, end=" ")


# ------------END OF FIRST METHOD---------------

# arrSum => Sum of all elements in the array

# sum (Sum of 2 missing numbers) = (Sum of integers from 1 to n) - arrSum
#                               = ((n)*(n+1))/2 – arrSum

# avg (Average of 2 missing numbers) = sum / 2;

# Input : 1 3 5 6, n = 6
# Sum of missing integers = n*(n+1)/2 - (1+3+5+6) = 6.
# Average of missing integers = 6/2 = 3.
# Sum of array elements less than or equal to average = 1 + 3 = 4
# Sum of natural numbers from 1 to avg = avg*(avg + 1)/2
#                                      = 3*4/2 = 6
# First missing number = 6 - 4 = 2
# Second missing number = Sum of missing integers-First missing number
# Second missing number = 6-2= 4

# Returns the sum of the array
def getSum(arr, n):
    sum = 0;
    for i in range(0, n):
        sum += arr[i]
    return sum


# Function to find two missing
# numbers in range [1, n]. This
# function assumes that size of
# array is n-2 and all array
# elements are distinct

def findTwoMissingNumbers2(arr, n):
    # Sum of 2 Missing numbers
    sum = ((n * (n + 1)) / 2 - getSum(arr, n - 2))

    # Find average of two elements
    avg = (sum / 2)

    # Find sum of elements smaller
    # than average (avg) and sum
    # of elements greater than average
    sumSmallerHalf = 0
    sumGreaterHalf = 0
    for i in range(0, n - 2):
        if arr[i] <= avg:
            sumSmallerHalf += arr[i]
        else:
            sumGreaterHalf += arr[i]
    print("Two Missing Numbers are")

    # The first (smaller) element = (sum
    # of natural numbers upto avg) - (sum
    # of array elements smaller than or
    # equal to avg)
    totalSmallerHalf = (avg * (avg + 1)) / 2
    print(totalSmallerHalf -
          sumSmallerHalf + " ")

    # The first (smaller) element = (sum
    # of natural numbers from avg+1 to n) -
    # (sum of array elements greater than avg)
    print(str(((n * (n + 1)) / 2 -
               totalSmallerHalf) -
              sumGreaterHalf))


arr = [1, 3, 5, 6]
n = 6
findTwoMissingNumbers1(arr, n)
# findTwoMissingNumbers2(arr,n)