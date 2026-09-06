def welcomeUser():
    print("Welcome to the text analysis tool, I will mine and analyze a body of text from a file you give me")


# Get Username
def getUsername():
    # Print message prompting user to input their name
    usernameFromInput = input("\nTo begin, please enter your username:\n")
    return usernameFromInput

def greetUser(name):
    # Greet the user
    print("Hello, " + name)


welcomeUser()
username = getUsername()
greetUser(username)