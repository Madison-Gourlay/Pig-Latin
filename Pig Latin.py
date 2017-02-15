'''
Pig Latin Program: For Fun

Author: Maddy Gourlay

Credits: Mike Gourlay (catching bugs only)

Idea came from Martyr2's Mega Project Ideas
'''

def remove_punc(word):
    '''
    (str) --> str

    Removes all non-alpha characters from a string. Changes all characters to
    lowercase. Removes any duplicate spaces and any spaces at the beginning or
    end of the string. Returns the new alpha-only, lowercase string.

    >>> remove_punc('Hello, world')
    'hello world'

    >>> remove_punc("Maddy's  code is awesome!")
    'maddys code is awesome'

    >>> remove_punc('My favorite numbers are 1, 2, 3, and 4.')
    'my favorite numbers are and'
    '''

    word = word.lower()
    new_string = ''

    for ch in word:
        if ch.isalpha() or ch == ' ':
            new_string = new_string + ch

    if new_string == '':
        return 'String must be a word or phrase.'

    while new_string[0] == ' ' and len(new_string) > 1:
        new_string = new_string[1:]

    while new_string[-1] == ' ' and len(new_string) > 1:
        new_string = new_string[:-1]

    if new_string == '' or new_string == ' ':
        return 'String must be a word or phrase.'
        
    i = 0
    
    while i < len(new_string) - 1:
        if new_string[i] == ' ' and new_string[i + 1] == ' ':
            new_string = new_string[:i] + new_string[i + 1:]
        else: i += 1

    return new_string
    

def pig_latin(word):
    '''
    (str) --> str

    Translates a string into pig latin. Removes punctuation, capitalization,
    numbers, and excessive spaces.

    >>> pig_latin('Hello, world')
    'Ellohay orldway'

    >>> pig_latin('Maddy is the best')
    'Addymay isway ethay estbay'

    >>> pig_latin('Shakespeare loves pig latin.')
    'Akespeareshay oveslay igpay atinlay'
    '''

    consonants = 'bcdfghjklmnpqrstvwxyz'
    split = 0
    pig_phrase = ''

    if word == 'A' or word == 'a':
        return 'away'

    if word == 'I':
        return 'Iway'

    if len(word) < 2:
        return 'String must be a word or phrase.'

    word = remove_punc(word)

    if word == 'String must be a word or phrase.':
        return 'String must be a word or phrase.'
    
    while split > -1:
        split = word.find(' ')
    
        if split >= 1:
            new_word = word[:split]
            word = word[split + 1:]
        else:
            new_word = word
            
        if new_word[0] in consonants and new_word[1] in consonants and new_word[2] in consonants:
            new_word = new_word[3:] + new_word[0] + new_word[1] + new_word[2] + 'ay'
        elif new_word[0] in consonants and new_word[1] in consonants:
            new_word = new_word[2:] + new_word[0] + new_word[1] + 'ay'
        elif new_word[0] in consonants:
            new_word = new_word[1:] + new_word[0] + 'ay'
        else:
            new_word = new_word + 'way'

        pig_phrase = pig_phrase + new_word + ' '
        pig_phrase = pig_phrase.capitalize()

    return pig_phrase[:-1]          
    
