# =========================
sample = {('<go>','this'), ('this','is'), ('is','an'), ('an','example'), ('example','.')}

# Functions needed from previous project: Ngram Generator
def clean_text(txt):
    cleaned = ''
    for letter in txt.lower():
        if ord('a') <= ord(letter) <= ord('z') or letter.isspace():
            cleaned += letter
    return cleaned

def find_bigrams(first_word,bigrams):
    bag = []
    for bigram in bigrams:
        word1,word2 = bigram
        if word1 == first_word:
            bag.append( word2 )
    return bag

#1) =========================
# store some text from the user & clean it from any non-alphabetic characters
def user_talk():
    txt = input('user: ')
    return clean_text(txt)

#results1 = user_talk()
#print(results1)

#2) =========================
# convert a string of words into a list of tuples of words (called bigrams)
#the string of words should start with a special token like "<go>" and end with a special token like "."
def txt_to_bigrams(txt):
    bigrams = set()
    txt = ['<go>'] + txt.split() + ['.']
    for bigram in zip(txt, txt[1:]):
        bigrams.add(bigram)
    return bigrams

# results2 = txt_to_bigrams('this is an example')
# print(results2)
# print(sample)

#3) =========================
# generate sentences using bigrams 
# use the special token <go> to start generating
# and the special token '.' to know when to stop the loop

def generate_sentence(ngrams):
    generated = ''
    from random import choice, shuffle
    word = '<go>'
    while word != '.':
        words = find_bigrams(word,ngrams)
        shuffle(words)
        word = choice(words)
        generated += ' ' + word
    return generated

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
    sentence = 'hello'
    while sentence != 'bye':
        sentence = user_talk()
        ngrams= txt_to_bigrams(sentence)
        remembered_ngrams |= ngrams
        reply = generate_sentence(remembered_ngrams)
        print('bot: ' + reply)
    print('bot: goodbye')
    return remembered_ngrams

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
    with open('bigrams.txt','w') as f:
        for w1,w2 in bigrams:
            f.write(w1)
            f.write(',')
            f.write(w2)
            f.write('\n')

#save_bigrams(sample)

#6) =========================
# load the bigrams stored on a file as a sequence of tuples
def load_bigrams(filename = 'bigrams.txt'):
    bigrams = set()
    with open(filename) as f:
        for bigram in f.readlines():
            w1,w2 = bigram.strip().split(',')
            bigram = (w1,w2)
            bigrams.add(bigram)
    return bigrams

#results6 = load_bigrams()
#print(results6)
#print(sample)

#========================= HAVE FUN TEACHING YOUR BOT TO SPEAK =========================
def chatbot():
    a = load_bigrams()
    b = chat(a)
    save_bigrams(b)
#chatbot()