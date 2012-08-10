import sixLetterFilter as s
import random
wordList = s.sixLetter()
def randomize():
    word = random.choice(wordList)
    print word
    l = list(word)
    random.shuffle(l)
    result = ''.join(l)
    return (result.lower(),word)

def trainer():
    words = randomize()
    word = words[0]
    correct = words[1]
    guess = raw_input('what do you think the word is? \n')
    while(True):
        if guess == correct:
            print 'Great Job!'
            trainer()
        else:
            print 'Try again '+correct
            guess = raw_input('what do you think the word is? \n')
trainer()
    
