#!/usr/bin/python
# -*- coding: utf-8 -*-
from nltk import word_tokenize, wordpunct_tokenize
import nltk.data

f = open('test_convert.txt', 'r')
text = f.read()
# s = ("It's a beautiful world we live in.  Why do birds cry? I can't get me no satisfaction. H. G. Wells wrote a sexist famous book.")
# word_tokenize(s)

sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")
with open('sentences.txt', "a") as fo:
	fo.write('\n-----\n'.join(sent_detector.tokenize(text.strip())))

new_f = open('sentences.txt', 'r')
possible_sims = {}
for line in new_f:
	if "like" in line:
		possible_sims[line] = 5

print possible_sims
