#James Harris
#2078031

def stronger_password(password):
    replace = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}
    strong_password = ""

    for char in password:
        if char in replace:
            strong_password = strong_password + replace[char]
        else:
            strong_password = strong_password + char


    strong_password = strong_password + "q*s"
    return strong_password



simple_password = input()
new_password = stronger_password(simple_password)

print(new_password)
