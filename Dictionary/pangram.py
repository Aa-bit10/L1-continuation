unumber = input("enter a number")
numbers = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    0: 0,

}
for item in unumber:
    if item in numbers:
        numbers[item] += 1
pangram =  True
for count in numbers.values():
    if count == 0:
        pangram =  False
if pangram: 
    print("numbers are a pangram")
else:
    print("number is not a pangram")


