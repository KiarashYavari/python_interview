# input >>> words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# expected output >>> [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]
# Anagrams contain the same letters with the same counts
# key = something that identifies the group
# value = all items belonging to that group
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}
    for word in words:
      anagram_match = "".join(sorted(word))
      if anagram_match in groups:
        groups[anagram_match].append(word)
      else:
        groups[anagram_match] = [word]
    return list(groups.values())

print(group_anagrams(words=words))
