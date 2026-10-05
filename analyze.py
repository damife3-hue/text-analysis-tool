from random_username.generate import generate_username
from nltk.tokenize import sent_tokenize, word_tokenize
import re

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

# Get text from file
def getArticleText():
    f = open("files/article.txt", "r")
    rawText = f.read()
    f.close()
    return rawText.replace("\n", " ").replace("\r", "")

# Extract Sentences from raw Text Body
def tokenizeSentences(rawText):
    return sent_tokenize(rawText)

# Extract Words from list of Sentences
def tokenizeWords(sentences):
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))
    return words

# Get the key sentences based on search pattern of key words
def extractKeySentences(sentences, searchPattern):
    matchedSentences = []
    for sentence in sentences:
        # if sentence matches desired pattern, add to matchedSentences
        if re.search(searchPattern, sentence.lower()):
            matchedSentences.append(sentence)
    return matchedSentences

# Get the average number of words per sentence, excluding punctuation
def getwordsPerSentence(sentences):
    totalWords = 0
    for sentence in sentences:
        totalWords += len(sentence.split(" "))
    return totalWords / len(sentences)

# Filter raw tokenized words list to only include
# valid english words
def cleanseWordList(words):
    cleansedWords = []
    invalidWordPattern = "[^a-zA-Z-+]"
    for word in words:
        cleansedWord = word.replace(".","").lower()
        if (not re.search(invalidWordPattern, word)) and len(word) > 1:
            cleansedWords.append(cleansedWord)
    return cleansedWords

# Get User Details
welcomeUser()
username = getUsername()
greetUser(username)

# Extract and Tokenize Text
articleTextRaw = getArticleText()
articleSentences = tokenizeSentences(articleTextRaw)
articleWords = tokenizeWords(articleSentences)

# Get Sentence Analytics
stockSearchPattern = "[0-9]|[$€£]|million|billion|trillion|profit|loss"
keySentences = extractKeySentences(articleSentences, stockSearchPattern)
wordsPerSentence = getwordsPerSentence(articleSentences)

# Get Word Analytics
articleWordsCleansed = cleanseWordList(articleWords)

# Print for testing
print("GOT:")
print(articleWordsCleansed)