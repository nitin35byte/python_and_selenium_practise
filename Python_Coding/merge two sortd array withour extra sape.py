def merge_arrays(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    # Iterate through all elements of arr2[] starting from
    # the last element
    for i in range(n - 1, -1, -1):
        # Find the smallest element greater than arr2[i].
        # Move all elements one position ahead till the smallest
        # greater element is not found
        last = arr1[m - 1]
        j = m - 2
        while (j >= 0 and arr1[j] > arr2[i]):
            arr1[j + 1] = arr1[j]
            j -= 1

        # If there was a greater element
        if (j != m - 2 or last > arr2[i]):
            arr1[j + 1] = arr2[i]
            arr2[i] = last


# Example usage
arr1 = [1, 4, 7, 8, 10]
arr2 = [2, 3, 9]
merge_arrays(arr1, arr2)
print("Merged array 1:", arr1)
print("Merged array 2:", arr2)
