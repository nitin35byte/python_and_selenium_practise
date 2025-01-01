# Input: arr1 = [1, 2, 4, 6, 10], arr2 = [4, 5, 6, 9, 12]
# Output: 11

def middleElementSum(arr1 , arr2):

    arr1 = sorted(arr1)
    arr2= sorted(arr2)
    arr3 =  sorted(arr1 +arr2)
    #middle =arr3[len(arr3)//2] if len(arr3) %2 != 0 else arr3[len(arr3) //2-1]
    # for odd
    if len(arr3) %2 != 0:
        middle = arr3[len(arr3)//2]
        subofmiddlearrya=middle
    # for even
    else:
        mid1=arr3[len(arr3) // 2 - 1]
        mid2=arr3[len(arr3) //2]
        subofmiddlearrya=mid1 +mid2
    # middleplus1 = middle+1
    # sumofmiddlearray = middle +middleplus1

    return f"Sum of Middle array is :{subofmiddlearrya}"


# arr1 = [1, 2, 4, 6, 10]
# arr2 = [4, 5, 6, 9, 12]
arr1 = [1, 12, 15, 26, 38, 4]
arr2 = [2, 13, 17, 30, 45]
print(middleElementSum(arr1 , arr2))
#1 , 2 , 4,12  , 13, 15 , 17 , 26  , 30 , 38 , 45