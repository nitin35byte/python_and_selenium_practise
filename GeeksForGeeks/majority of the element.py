def majorityelement(nums):
    majority = {}  # Dictionary to store the frequency of each element

    for num in nums:  # Iterate through each number in the list
        # Update the frequency of the current number in the dictionary
        majority[num] = majority.get(num, 0) + 1

        # Check if the frequency of the current number exceeds half the list length
        if majority[num] > len(nums) // 2:
            return num  # If yes, return the number as the majority element
    return -1

nums = [3,1,3 , 3 ,1]
m1=majorityelement(nums)
print(m1)


def majority_element(nums):
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
nums = [3,1,3 , 3 ,1]
m2=majorityelement(nums)
print(m2)