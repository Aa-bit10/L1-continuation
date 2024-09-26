vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,

}
sentence = input("enter a sentence")
for item in sentence:
    if item in vowels:
        vowels[item] += 1      
print(vowels)

