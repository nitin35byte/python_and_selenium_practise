def findTriplets(arr):
    arr.sort()  # Step 1: Sort the array
    n = len(arr)
    triplets = []

    for i in range(n - 2):  # Fix the first element
        # Skip duplicates for the anchor
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        # Initialize two pointers
        left, right = i + 1, n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                triplets.append([arr[i], arr[left], arr[right]])

                # Move left pointer to the next distinct number
                while left < right and arr[left] == arr[left + 1]:
                    left += 1

                # Move right pointer to the previous distinct number
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                # Move both pointers
                left += 1
                right -= 1

            elif total < 0:
                left += 1  # Increase sum by moving the left pointer right
            else:
                right -= 1  # Decrease sum by moving the right pointer left

    return triplets
arr= [0, -1, 2, -3, 1]
print(findTriplets(arr))


###https://leetcode.com/discuss/interview-question/3164322/60-Recently-asked-problems-in-D.E-Shaw-in-last-6-months?utm_source=chatgpt.com