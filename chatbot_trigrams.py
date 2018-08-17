
class Learn:    
    def text_to_trigrams(self,txt,context = '<go>'):
        trigrams = {('<go>','<go>',txt.split()[0])}
        txt = [context,'<go>'] + txt.split() + ['.']
        for trigram in zip(txt, txt[1:],txt[2:]):
            trigrams.add(trigram)
        return trigrams
    
    def add_to_trigrams(self,ngrams):
        try:
            with open('trigrams.txt') as f:
                while True:
                    line = f.readline()
                    w1,w2,w3 = line.strip().split(',')
                    trigram = (w1,w2,w3)
                    if trigram in ngrams: 
                        ngrams.remove(trigram)
                    if len(ngrams) == 0:
                        return
        except:
            with open('trigrams.txt','a') as f:
                for w1,w2,w3 in ngrams:
                    f.write('{},{},{}\n'.format(w1,w2,w3))

    def find_trigrams(self,first_word,second_word):
        tris = []
        with open('trigrams.txt') as f:
            try:
                while True:
                    line = f.readline()
                    w1,w2,w3 = line.strip().split(',')
                    if w1 == first_word and w2 == second_word:
                        tris.append(w3)
            except:
                pass
        if len(tris) == 0:
            tris.append('.')
        return tris
    
    def generate_sentence(self,word1 = '<go>'):
        from random import choice,shuffle
        generated = ''
        word2,word3 ='<go>',''
        while word3 != '.':
            words = self.find_trigrams(word1,word2)
            shuffle(words)
            word3 = choice(words)
            generated += ' ' + word3
            word1 = word2
            word2 = word3
        return generated

    def learn_and_talk(self,prev_user_sentence,pprev_bot_sentence = ' .'):
        # format textual information
        user_context = clean(prev_user_sentence) + ' .'        
        if len(pprev_bot_sentence.split()) > 1:
            bot_context = pprev_bot_sentence.split()[-2]
        else:
            bot_context = '<go>'            
        # store bigrams to learn
        self.add_to_trigrams(self.text_to_trigrams(user_context, bot_context))
        # reply
        last_word = user_context.split()[-2]
        reply = self.generate_sentence(last_word)
        if reply == ' .':
            reply = '(... lets change topic)<br>' + self.generate_sentence()
        return reply


    def quick_test(self):
        user,bot = 'hello',' .'
        while user != 'bye':
            user = input('user: ')
            bot = self.learn_and_talk(user,bot)
            print('bot:',bot)