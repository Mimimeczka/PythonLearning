def is_anagram(messageA, messageB):
    return sorted(messageB.replace(" ", "")) == sorted(messageA.replace(" ", ""))
