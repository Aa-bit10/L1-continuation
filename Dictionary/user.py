user_names_passwords = {
    "user1": "abc",
    "user2": "abd",
    "user3": "abe",
    "user4": "abf",
    "user5": "abg",
    "user6": "abh",
    "user7": "abi",
    "user8": "abj",
    "user9": "abk",
    "user10": "abl",
}
username = input("enter a username")
password = input("enter a password")
if username not in user_names_passwords:
    print("username not found")
else:
    if user_names_passwords[username] == password:
        print("you are logged in")
    else:
        print("you are not logged in")
        