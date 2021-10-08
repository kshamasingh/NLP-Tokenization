#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:31:16 2021

@author: kshama.singh
"""


import nltk


paragraph = open("../Tokenization/Tokenization.txt", 'r').read()
#print(paragraph)

# Preparing the sentences
def processData_SentencesTokenize(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    return sentences


# Preparing the words
def processData_WordTokenize(paragraph):
    words = nltk.word_tokenize(paragraph)
    return words


sentences = processData_SentencesTokenize(paragraph);

word = processData_WordTokenize(paragraph);
