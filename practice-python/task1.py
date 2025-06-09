vowel = 'aeiouAEIOU'
vowel_chars = ''
consonant_chars = ''
s = input("Enter line: ")
for char in s:
    if char.isalpha():
        if char in vowel:
            vowel_chars += char
        else:
            consonant_chars += char
print("Vowels: ", vowel_chars)
print("Number of vowels: ", len(vowel_chars))
print("Consonant: ", consonant_chars)
