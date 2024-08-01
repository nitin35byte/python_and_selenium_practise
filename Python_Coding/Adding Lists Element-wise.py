def add_lists(l1, l2):
    # Initialize variables
    carry = 0
    result = []

    # Reverse the lists to start adding from the least significant digit
    l1 = l1[::-1]
    l2 = l2[::-1]

    # Make sure both lists are of the same length by padding with zeros
    max_len = max(len(l1), len(l2))
    l1.extend([0] * (max_len - len(l1)))
    l2.extend([0] * (max_len - len(l2)))

    # Add corresponding elements and handle carry
    for i in range(max_len):
        total = l1[i] + l2[i] + carry
        result.append(total % 10)  # Append the last digit of total
        carry = total // 10  # Carry over the rest

    # If there's any carry left after the last addition, append it
    if carry:
        result.append(carry)

    # Reverse the result to get the correct order
    return result[::-1]


l1 = [2, 3, 4]
l2 = [5, 6, 4]
output = add_lists(l1, l2)
print(output)
