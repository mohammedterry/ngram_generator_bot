#=============
# lets modify the bot to use trigrams instead

def clean_text(txt):
    cleaned = ''
    for letter in txt.lower():
        if ord('a') <= ord(letter) <= ord('z') or letter.isspace():
            cleaned += letter
    return cleaned

def user_talk():
    txt = input('user: ')
    return clean_text(txt)

def find_trigrams(first_word,second_word,trigrams):
    bag = []
    for trigram in trigrams:
        word1,word2,word3 = trigram
        if word1 == first_word and word2 == second_word:
            bag.append( word3 )
    return bag

def txt_to_trigrams(txt):
    trigrams = set()
    txt = ['<go>','<go>'] + txt.split() + ['.']
    for trigram in zip(txt, txt[1:],txt[2:]):
        trigrams.add(trigram)
    return trigrams

def generate_sentence(ngrams):
    generated = ''
    from random import choice, shuffle
    word1,word2,word3 = '<go>','<go>',''
    while word3 != '.':
        words = find_trigrams(word1,word2,ngrams)
        shuffle(words)
        word3 = choice(words)
        generated += ' ' + word3
        word1 = word2
        word2 = word3
    return generated

def chat(remembered_ngrams = set()):
    sentence = 'hello'
    while sentence != 'bye':
        sentence = user_talk()
        ngrams= txt_to_trigrams(sentence)
        remembered_ngrams |= ngrams
        reply = generate_sentence(remembered_ngrams)
        print('bot: ' + reply)
    print('bot: goodbye')
    return remembered_ngrams

def save_trigrams(trigrams):
    with open('trigrams.txt','w') as f:
        for w1,w2,w3 in trigrams:
            f.write('{},{},{}\n'.format(w1,w2,w3))

def load_trigrams(filename = 'trigrams.txt'):
    trigrams = set()
    with open(filename) as f:
        for trigram in f.readlines():
            w1,w2,w3 = trigram.strip().split(',')
            trigram = (w1,w2,w3)
            trigrams.add(trigram)
    return trigrams

def bootstrap(filename = 'twitter.txt'):
    trigrams = set()
    with open(filename) as f:
        for line in f.readlines():
            trigrams |= txt_to_trigrams(clean_text(line))
    save_trigrams(trigrams)

def chatbot():
    a = load_trigrams()
    b = chat(a)
    save_trigrams(b)

bootstrap()
chatbot()
