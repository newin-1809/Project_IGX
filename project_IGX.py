# 1. generate random password
# 2. check password strength
# 3. count characters in password
# 4. calculate strength score using math
# 5. save result in a file using os

import random
import math
import os

# characters manually defined
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
specials = "!@#$%^&*()_+"
all_chars = letters + digits + specials

# generate password
password = ""
for i in range(12):
    password += random.choice(all_chars)

# count characters
char_count = {}
for ch in password:
    char_count[ch] = char_count.get(ch, 0) + 1

# check strength
upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upper = True
    elif ch in "abcdefghijklmnopqrstuvwxyz":
        lower = True
    elif ch in digits:
        digit = True
    elif ch in specials:
        special = True

strength = upper + lower + digit + special

# strength score using math
score = round(math.log(len(password)) * strength, 2)

# save result using os
os.makedirs("output", exist_ok=True)
f = open("output/password.txt", "w")
f.write("Password: " + password + "\n")
f.write("Character Count: " + str(char_count) + "\n")
f.write("Strength Score: " + str(score))
f.close()

print("Password saved in output/password.txt")
