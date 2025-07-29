import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!\n")

    while True:
        try:
            length = int(input("Enter the desired password length (min 4): "))
            if length < 4:
                print("Password length should be at least 4. Please try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        password = generate_password(length)
        print(f"\nGenerated Password: {password}")

        again = input("\nGenerate another password? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye! Stay secure. 🛡️")
            break

if __name__ == "__main__":
    main()