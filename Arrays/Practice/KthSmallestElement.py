'''
Given an array arr[] and an integer k where k is smaller than the size of the array, your task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.
'''

#Brute

def k_smallest_brute(arr,k):
    uniq = set(arr)
    new_arr = list(uniq)
    new_arr.sort()
    print(new_arr[k])
# TC - o(n log n) sc - o(n)

#Heaps Notes - https://colab.research.google.com/drive/1vUROF93_7r8hP3_Q9PjOWCgIEdiDpLae?usp=sharing  Video - https://www.youtube.com/watch?v=E2v9hBgG6gE&t=1s

import heapq

def k_smallest_optimal(arr,k):
    heapq.heapify(arr) # Tc - o(N)
    min_k = float('inf')
    for _ in range(0,k):
        min_k = heapq.heappop(arr) # One pop log n, therefore k log N
    print(min_k)

#Better approach
def k_largest_better(arr,k):
    n = len(arr)
    heapq.heapify(arr)
    max_k = float('-inf')
    for _ in range(0,n-k+1):
        max_k = heapq.heappop(arr)

    print(max_k)


#Optimal approach

def k_largest_optimal(arr,k):
    min_heap = []

    for i in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, i)
        else:
            heapq.heappushpop(min_heap,i)

    return min_heap[0]
# t - o(N log K) s - O(k)

arr = [7, 10, 4, 3, 20, 15]
k = 3
k_largest_optimal(arr,k)
