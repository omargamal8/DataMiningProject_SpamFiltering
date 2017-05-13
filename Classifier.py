import collections
import os
from string import punctuation

def classify(file):
    h=0
    s=0
    with open(file) as f:
        for line in f:
            for word in line.split():
                h+=ham_rating[word]
                s+=spam_rating[word]
    i= 1+s-h
    if(i<0):
        print ('Ham')
    else:
        print('spam')

ham = collections.Counter()
spam = collections.Counter()
spam_rating = collections.Counter()
ham_rating = collections.Counter()



ham_path = './ham/'
spam_path = './spam/'
punc = set(punctuation)

for file in os.listdir(ham_path):
    with open(ham_path+''+file) as f:
        for line in f:
            for word in line.split():
                ham.update({word.lower()})


for file2 in os.listdir(spam_path):
    with open(spam_path+''+file2) as f2:
        for line2 in f2:
            for word2 in line2.split():
                spam.update({word2.lower()})

for word in spam :
    s = spam[word]/(spam[word]+ham[word])
    spam_rating.update({word:s})
    ham_rating.update({word:1-s})

classify('./spam/0041.2003-12-19.GP.spam.txt')


