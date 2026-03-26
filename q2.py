"""
INSTRUCTIONS:
The code below has a lot of repetition. Use a dictionary and a for loop to 
make the code more compact.
"""
essay = "A bunch of yap"
def pad_word_count(essay):
    dict = {}
    meh = essay.split()
    for word in meh:
        m = 0
        m = m+1
        m = dict(word) 
    return m 
    # Initialize new essay to match the original.
    # We will update it and re-assign this variable later.
    new_essay = essay

    #### START REPLACING CODE HERE
    new_essay = new_essay.replace("n't", " not")
    new_essay = new_essay.replace("'s'", " is")
    new_essay = new_essay.replace("'re'", " are")
    new_essay = new_essay.replace("'ve'", " have")
    #### STOP REPLACING CODE HERE

    return new_essay

# Here's the function call.
# Don't change this.
