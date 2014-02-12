#!/usr/bin/env python

from sys import argv
from random import choice

# def sanitize(dirtystring)
#     return ' '
    
#     if sanitize:
#         print "We are in the sanitize clause"
#         # for word in input_words:
#         #     word = input_words.lower()
#         #     word = input_words.strip("!@#$%^&*()_+=-~`,./;\'\[\]\{\}\":?><" )
# # fix the above with a range over the length

#     # create blank dictionary   

def make_chains(corpus,sanitize):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # split and sanitize (maybe) the string so we have a list of words
    
    input_words = corpus.split()


    markov_dict = {}

    # iterate through list and create markov dictionary
    #  for each tuple -- current word and next word 
    #  if that tuple exists in the dictionary, append the value with a new word

    for i in range (len(input_words)-2):
        if not markov_dict.get((input_words[i],input_words[i+1]),False):
            markov_dict[(input_words[i],input_words[i+1])] = [input_words[i+2]]
        else:
            markov_dict[(input_words[i],input_words[i+1])].append(input_words[i+2])
  #  print markov_dict
    # for key,value in markov_dict.iteritems():
    #     print key,value


    return markov_dict


def make_text(chains,n):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # find a bigram to start off
    #TODO is there a better way to do this than popping then reinserting

    ngram,value = chains.popitem()
    print ngram[0],ngram[1]
    chains[ngram] = value
    # print ngram[0]
    # print ngram[]
    wordlist = []
    #we'll convert back to a string later

    for i in range(int(n)):
         choiceword = choice(value)
         wordlist.append(ngram[0])
         wordlist.append(ngram[1])
         wordlist.append(choiceword)

         new_key = (ngram[1],choiceword)
         ngram = new_key
         value = chains[ngram]  
    
    print " ".join(wordlist)

         
#we need to split the tuple in the key, create a new key with the second from the old
    

    # go through n ngrams
    # start with the initial ingram
    # append the output string with that ngram, and random value
    # set new key to second of the earlier key and the value from above
    # for nmgram, value in chains.iteritems():
    #     print key, value, choice(value)

    return " ".join(wordlist)

def main():
    filename = argv[1]
# Do we want to change case, remove punctuation?
    sanitize = argv[2]
# How many ngrams do we want?
    n = argv[3]
#open filename
#TODO clean up argument handling
    f = open(filename, "r")
    input_text = f.read()
    f.close()

    chain_dict = make_chains(input_text,sanitize)
    random_text = make_text(chain_dict,n)
    print random_text

if __name__ == "__main__":
    main()
