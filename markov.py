#!/usr/bin/env python

from sys import argv
#  open a file
# create make_chains
# create make_text


def make_chains(corpus,sanitize):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    # split and sanitize (maybe) the string so we have a list of words
    
    input_words = corpus.split()
    
    if sanitize:
        print "We are in the sanitize clause"
        # for word in input_words:
        #     word = input_words.lower()
        #     word = input_words.strip("!@#$%^&*()_+=-~`,./;\'\[\]\{\}\":?><" )
# fix the above with a range over the length

    # create blank dictionary
   # print input_words

    markov_dict = {}
    for i in range (len(input_words)-2):
        if not markov_dict.get((input_words[i],input_words[i+1]),False):
          #  print (input_words[i],input_words[i+1]),input_words[i+2]
            markov_dict[(input_words[i],input_words[i+1])] = input_words[i+2]

    print "now the dictionary"
    print markov_dict



    # iterate through list and create markov list
    #  for each tuple -- current work and next work 
    #  if that tuple exists in the dictionary, append the value with the foll
    return {}

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    filename = argv[1]
    sanitize = argv[2]
#open filename
    f = open(filename, "r")
    input_text = f.read()

#Read file and put it in a 
    # Change this to read input_text from a file
    #print type(input_text)
    #print input_text

    chain_dict = make_chains(input_text,sanitize)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
