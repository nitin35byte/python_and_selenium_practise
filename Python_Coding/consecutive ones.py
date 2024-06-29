def max_consecutive_ones(nums):
    max_count = 0  # Initialize the maximum count of consecutive ones
    count = 0  # Initialize the current count of consecutive ones

    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)  # Update the maximum count if needed
        else:
            count = 0  # Reset the count if the current number is not 1

    return max_count


# Test the function
binary_array = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print("Maximum consecutive ones:", max_consecutive_ones(binary_array))
