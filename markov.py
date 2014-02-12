#!/usr/bin/env python

from sys import argv
from random import choice



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # split the string so we have a list of words
    
    input_words = corpus.split()


    markov_dict = {}

    # iterate through list and create markov dictionary
    #  for each tuple -- current word and next word 
    #  if that tuple exists in the dictionary, append the value with a new word
    lw = len(input_words)
    for i in range (lw-2):
        if not markov_dict.get((input_words[i],input_words[i+1]),False):
            markov_dict[(input_words[i],input_words[i+1])] = [input_words[i+2]]
        else:
            markov_dict[(input_words[i],input_words[i+1])].append(input_words[i+2])
   
    # for key,value in markov_dict.iteritems():
    #     print key,value

# We ommited the very last bigram in the text.  We need to add it manually, and assign a value

    markov_dict[(input_words[lw-2],input_words[lw-1])] = [input_words[0]]
    markov_dict[(input_words[lw-1],input_words[0])] = [input_words[1]]

    print markov_dict

    return markov_dict


def make_text(chains,n):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # find a bigram to start off
    #TODO is there a better way to do this than popping then reinserting

    print chains
    
#TODO  this is inelegant.  We should iterate through until we find a tuple in which 
# first word is capitalized and use that as a start

    ngram,value = chains.popitem()
    chains[ngram] = value
    # print ngram[0]
    # print ngram[]
    wordlist = []
    #we'll convert back to a string later


#we need to split the tuple in the key, create a new key with the second from the old
    

    # go through n ngrams
    # start with the initial ingram
    # append the output string with that ngram, and random value
    # set new key to second of the earlier key and the value from above
    # for nmgram, value in chains.iteritems():
    #     print key, value, choice(value)

    for i in range(int(n)):
         choiceword = choice(value)
         if i == 0:
            wordlist.append(ngram[0])
            wordlist.append(ngram[1])
         
         wordlist.append(choiceword)
         print i
         print wordlist

         new_key = (ngram[1],choiceword)
         ngram = new_key
         value = chains[ngram]  
    
        
# To get sentences, we need to capitalize the word after a sentence ender 

    return " ".join(wordlist)

def main():
    filename = argv[1]
# Do we want to change case, remove punctuation?
# How many ngrams do we want?
    n = argv[2]

#open filename
#TODO clean up argument handling
    f = open(filename, "r")
    input_text = f.read()
    f.close()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict,n)
    print random_text

if __name__ == "__main__":
    main()
