import matplotlib.pylab as plt

#string LETTERS is declared here to convert letters into numerical values
#LETTERS[0] is a blank space

LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# here we count the frquency of each letter
def frequency_analysis(text):

    #the text is case insensitive
    text = text.upper
    #we will be using a dictionary to store letter frequencies
    letter_frequencies= {}
    #initialize the dictionary
    for letter in LETTERS:
    		letter_frequencies[letter] = 0
    #let's consider the text we want to analyse	
    for letter in cipher_text:
		#we keep incrementing the occurence of the given letter
        if letter in LETTERS:
            letter_frequencies[letter] += 1
			
    return letter_frequencies

#histogram of letter_frquencies
def plot_distribution(frequencies):
    centers = range(len(LETTERS))
    plt.bar(centers, frequencies.values(), align='center', tick_label=frequencies.keys())
    plt.xlim([0,len(LETTERS)-1])
    plt.show()
def caesar_crack(cipher_text):
    frequency= frequency_analysis(cipher_text)
    print(frequency)
    plot_distribution(frequency)

if __name__ == "__main__":
 cipher_text="YMNXENXEFEXJHWJYERJXXFLJEYMFYERZXYEGJE JWCEXFKJ"
 caesar_crack(cipher_text)
            