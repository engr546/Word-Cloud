# Psuedo Code: Add every word of the file to a string, then add all interesting words
# to a list, lastly count how many times the word repeats using a dictionary and add to cloud.

import wordcloud
import numpy as np
from matplotlib import pyplot as plt


# Get the File
fname = input("Enter File Name: ")

try:
	fread = open(fname)
	file = fread.read()
except Exception as e:
	print(e)


def image_name(name):
	dot = name.find('.')
	img_name = name[:dot]
	return "%s.jpg" % (img_name)


def get_interesting_words(file):
	# Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # To store the strings
    file_contents = ""

    # Enumerate the file
    for index, char in enumerate(file):
    	# Check for word
        if char.isalpha() == True or char.isspace():
			# Concatenate every word 
            file_contents += char

    # Split every word
    spit_contents = file_contents.split()

    # loop every word in the list. Check lower case words. Add the interesting words to list
    interesting_words = [item for item in spit_contents if item.lower() not in uninteresting_words and item.isalpha() == True]

    return interesting_words


def calculate_frequencies(words):
    # Dictionary to store to word counts
    frequencies = {}

    # loop words in the list
    for word in words:
    	# if word is not in the list. Add 1 value
        if word.lower() not in frequencies:
            frequencies[word.lower()] = 1
        # Add count for every word repeatition
        else:
            frequencies[word.lower()] += 1

    return frequencies


def generate_word_cloud(frequencies):
	# Instantiate word cloud
    cloud = wordcloud.WordCloud()
    # Generate the word cloud
    cloud.generate_from_frequencies(frequencies)
    # Create the word cloud image image
    cloud.to_file(image_name(fname))
    # Return the word cloud
    return cloud.to_array()


words = get_interesting_words(file)

file_frequencies = calculate_frequencies(words)

myimage = generate_word_cloud(file_frequencies)

plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()