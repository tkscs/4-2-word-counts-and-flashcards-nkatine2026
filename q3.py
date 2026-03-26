# Update this dictionary with questions and answers:
flashcards = {
    "question": "answer"
}

# Get a list of keys (questions) from the dictionary
#### YOUR CODE HERE
flashcards["6*7"] = "42"
flashcards["9+10"] = "21"
flashcards["Solve Unified Field Theory!!!"] = "I know the answer but that sounds like a you problem"
flashcards["Is Project Hail Mary Scientifically Accurate?"] = "Is the Earth flat?"
# Randomly sample one question
#### YOUR CODE HERE
b = input("ask a question")
if b == "6*7":
    print(flashcards["6*7"])
elif b == "9+10":
    print(flashcards["9+10"])
elif b == "Solve Unified Field Theory!!!":
    print(flashcards["Solve Unified Field Theory!!!"])
elif "Is Project Hail Mary Scientifically Accurate?":
    print(flashcards["Is Project Hail Mary Scientifically Accurate?"])
else:
    print("screw you")
# Use the `input` function to ask the user the question and get their response
#### YOUR CODE HERE

# Use the question as a key to look up the answer in the dicitonary
#### YOUR CODE HERE

# Check if the response is the same as the answer, and give the user
# feedback based on whether their response was correct or incorrect
#### YOUR CODE HERE