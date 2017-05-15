from mailparser import MailParser
from nltk.stem.porter import *
from nltk.corpus import stopwords
from os import listdir
from os import path
from os import remove
from os import makedirs
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


def getAllFiles(top_directory):
	files = []
	for directory in listdir(top_directory):
		if path.isfile( str(top_directory + directory) ):
			files.append( str(top_directory + directory) )
		else:
			files = files + (getAllFiles( str(top_directory + directory+"/") ))
	return files 


source_top_directory = './beck-s/'
files = getAllFiles(source_top_directory)

dest_top_directory = "./output/"
dest_directory = dest_top_directory+source_top_directory[1:]


try:
    makedirs(dest_top_directory)
    print("Output top directory check: Created")
except:
	print("Output top directory check: Exists")
try:
    makedirs(dest_directory)
    print("Output inner directory check: Created")
except :
    print("Output inner directory check: Exists")
from time import sleep

delay_time = 5
print("Parsing will start in",delay_time, "seconds")
sleep(delay_time)


parser = MailParser()
success = 0
fail = 0
i = 0
for file in files:
	print("file to be parsed:") 
	print(file)
	try:
		parser.parse_from_file(file)
		success+=1
		i+=1
	except:
		print("file cannot be parsed")
		output_file_path = "./PreProcessed"+file[1:]
		try:
			remove(output_file_path)
		except:
			print("already removed")	
		fail+=1
		continue

	mail_subject = str(parser.subject)
	mail_from = str(parser.from_)
	mail_body = str(parser.body)
	# print(mail_body)


	init_count = countWords(mail_body)

	mail_body = removePunc(mail_body)
	# print("\n\n-----Removed Punc -----\n",mail_body)

	mail_body_words = stemWords(mail_body)
	# print("\n\n-----Stemmed-----\n",mail_body_words)

	mail_body_words = removeStopWords(mail_body_words)
	# print("\n\n-----Removed Stop Words-----\n",mail_body_words)

	final_count = len(mail_body_words)
	# print("\nPre-Processing Done.. Reduced words count from:",init_count,"to: ",final_count)


	output_file_path = dest_directory+str(i)
	print("Parsing Complete")
	print(file, "parsed to output file: ", output_file_path,"\n\n")		
	# print(output_file_path)
	of = open(output_file_path, 'w')
	# of.write("From: "+ str(parser.from_)+"\n")
	of.write("Subject: "+str(mail_subject)+"\n" )
	for word in mail_body_words:
		of.write( str(word) + " " )
	# of.write(str(mail_body))
	of.close()

print("Parsed: ",success)
print("Failed: ",fail)