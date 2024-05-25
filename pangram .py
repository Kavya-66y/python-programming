import string
def is_pangram(sentence):
    sentence_lower = sentence.lower()
    alphabet_set = set(string.ascii_lowercase)
    for char in sentence_lower:
        if char in alphabet_set:
            alphabet_set.remove(char)
    return len(alphabet_set) == 0
sentence = 'The quick brown fox jumps over the lazy dog'
if is_pangram(sentence):
    print('the sentence is pangram')
else:
    print('the sentence is not a pangram')



 