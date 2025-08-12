import os
import string
import collections
from collections import defaultdict

def check_password_strength(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters."

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)

    if not (has_upper and has_lower and has_digit and has_special):
        return False, "Password must contain uppercase, lowercase, digit, and special character (!@#$%^&*)."

    return True, "Strong password."

def validate_passwords_from_file(input_file, output_file, log_file="password_validation.log"):
    try:
        if not os.path.exists(input_file):
            with open(input_file, 'w', encoding='utf-8') as f:
                f.write("Password123!\n")
                f.write("weakpass\n")
                f.write("NoDigitsHere!\n")
                f.write("password123\n")
                f.write("MYPASS123!\n")
                f.write("P@ssword123\n")
                f.write("P@ss1")
            print(f"Created a dummy password file for Password Strength Checker: {input_file}")

        with open(output_file, 'w', encoding='utf-8') as outfile, \
             open(log_file, 'w', encoding='utf-8') as logfile:
            print(f"Starting password validation. Logging results to '{log_file}'.")
            logfile.write("Password Validation Log\n")
            logfile.write("-----------------------\n")

            with open(input_file, 'r', encoding='utf-8') as infile:
                for line in infile:
                    password = line.strip()
                    if not password:
                        continue

                    is_strong, message = check_password_strength(password)
                    if is_strong:
                        outfile.write(password + '\n')
                        logfile.write(f"'{password}': {message} (Strong)\n")
                    else:
                        logfile.write(f"'{password}': {message} (Weak)\n")
        print(f"Strong passwords written to '{output_file}'.")
        print(f"Validation log written to '{log_file}'.")

    except FileNotFoundError:
        print(f"Error (Password Strength Checker): The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error (Password Strength Checker) reading or writing files: {e}")
    except Exception as e:
        print(f"An unexpected error occurred (Password Strength Checker): {e}")


if __name__ == "__main__":
    print("--- Running Exercise 1: Palindrome Checker ---")
    ("input_words.txt", "palindromes.txt") #check_and_write_palindromes
    try:
        with open("palindromes.txt", 'r', encoding='utf-8') as f:
            print("\nContent of palindromes.txt:")
            print(f.read())
    except FileNotFoundError:
        print("Palindromes.txt was not created or found.")
    print("\n" + "="*70 + "\n")

    print("--- Running Exercise 2: Temperature Converter ---")
    ("celsius.txt", "fahrenheit.txt") #convert_temperatures
    try:
        with open("fahrenheit.txt", 'r', encoding='utf-8') as f:
            print("\nContent of fahrenheit.txt:")
            print(f.read())
    except FileNotFoundError:
        print("Fahrenheit.txt was not created or found.")
    print("\n" + "="*70 + "\n")

class InvalidLengthError(Exception):
    pass

class InvalidCharacterError(Exception):
    pass

def register_user(username, output_file):
    try:
        if not (5 <= len(username) <= 15):
            raise InvalidLengthError("Username must be between 5 and 15 characters long.")

        if not username.isalnum():
            raise InvalidCharacterError("Username must contain only alphanumeric characters.")

        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(username + '\n')
        print(f"User '{username}' registered successfully.")
        return True
    except (InvalidLengthError, InvalidCharacterError) as e:
        print(f"Registration failed for '{username}': {e}")
        return False
    except IOError as e:
        print(f"Error (User Registration) writing to file '{output_file}': {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred (User Registration): {e}")
        return False
    finally:
        print(f"Attempt to register '{username}' completed.")

def register_user(username, output_file):
    try:
        if not (5 <= len(username) <= 15):
            raise InvalidLengthError("Username must be between 5 and 15 characters long.")

        if not username.isalnum():
            raise InvalidCharacterError("Username must contain only alphanumeric characters.")

        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(username + '\n')
        print(f"User '{username}' registered successfully.")
        return True
    except (InvalidLengthError, InvalidCharacterError) as e:
        print(f"Registration failed for '{username}': {e}")
        return False
    except IOError as e:
        print(f"Error (User Registration) writing to file '{output_file}': {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred (User Registration): {e}")
        return False
    finally:
        print(f"Attempt to register '{username}' completed.")
    print("--- Running Exercise 3: User Registration ---")
    users_file = "users.txt"
    if os.path.exists(users_file):
        os.remove(users_file)
    register_user("validuser", users_file)
    register_user("short", users_file)
    register_user("verylongusername12345", users_file)
    register_user("user-name", users_file)
    register_user("anotheruser1", users_file)
    try:
        with open(users_file, 'r', encoding='utf-8') as f:
            print("\nContent of users.txt:")
            print(f.read())
    except FileNotFoundError:
        print("Users.txt was not created or found.")
    print("\n" + "="*70 + "\n")

    print("--- Running Exercise 4: Log File Analyzer ---")
    analyze_log_file("server.log", "report.txt")
    try:
        with open("report.txt", 'r', encoding='utf-8') as f:
            print("\nContent of report.txt:")
            print(f.read())
    except FileNotFoundError:
        print("Report.txt was not created or found.")
    print("\n" + "="*70 + "\n")

    print("--- Running Exercise 5: Password Strength Checker ---")
    validate_passwords_from_file("passwords.txt", "strong_passwords.txt")
    try:
        with open("strong_passwords.txt", 'r', encoding='utf-8') as f:
            print("\nContent of strong_passwords.txt:")
            print(f.read())
    except FileNotFoundError:
        print("Strong_passwords.txt was not created or found.")
    try:
        with open("password_validation.log", 'r', encoding='utf-8') as f:
            print("\nContent of password_validation.log:")
            print(f.read())
    except FileNotFoundError:
        print("Password_validation.log was not created or found.")
    print("\n" + "="*70 + "\n")