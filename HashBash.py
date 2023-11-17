import bcrypt

def hash_password(password):
    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

def check_password(input_password, hashed_password):
    # Check that an unhashed password matches one that has previously been hashed
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

# Example usage:
if __name__ == "__main__":
    # Get a password from the user (in a real-world scenario, this would come from a form or some input)
    user_password = input("Enter your password: ")

    # Hash the password
    hashed_password = hash_password(user_password)

    # Simulate a login attempt
    login_attempt = input("Enter your password for login attempt: ")

    # Check if the entered password matches the hashed password
    if check_password(login_attempt, hashed_password):
        print("Login successful!")
    else:
        print("Incorrect password. Access denied.")
