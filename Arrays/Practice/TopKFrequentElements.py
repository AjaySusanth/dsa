'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

'''

# Brute
'''
Store the frequency of each elt in dict
sort the dict by frequency(desc)
return the values of first k elts
'''

def top_k_frequent_brute(arr,k):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    sorted_freq =sorted(freq.items(),reverse=True,key= lambda item:item[1])

    ret = []
    for i in range(k):
        ret.append(sorted_freq[i][0])

    print(ret)

    # t - o (n + nlogn) sc- O(n + k) k - to return the ans

# Better
from collections import Counter
import heapq
def top_k_frequent_better(arr,k):
    freq = Counter(arr)

    heap = []

    for key,value in freq.items():
        if len(heap) < k:
            heapq.heappush(heap,(value,key))
        else:
            heapq.heappushpop(heap,(value,key))

    print([item[1] for item in heap])

    # t - O(n + nlogk) sc - O(k) - heap arr


#Optimal
'''
Find the occurences of each elt

Create an array and map the elts to the array in such a way that the elt is mapped to index which is its value. 

Since an arr can have max occurence of an elt  that would be equal to the size of the arr, initialize the array of size n+1 with 0

Insert the elt as an arr, so that if multiple elt have same occurence they can be stored as arr.

Create a ret arr, iterate from back whose value is not zero, then extend to ret array until the len of return arr is k


'''
def top_k_frequent_optimal(arr,k):
    n = len(arr)

    counter = Counter(arr)

    buckets = [0] * (n+1)

    for num,freq in counter.items():
        if buckets[freq] == 0:
            buckets[freq] = [num]
        else:
            buckets[freq].append(num)
    
    ret = []
    for i in range(n,-1,-1):
        if buckets[i]!=0:
            ret.extend(buckets[i])
        if len(ret) >= k : # if multiple elts have same freq and extends the k
            break
    print(ret)



nums = [1,1,1,2,2,3]
k = 2

top_k_frequent_optimal(nums,k)