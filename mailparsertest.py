from mailparser import MailParser
from nltk.stem.porter import *
from nltk.corpus import stopwords
from os import listdir

def removePunc(mail_body):
	from string import punctuation
	new_body = ""
	punc = set(punctuation)

	for i in range(len(mail_body)):
		if(mail_body[i] in punc):
			continue
		else:
			new_body += mail_body[i]
	return new_body	
def stemWords(mail_body):
	
	words = []
	stemed_words = []
	for line in mail_body.split('\n'):
		for word in line.split():
			words.append(word)	
	stemmer = PorterStemmer()
	for word in words:
		stemed_words.append(stemmer.stem(word))
	return stemed_words

def removeStopWords(words):
	new_words =[]
	stopwrds = stopwords.words('english')
	for word in words:
		if word.lower() not in stopwrds:
			new_words.append(word.lower())
	return new_words

def countWords(body):
	count =0
	for line in body.split('\n'):
		for word in line.split():
			count+=1
	return count
testpath = './beck-s/2001_plan/'
testfile = testpath + listdir(testpath)[1]
parser = MailParser()
parser.parse_from_file(testfile)

mail_subject = str(parser.subject)
mail_from = str(parser.from_)
mail_body = str(parser.body)
print(mail_body)


init_count = countWords(mail_body)

mail_body = removePunc(mail_body)
print("\n\n-----Removed Punc -----\n",mail_body)

mail_body_words = stemWords(mail_body)
print("\n\n-----Stemmed-----\n",mail_body_words)

mail_body_words = removeStopWords(mail_body_words)
print("\n\n-----Removed Stop Words-----\n",mail_body_words)

final_count = len(mail_body_words)
print("\nPre-Processing Done.. Reduced words count from:",init_count,"to: ",final_count)
of = open('./output','w')
of.write(str(parser.from_) )
of.write('\n\n\n')
for word in mail_body_words:
	of.write(str(word)+" " )
#of.write(str(mail_body))
of.close()
