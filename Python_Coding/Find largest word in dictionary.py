def find_largest_word(dictionary):
    # Initialize a variable to hold the largest word
    largest_word = ""

    # Iterate through each word in the dictionary
    for word in dictionary:
        # Check if the current word is longer than the largest found so far
        if len(word) > len(largest_word):
            largest_word = word  # Update the largest word

    return largest_word


# Example usage
dictionary = ["apple", "banana", "watermelon", "kiwi", "strawberry"]
largest_word = find_largest_word(dictionary)
print("The largest word in the dictionary is:", largest_word)
