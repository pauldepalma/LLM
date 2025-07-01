import CreateVocab as cv


def main():

	raw_text = cv.read_data()
	preprocessed = cv.tokenize(raw_text)
	vocab = cv.create_vocab(preprocessed)
	#cv.display_vocab(vocab)
	tokenizer = cv.SimpleTokenizerV1(vocab)
main()