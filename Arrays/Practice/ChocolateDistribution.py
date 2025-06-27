'''
Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets among m students such that -
      i. Each student gets exactly one packet.
     ii. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and return that minimum possible difference.

     https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1
'''

#Sliding window - fixed length

def chocolate_distribution(arr,m):
    maxx = float('-inf')
    minn = float('inf')
    min_diff = float('inf')
    arr.sort()

    i=0
    for j in range(i+(m-1),len(arr)):
        minn = arr[i]
        maxx = arr[j]
        min_diff = min(min_diff,maxx - minn)
        i+=1

    return min_diff
     # t - O(n log n) 
arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(chocolate_distribution(arr,m))
        
