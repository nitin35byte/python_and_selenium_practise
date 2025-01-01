# Input: arr[] = [1, 2, 3, 4], k = 1
# Output: [3]
# Explanation: The highest marks is at index 3.

def classtopper(arr , k):
     # sorted_arr=sorted(arr, reverse=True)
     #
     # highet_elemt=sorted_arr[k-1]
     #
     # return arr.index(highet_elemt)
    index_arr =[(value , index) for index ,value in enumerate(arr)]

    sorted_arrya = sorted(index_arr , key=lambda  x: (-x[0], x[1]))

    index= [index for value , index in sorted_arrya[:k]]
    return index
arr= [2, 2, 1, 3, 1]
k = 3

print(classtopper(arr , k))