def max_consecutive_one(arr,n):
    max=0
    count=0
    for i in range(0,n):
        if arr[i]!=1:
            count=0
            continue
        else:
            count+=1
        if max < count:
            max=count

    return max


nums = [1, 1, 0, 1, 1, 1]
n= 6
print(max_consecutive_one(nums,n))