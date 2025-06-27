'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''

#Brute

def contains_dup_brute(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                return True
                break
    return False

    # t - O(n^2)

def contains_dup_optimal(arr):
    uniq = set()
    for i in arr:
        if i in uniq:
            return True
            break
        uniq.add(i)
        



nums = [1,2,3,1]
print(contains_dup_brute(nums))