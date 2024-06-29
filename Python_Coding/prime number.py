l = [2,3,5,-1,9,4]
max_ele=max(l)
print(max_ele)
for i in l:
    if i >= max_ele:
        print(i)


def find_subarray(l):
    max_ele = max(l)  # Maximum element in the list
    left = right = 0  # Initialize the left and right pointers
    max_sum = float('-inf')  # Initialize the maximum sum of the subarray
    current_sum = 0  # Initialize the current sum of the subarray

    while right < len(l):
        current_sum += l[right]  # Expand the window
        while current_sum < max_ele:  # Move the left pointer until current sum >= max element
            if left < right:
                current_sum -= l[left]  # Adjust current sum
                left += 1
            else:
                break
        if current_sum >= max_ele and current_sum > max_sum:  # Update max sum and subarray indices
            max_sum = current_sum
            subarray_indices = (left, right)
        right += 1

    return l[subarray_indices[0]:subarray_indices[1] + 1] if max_sum != float('-inf') else None


# Test the function
l = [2, 3, 5, -1, 9]
print("Subarray:", find_subarray(l))
