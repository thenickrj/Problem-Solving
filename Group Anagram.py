def anagrams(words):
    anagram={}
    for word in words:
        sortedWord="".join(sorted(word))
        if sortedWord in anagram:
            anagram[sortedWord].append(word)
        else:
            anagram[sortedWord]=[word]
    return list(anagram.values())

words=["tea","ate","eat","ban","tan","can"]
t=[]
print(anagrams(t))


