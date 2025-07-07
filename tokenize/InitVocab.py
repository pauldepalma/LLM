import re
import urllib.request
#import SimpleTokenizerV1 as ST
import SimpleTokenizerV2 as ST

def download_data(file_name):
	url = 	("https://raw.githubusercontent.com/rasbt/"
			"LLMs-from-scratch/main/ch02/01_main-chapter-code/"
			"the-verdict.txt")
	urllib.request.urlretrieve(url, file_name)  

def read_data(file_name):
	with open(file_name, "r", encoding="utf=8") as f:
		raw_text = f.read()
	return raw_text

def preprocess(raw_text):
	#split on punctuation and spaces. parens says "keep delimiters"
	#result is a list of words, punctuation, and spaces
	result = re.split(r'([,.:;?_!()"\']|--|\s)', raw_text)

	#remove white space
	preprocessed = [item.strip() for item in result if item.strip()] 
	return preprocessed
	
def create_vocab(preprocessed):
	#use a set to retain only unique tokens
	all_tokens = sorted(list(set(preprocessed)))  
	
	#add special tokens
	all_tokens.extend(["<|endoftext|>", "<|unk|>"])
	
	#dictionary of integers and vocab words
	vocab = {token:integer for integer,token in enumerate(all_tokens)} 
	return vocab
	
def display_vocab_f_to_b(vocab,size):
	for i, item in enumerate(vocab.items()):
		print(item)
		if i >= size:
			break
			
def display_vocab_b_to_f(vocab,size):
	for i, item in enumerate(list(vocab.items())[-size:]):
		print(item)
			
def display_length(vocab):
	print(len(vocab))
			
def main():
	#Create an initial vocabulary 
	file_name = "the-verdict.txt"
	download_data(file_name)
	raw_text = read_data(file_name)
	preprocessed = preprocess(raw_text)
	vocab = create_vocab(preprocessed)
	#display_length(vocab)
	#display_vocab_f_to_b(vocab,5)
	#display_vocab_b_to_f(vocab,5)
	
	tokenizer = ST.SimpleTokenizerV2(vocab)
	
	'''
	#Tokenize text and map to IDs from  existing vocabulary
	#Tokenizer = ST.SimpleTokenizerV1(vocab)
	#triple quotes necessary to preserve line breaks, indentation, and single/double quotes
	text =  """"It's the last he painted, you know,"
			Mrs. Gisburn said with pardonable pride."""
	ids = tokenizer.encode(text)
	print(ids)
	tokens = tokenizer.decode(ids)
	print(tokens)
	'''
	
	'''
	Listing 2.4 illustrating handling of unknown words
	'''
	text1 = "Hello,do you like tea?"  
	text2 = "In the sunlit terraces of the palace."
	text = " <|endoftext|> ".join((text1, text2))
	#print(text)
	tokenizer = ST.SimpleTokenizerV2(vocab)
	ids = tokenizer.encode(text)
	print(ids)
	tokens = tokenizer.decode(ids)
	print(tokens)
	
	
	
	
	
	
	
	
	
    
main()