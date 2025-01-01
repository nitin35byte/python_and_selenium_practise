from collections import defaultdict


#arr= ["act", "god", "cat", "dog", "tac"]
def groupwords(arr):
    anagram_word={}
    for i in arr:
            sorted_word=''.join(sorted(i))
            if sorted_word in anagram_word:
                anagram_word[sorted_word].append(i)
            else:
                anagram_word[sorted_word]=[i]
    return list(anagram_word.values())
arr = ["cat", "dog", "tac", "god", "act"]
result = groupwords(arr)

# Output result
for group in result:
    print(group)
