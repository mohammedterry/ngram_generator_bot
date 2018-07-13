# =========================
sample = {('<go>','this'), ('this','is'), ('is','an'), ('an','example'), ('example','.')}

# Functions needed from previous project: Ngram Generator
#from student_name import clean_text, find_bigrams

#1) =========================
# store some text from the user & clean it from any non-alphabetic characters
def user_talk():
    pass
#results1 = user_talk()
#print(results1)

#2) =========================
# convert a string of words into a list of tuples of words (called bigrams)
#the string of words should start with a special token like "<go>" and end with a special token like "."
def txt_to_bigrams(txt):
    pass
# results2 = txt_to_bigrams('this is an example')
# print(results2)
# print(sample)

#3) =========================
# generate sentences using bigrams 
# use the special token <go> to start generating
# and the special token '.' to know when to stop the loop

def generate_sentence(ngrams):
    pass
# results3 = generate_sentence(sample)
# print(results3)

#4) =========================
# to chat, the bot should:
#   - take in the users sentence
#   - convert it to bigrams
#   - add those bigrams to its working memory
#   - use the bigrams in its memory to generate a sentence that it can print back to the user
#   - the bot should then repeat this process
#   - the bot should stop chatting when it hears the user say a keyword (e.g. "bye")
#   - once finished, return all the bigrams collected in the bots memory
def chat(remembered_ngrams = set()):
    pass
#results4 = chat()
#print(results4)

#5) =========================
# save a list of bigrams to a file called "bigrams.txt"
# each bigram should be on a new line
# each word in the bigram should be separated by a comma
# e.g.
# <go>, hello
# hello, how
# how, are
# etc...
def save_bigrams(bigrams):
    pass
#save_bigrams(sample)

#6) =========================
# load the bigrams stored on a file as a sequence of tuples
def load_bigrams(filename = 'bigrams.txt'):
    pass

#results6 = load_bigrams()
#print(results6)
#print(sample)

#========================= HAVE FUN TEACHING YOUR BOT TO SPEAK =========================
def chatbot():
    a = load_bigrams()
    b = chat(a)
    save_bigrams(b)
#chatbot()