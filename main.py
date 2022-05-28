import string
# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
        textfile= open(filename)
        file = textfile.read()
        return file
    # [assignment] Add your code here 
       


def count_words():
    text = read_file_content("./story.txt")
    text=text.strip()
    text=text.replace('\n',"")
    text = text.translate(str.maketrans('', '', string.punctuation))
    text=text.split(' ')
    while("" in text):
        text.remove("")

    frequency={}
    for item in text:
        if (item in frequency):
            frequency[item]+=1

        else:
            frequency[item]=1
    return frequency
    # [assignment] Add your code here

count =count_words()
print(count)