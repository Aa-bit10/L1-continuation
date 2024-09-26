fruit_colors = {
    "apple": "red",
    "pear": "green",
    "grapes": "purple",


}
#accessing keys
print(fruit_colors)
print(fruit_colors["apple"])
#Get all keys: Use the keys() method
print(fruit_colors.keys())
#Get all values: Use the values() method.
print(fruit_colors.values())
#Get all key-value pairs: Use the items() method
print(fruit_colors.items())
#Checking if a Key Exists
if "apple" in fruit_colors:
    print("apple is in the dictonary")
#Changing a Value
fruit_colors["apple"] = "sweet"
print(fruit_colors)
for item in fruit_colors:
    print(item)