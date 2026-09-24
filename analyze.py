from random_username.generate import generate_username

def welcomeUser():
    print("Welcome to the text analysis tool, I will mine and analyze a body of text from a file you give me")


# Get Username
def getUsername():

    maxAttempts = 3
    attempts = 0

    while attempts < maxAttempts:

        # Print message prompting user to input their name
        inputPrompt = ""
        if attempts == 0:
            inputPrompt = "\nTo begin, please enter your username:\n" #input("\nTo begin, please enter your username:\n")
        else:
            inputPrompt = "\nPlease try again:\n"
        usernameFromInput = input(inputPrompt)
        
        # Validate username
        if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
            print("\nYour username must be at least 5 characters long, alphanumeric only (a-z/A-Z/0-9) and underscores, have no spaces, and cannot start with a number\n")
        else:
            return usernameFromInput
        attempts += 1

    print("\nExhausted all " + str(maxAttempts) + " attempts, Assigning username instead...")
    return generate_username()[0]

     
    

def greetUser(name):
    # Greet the user
    print("Hello, " + name)


welcomeUser()
username = getUsername()
greetUser(username)