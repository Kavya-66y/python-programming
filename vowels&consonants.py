s = input('enter a string')
vowel = 0
consonant = 0
digit = 0
special = 0
vowels = 'aeiou'
digits = '0123456789'
specials = '@#$%&^*!'
for i in s:
    if i in vowels:
        vowel += 1
    elif i not in digits and i not in specials:
        consonant += 1
    elif i in digits:
        digit += 1
    else:
        special += 1
print('vowels are:',vowel, '\n' 'consonants are:',consonant,'\n' 'digits are:',digit,'\n' 'specials are:',special)