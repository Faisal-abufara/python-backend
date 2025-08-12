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