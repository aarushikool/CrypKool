from random import randint
import matplotlib.pyplot as plt
#string alphabet is declared here to convert ALPHABET into numerical values
#ALPHABET[0] is a blank space
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encrypt(text, key):
    text= text.upper()
    cipher_text = ''
    for index, char in enumerate(text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]
    return cipher_text
def decrypt(msg, key):
    plain = ''
    for index, char in enumerate(msg):
         key_index = key[index]
         char_index = ALPHABET.find(char)
         plain += ALPHABET[(char_index - key_index) % len(ALPHABET)]
    return plain

def random_sequence(text):
    #we store the random values in a list
	random_sequence = []

	#generating as many random values as the number of characters in the plain_text
	#size of the key = size of the plain_text
	for rand in range(len(plain_text)):
		random_sequence.append(randint(0,len(ALPHABET)))
		
	return random_sequence

def frequency_analysis(plain_text):
    
    #the text is case insensitive
    plain_text = plain_text.upper
    #we will be using a dictionary to store letter frequencies
    letter_frequencies= {}
    #initialize the dictionary
    for letter in ALPHABET:
    		letter_frequencies[letter] = 0
    #let's consider the text we want to analyse	
    for letter in plain_text:
		#we keep incrementing the occurence of the given letter
        if letter in ALPHABET:
            letter_frequencies[letter] += 1
			
    return letter_frequencies

#histogram of letter_frquencies
def plot_distribution(frequencies):
    centers = range(len(ALPHABET))
    plt.bar(centers, frequencies.values(), align='center', tick_label=frequencies.keys())
    plt.xlim([0,len(ALPHABET)-1])
    plt.show()

if __name__ == "__main__":
    plain_text = 'HELLO I AM HERE BRO'
    key= random_sequence(plain_text)
    print("Original message is %s " % plain_text.upper())
    cipher= encrypt(plain_text,key)
    print("Encrypted message is %s " % cipher)
    decrypted_text= decrypt(cipher,key)
    print("Decrypted message is %s " % decrypted_text)
    plot_distribution(frequency_analysis(cipher))

