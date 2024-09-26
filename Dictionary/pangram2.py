numberAsString = input("Enter the number - ")

# Dictionary to count occurrences of each digit
numCount = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0
}

# Counting each digit in the input number
for num in numberAsString:
    if num in numCount:
        numCount[num] += 1

# Check if all digits are present
pangram = True
for count in numCount.values():
    if count == 0:
        pangram = False

# Output result
if pangram:
    print("Entered number is a Pangram")
else:
    print("Entered number is not a Pangram")