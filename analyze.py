from random_username.generate import generate_username
import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords
from wordcloud import WordCloud
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('vader_lexicon')
wordLemmatizer = WordNetLemmatizer()
stopWords = set(stopwords.words('english'))
sentimentAnalyzer = SentimentIntensityAnalyzer()

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

# Convert part of speech from pos_tag() function
# into wordnet compatible pos tag
posToWordnetTag = {
    "J": wordnet.ADJ,
    "V": wordnet.VERB,
    "N": wordnet.NOUN,
    "R": wordnet.ADV
}

def treebankPosToWordnetPos(partOfSpeech):
    posFirstChar = partOfSpeech[0]
    if posFirstChar in posToWordnetTag:
        return posToWordnetTag[posFirstChar]
    return wordnet.NOUN

# Convert raw list of (word, POS) tuple to a list of strings
# that only include valid english words
def cleanseWordList(posTaggedWordTuples):
    cleansedWords = []
    invalidWordPattern = "[^a-zA-Z-+]"
    for posTaggedWordTuple in posTaggedWordTuples:
        word = posTaggedWordTuple[0]
        pos = posTaggedWordTuple[1]
        cleansedWord = word.replace(".","").lower()
        if (not re.search(invalidWordPattern, word)) and len(word) > 1 and cleansedWord not in stopWords:
            cleansedWords.append(wordLemmatizer.lemmatize(cleansedWord, treebankPosToWordnetPos(pos))) 
    return cleansedWords

# # Get User Details
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
wordsPosTagged = nltk.pos_tag(articleWords)
articleWordsCleansed = cleanseWordList(wordsPosTagged)

# Generate word cloud
separator = " "
# the \ tells python to read the next line as part of the same line of code, so we can break it up for readability
wordcloud = WordCloud(width = 1000, height = 700, \
                      background_color="white", colormap="Set3", \
                        collocations=False).generate(separator.join(articleWordsCleansed))
wordcloud.to_file("results/wordcloud.png")

# Run Sentiment Analysis
sentimentResult = sentimentAnalyzer.polarity_scores(articleTextRaw)

# Print for testing
print(sentimentResult)