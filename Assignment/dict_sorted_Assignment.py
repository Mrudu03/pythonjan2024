"""
Assignment
==========
choose a large sentence greater than 150 words and perform the following
1) character frequency analyses
    a) case sensitive
        {
            'P': 1,
            'y': 2,
            't : 5
            ....
        }
    b) case insensitive
        {
            'p': 2,
            'y': 2,
            't : 5
            .....
        }
        HINT: str.lower()
2) word frequency analyses
    a) case sensitive
    b) case insensitive
    HINT: str.split()

3) cleansed_words frequency analyses
        HINT: string module -> string.punctuation
    a) case sensitive
    b) case insensitive

    Are you coming?  --> ['Are', 'you', 'coming']

"""
sentence = """Python, a versatile and powerful programming language, has become a cornerstone in software development, 
data science, artificial intelligence, and web development. Known for its readability and simplicity, 
Python facilitates efficient code writing and maintenance, making it an ideal choice for beginners and seasoned developers alike? 
Its extensive standard library and vibrant community support offer a plethora of modules and frameworks, accelerating development processes. 
Python's object-oriented, high-level syntax enhances code readability and encourages modular design, fostering code reuse and maintainability. 
With dynamic typing and automatic memory management, "Python" enables rapid prototyping and agile development. 
Its popularity continues to surge as it seamlessly integrates with other languages and technologies, 
making it an indispensable tool for a wide range of applications, from building web applications to scientific computing and machine learning.
"""
import string
#frequency for case sensitive

frequency = {}
for each_char in sentence:
    if each_char.isalpha():
        if each_char in frequency: # key is present
            frequency[each_char] = frequency[each_char] + 1
        else:
            frequency[each_char] = 1
print(frequency)
print()

#for case in sesitive
frequency = {}
for each_char in sentence:
    if each_char.isalpha():
        each_char = each_char.lower()
        if each_char in frequency: # key is present
            frequency[each_char] = frequency[each_char] + 1
        else:
            frequency[each_char] = 1
print(frequency)

print()
#word frequency analyses for case sensitive

words_in_sentence = sentence.split()
frequency = {}
for word in words_in_sentence:
    if word in frequency: # key is present
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1
print(frequency)

print()

#word frequency analyses for case in-sensitive 

words = sentence.split()
words_in_sentence = []
for w in words:
    w = w.lower()
    words_in_sentence.append(w)
frequency = {}
for word in words_in_sentence:
    if word in frequency: # key is present
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1
print(frequency)

print()
#cleansed words
words = sentence.split()
words_in_sentence = []
for w in words:
    translator = (str.maketrans("", "", string.punctuation))
    w = w.translate(translator)
    words_in_sentence.append(w)
frequency = {}
for word in words_in_sentence:
    if word in frequency: # key is present
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1
print(frequency)

print()
#cleansed words with case insensitive
words = sentence.split()
words_in_sentence = []
for w in words:
    translator = (str.maketrans("", "", string.punctuation))
    w = w.translate(translator).lower()
    words_in_sentence.append(w)
frequency = {}
for word in words_in_sentence:
    if word in frequency: # key is present
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1
print(frequency)