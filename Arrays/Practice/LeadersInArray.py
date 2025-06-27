'''
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.

https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
'''

# Brute

def brute(arr):
    n =len(arr)
    leaders = []
    for i in range(n):
        leader = True
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                leader = False
                break
        if leader:
            leaders.append(arr[i])
    return leaders


#Optimal

def optimal(arr):
    n = len(arr)
    maxi = float('-inf')
    leaders = []
    for i in range(n-1,-1,-1):
        if arr[i] > maxi:
            maxi = arr[i]
            leaders.append(arr[i])

    return leaders

arr = [16, 17, 4, 3, 5, 2]
print(brute(arr))
print(optimal(arr))