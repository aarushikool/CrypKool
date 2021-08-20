ENGLISH_WORDS = []
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_data():
    dictionary =  open('lanuageDetectionWordlist.txt', 'r')
    #initialize ENGLISH_WORDS with the words from the text file
    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)
    dictionary.close()
def count_words(text):
    text = text.upper()
    #text converted to a list of words:
    words = text.split(' ')
    #matches counts the english words in the text
    matches=0
    #check
    for word in words:
        if word in ENGLISH_WORDS:
            matches+=1
    return matches
def is_text_english(text): 
    matches= count_words(text)
    #if 90% of the words in the text are english words then
	#it is an english text
    if (float(matches) / len(text.split('\n'))) * 100 >= 90:
        return True
    return False
def caesar_crack(cipher_text):
    for key in range(len(ALPHABET)):
        plain_text = ''
        #caesar decryption
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index-key)%len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
			
		#print decrypted string with the given key
        if is_text_english(plain_text):
            print("Caesar cipher cracked!, Key: %s, Message: %s" % (key,plain_text))

if __name__ == "__main__":
    get_data()
    encrypted = 'VJKUBKUBCBOGUUCIG'
    caesar_crack(encrypted)