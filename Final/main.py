import wordcloud
import numpy as np
from matplotlib import pyplot as plt

def image_name(name):
    """Get the name of the file and returns a string with .jpg format"""
    
    # Gets the '.' position
    dot = name.find('.')
    # Slice the name from beginning and before '.'
    img = name[:dot]
    # return string with jpg format
    return "{}.jpg".format(img)


def calculate_frequencies(file_contents):
    """Checks the contents of the file and calulcate
     the occurences of words and returns a dictionary """

    # list of uninteresting words
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # Dictionary to store frequencies
    frequencies = {}

    # Split the contents into words
    file_contents = file_contents.split()

    # loop through every word
    for line in file_contents:
        # Contatenate every word
        words = ''.join(w for w in line if w.isalpha())
        # Check if word is not a uninetersting_words
        if words.lower() not in uninteresting_words:
            # Get the number of occurences
            frequencies[words.lower()] = frequencies.get(words, 0) + 1

    # returns the frequencies from words
    return frequencies


def generate_word_cloud(frequencies):
    """Gets the dictionary from calcualte_frequencies and returns a numpy array  """

    # Instantiate word cloud
    cloud = wordcloud.WordCloud()
    # Create a word_cloud from words and frequencie
    cloud.generate_from_frequencies(frequencies)
    # Export to image file.
    cloud.to_file(image_name(fname))
    # returns a numpy array
    return cloud.to_array()


# Get the File
try:
    fname = input("Enter File Name: ")
    fread = open(fname)
    file = fread.read()
except Exception as e:
    print(e)
else:  
    frequencies = calculate_frequencies(file)
    myimage = generate_word_cloud(frequencies)

    # Display an image
    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')
    plt.show()
