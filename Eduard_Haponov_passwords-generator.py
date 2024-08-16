import random
import string
import csv

# Initialize parameters for generating passwords
password_types = [
    {"count": 5000, "password_length": 25, "special_chars": True, "numbers": True},
    {"count": 2500, "password_length": 10, "special_chars": False, "numbers": True},
    {"count": 1000, "password_length": 5, "special_chars": True, "numbers": False}
]

#Generate a random password
def generate_password(password_length, special_chars, numbers):
    characters = string.ascii_letters
    if special_chars:
        characters += string.punctuation
    if numbers:
        characters += string.digits
    return ''.join(random.choice(characters) for i in range(password_length))#Takes 1 random character and combines it into one string of the given password length


# Generate passwords
for index, password_type in enumerate(password_types):
    passwords = []
    for _ in range(password_type["count"]):
        password = generate_password(password_type["password_length"],
                                     password_type["special_chars"],
                                     password_type["numbers"])
        passwords.append(password)
    
    # Write passwords to a CSV file
    with open(f'Eduard_Haponov - passwords_{index+1}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["password"])  # Write header
        for password in passwords:
            writer.writerow([password])  # Write passwords
    print(f"File Eduard_Haponov - passwords_{index+1}.csv succesfully created")
