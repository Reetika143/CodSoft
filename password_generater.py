import string
import secrets

def password_generator(length, use_uppercase, use_numbers, use_special_char):
   
    char = string.ascii_lowercase
    if use_uppercase:
        char = char + string.ascii_uppercase
    if use_numbers:
        char = char + string.digits
    if use_special_char:
        char = char + string.punctuation

    password = ''.join(secrets.choice(char) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    length = int(input("Enter the length of the password: "))

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_char = input("Include special characters? (y/n): ").lower() == 'y'

    password = password_generator(length, use_uppercase, use_numbers, use_special_char)

    print("\nGenerated Password : ", password)

if __name__ == "_main_":
    main()