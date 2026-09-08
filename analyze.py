from random_username.generate import generate_username

def welcomeUser():
    print("Welcome to the text analysis tool, I will mine and analyze a body of text from a file you give me")


# Get Username
def getUsername():
    # Print message prompting user to input their name
    usernameFromInput = input("\nTo begin, please enter your username:\n")

    if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
        print("\nYour username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9) and underscores, have no spaces, and cannot start with a number\n")
        print("Assigning username instead...")
        usernameFromInput = generate_username()[0]

    return usernameFromInput

def greetUser(name):
    # Greet the user
    print("Hello, " + name)


welcomeUser()
username = getUsername()
greetUser(username)