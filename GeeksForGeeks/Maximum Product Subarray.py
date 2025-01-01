def max_product(nums):
    if not nums:
        return 0

    # Initialize the variables to the first element
    max_prod = min_prod = result = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        # If the current number is negative, swap max_prod and min_prod
        if num < 0:
            max_prod, min_prod = min_prod, max_prod

        # Update max_prod and min_prod
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)

        # Update the result with the maximum product found so far
        result = max(result, max_prod)

    return result



nums = [2, 3, 4]
print(max_product(nums))
