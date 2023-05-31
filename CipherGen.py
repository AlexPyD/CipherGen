import random
import string

def generate_password(length, allowed_chars):
    password = ''
    for _ in range(length):
        password += random.choice(allowed_chars)
    return password

def main():
    length = int(input("Enter the length of the password: "))
    allowed_characters = input("Enter the allowed characters (leave blank to use all characters): ")
    
    if allowed_characters == '':
        allowed_characters = string.ascii_letters + string.digits + string.punctuation
    else:
        allowed_characters = "".join(set(allowed_characters))
    
    generated_password = generate_password(length, allowed_characters)
    print("Generated password:", generated_password)

    input("Press Enter to exit.")

if __name__ == '__main__':
    main()
