#!/usr/bin/env python

from sys import argv
from random import choice



def make_chains(corpus,ntv):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    # split the string so we have a list of words
    
    input_words = corpus.split()

    markov_dict = {}

    # iterate through list and create markov dictionary
    #  for each tuple -- current word and next word 
    #  if that tuple exists in the dictionary, append the value with a new word

    # lw = len(input_words)
    # for i in range (lw-ntv):
    #     if not markov_dict.get((input_words[i],input_words[i+1]),False):
    #         markov_dict[(input_words[i],input_words[i+1])] = [input_words[i+2]]
    #     else:
    #         markov_dict[(input_words[i],input_words[i+1])].append(input_words[i+2])


    lw = len(input_words)
    for i in range (lw - ntv):
        
        current_tuple = ()
        for j in range(ntv):
            current_tuple += (input_words[i+j],)
            print i,j, current_tuple

        if not markov_dict.get(current_tuple,False):
            markov_dict[current_tuple] = [input_words[i+ntv]]
        else:
            markov_dict[current_tuple].append(input_words[i+ntv])


    # We ommited the very last bigram in the text.  We need to add it manually, and assign a value

    # markov_dict[(input_words[lw-2],input_words[lw-1])] = [input_words[0]]
    # markov_dict[(input_words[lw-1],input_words[0])] = [input_words[1]]

#   print markov_dict

    return markov_dict


def make_text(chains,n,ntv):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # find a bigram to start off
    #TODO keep trying until we get a tuple with the first value capitalized
    
    ngram = choice(chains.keys())
    value = chains.get(ngram)


#using a wordlist since we need to append; will convert back to a string later.
    wordlist = []

#we need to split the tuple in the key, create a new key with the second from the old
        # go through n ngrams
    # start with the initial ingram
    # append the output string with that ngram, and random value
    # set new key to second of the earlier key and the value from above
    # for nmgram, value in chains.iteritems():

    for i in range(int(n)):
        choiceword = choice(value)
        if i == 0:
            # wordlist.append(ngram[0])
            # wordlist.append(ngram[1])
            for j in range(ntv):
                wordlist.append(ngram[j]) 
            #     wordlist.append(choiceword)
            #      # print i
                 # print wordlist

        wordlist.append(choiceword)


       #  # create new key of an arbitrary ngram length
       #  for k in range(ntv-2):
       #      new_key_tupple[k] = ngram[k+1]

       #  new_key_tupple[ntv-1] = choiceword
        # print "ngram, value"
        # print ngram,value
        temp_tuple = ()
        for k in range(ntv-1):
            temp_tuple += (ngram[k+1],)
           # print temp_tuple

        # new_key = (ngram[1],choiceword)
        new_key = (temp_tuple + (choiceword,))
       # print new_key

        ngram = new_key
        value = chains.get(ngram,None)
        
        if value == None:

            ngram = choice(chains.keys())
            value = chains.get(ngram)

                    #break; 


    return " ".join(wordlist)

def main():
    filename = argv[1]

# Max # of ngrams over which to loop if we don't hit end-of-file
    n = argv[2]

    ntv = int(argv[3])

#TODO clean up argument handling, pick a nice default for n, check for file existence, etc.

    f = open(filename, "r")
    input_text = f.read()
    f.close()

    chain_dict = make_chains(input_text,ntv)
    random_text = make_text(chain_dict,n,ntv)
    print random_text

if __name__ == "__main__":
    main()
