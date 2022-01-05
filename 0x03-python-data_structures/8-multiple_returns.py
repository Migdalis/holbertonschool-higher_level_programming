#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_chr = 'None'
    else:
        first_chr = sentence[0]
    return (len(sentence), first_chr)
