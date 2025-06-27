#BRUTE FORCE APPROACH

'''
Find the largest element in one pass
Find the second largest by finding the greatest element which is not the largest.
'''
def getElements(arr,n):
    largest = float('-inf')
    for i in range(n):
        if arr[i]>largest:
            largest = arr[i]
    
    sec_largest = float('-inf')
    for i in range(0,n):
        if arr[i]> sec_largest and arr[i]!=largest:
            sec_largest = arr[i]
    
    print(sec_largest)

# Optimal approach
'''
If the element is greater than largest, then largest becomes slargest. If it is not equal to largest and greater than slargest, it becomes slargest

'''

def optimal(arr,n):
    largest = float('-inf')
    slargest = float('-inf')
    for i in range(n):
        if arr[i]>largest:
            slargest = largest
            largest = arr[i]
        elif arr[i]!=largest and arr[i] > slargest:
            slargest = arr[i]
    
    print(slargest)


if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    n = len(arr)
    getElements(arr, n)
    optimal(arr, n)