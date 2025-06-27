# Maximum and minimum elt of an array

#Brute

def max_min_brute(arr):
    arr.sort()
    max_elt = arr[-1]
    min_elt = arr[0]

    print(max_elt,min_elt)
    return max_elt,min_elt

# Tc - o(n log n)  sc - o(1)

def max_min_optimal(arr):
    max_elt = float('-inf')
    min_elt = float('inf')

    for i in arr:
        if i > max_elt:
            max_elt = i
        if i < min_elt:
            min_elt = i

    print(max_elt,min_elt)
    return max_elt,min_elt

# tc - O(n) sc-O(1)

arr = [3,5,4,1,9]
max_min_optimal(arr)

