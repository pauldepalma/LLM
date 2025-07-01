import re
import urllib.request

def read_data():
   url = ("https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt")

   file_path = "the-verdict.txt"
   urllib.request.urlretrieve(url, file_path)

   with open(file_path, "r", encoding="utf=8") as f:
      raw_text = f.read()
   return raw_text
    

def tokenize(raw_text):
   #Split when there is punctuation, white space, and other indicators, but return the match (of punctuation and white space)
   result = re.split(r'([,.:;?_!()"\']|--|\s)', raw_text)
   #Now remove the additional white space
   #first strip removes whitespace for each string in the list; 
   #This could result in "   " becoming ""; ir item.strip() returns "", it is treate s false, so is passed over
   #Result is that all white space is excluded, punctation and indicated special characters are retained
   preprocessed = [item.strip() for item in result if item.strip()] #first strip removes whitespace for each string in list; 
   return preprocessed
	
def create_vocab(preprocessed):
   all_words = sorted(set(preprocessed))  #use a set to retain only unique tokens
   vocab = {token:integer for integer,token in enumerate(all_words)} #dictionary of integers and vocab words
   return vocab


def display_vocab(vocab):
   for i, item in enumerate(vocab.items()):
      print(item)
      if i >= 50:
         break
    
class SimpleTokenizerV1:
   def __init__(self,vocab):
      self.str_to_int = vocab
      self.int_to_str = {i:s for s, i in vocab.items()}

   def encode(self,text):
      preprocessed = re.split(r'([,.:;?_!()"\']|--|\s)', text)
      ids = [item.strip() for item in result if item.strip()]
      return ids
      
   def decode(self, ids):
      text = " ".join([self.int_to_str[i] for i in ids])
      text = re.sub(r'\s+([,.?!"()\'])', r'\1',text)
      return text