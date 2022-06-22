

# def peak(arr):
#     length = len(arr)
#     found = False

#     for x in range(1,length-1):
#         if (arr[x-1] < arr[x] > arr[x+1]):

#             return x

def peak(arr):
    length = len(arr)
    found = False
    
    middle = length//2+1 # 3
    
    for x in range(1, middle): # 1,2
        if (arr[x-1] < arr[x] > arr[x+1]):
            return x
        elif arr[middle+x-2] < arr[middle+x -1] > arr[middle+x]:
            return middle+x-1
    # return middle

print(peak([0,3,4,5,1]))
