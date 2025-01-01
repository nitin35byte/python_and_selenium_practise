def longestConsecutive(arr):
    if not arr:
        return 0

    # Convert the array to a set to handle duplicates and for O(1) lookups
    arr_set = set(arr)
    longest_streak = 1

    for num in arr_set:
        if num-1 not in arr_set:
            current_num= num
            current_streak=1

            while current_num+1 in arr_set:
                current_num +=1
                current_streak +=1

            longest_streak= max(longest_streak , current_streak)
    return longest_streak

arr = [100, 4, 200, 1, 3, 2]
solution = longestConsecutive(arr)
print("Length of longest consecutive subsequence:",solution)