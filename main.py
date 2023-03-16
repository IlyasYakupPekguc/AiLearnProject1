import random
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.models import Sequential #so we can create the neural network
from tensorflow.python.keras.layers import LSTM, Dense, Activation #this will be the memory of the model
from tensorflow.python.keras.optimizers import rmsprop_v2 #this is to compile the model

filepath = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt') #getting the text to train our model

text = open(filepath, 'rb').read().decode(encoding='udf-8').lower() #rb stands forread Binary, the lower case is so that the text will be guessing the text in lower case for better performance (it has les letter options)

#-----------------------------------------Part1


#NOTE: We need to change the format of the sentences to a numerical fomat so we can use the numpy library. the model canot train on sentences and let it predict the next senctences

#we're selecting a pat of the text so it's easier to train on
text = text[300000:80000] #from karakter 300000 to 800000

#we're selecting all possible charachter given in the data set (for ex. if T does not include in the text than T shouldn't be included)
characters = sorted(set(text)) #this code filters each charachter that occurs in the data set (1 time) sorted

#c = charachter, i= index
#first we want to convert the characters to numbers, train the model and the reverse the process
char_to_index = dict((c,i) for i, c in enumerate(characters)) 
#explenation:
"""
create a dictionary, which has the character as a key and the index as a value for al the i and c's in characters
for exp:
{'a' : 1, 'b' : 2.....}
"""

index_to_char = dict((i,c) for i, c in enumerate(characters)) #{1 : 'a', 2 : 'b'.....}



#-----------------------------------------Part2

# we want to look to the last 40 characters, we don't want to use too much data
SEQ_LENGTH = 40 
STEP_SİZE  = 3
#EXPLENATİON!!!!
"""
Hello World i love neuralNine because the videos are so great!
if Seq length is 5
hello world would be 1 sequal

step size is the shifted character count
lo Wo this would be the second sequal 

this would continue in this way
"""

sentences= []
next_characters = []

#we give an sentence and the next character should be predicted by the model
#"how are yo" "u"

for i in range(0,len(text) - SEQ_LENGTH, STEP_SİZE): # from the beginning of the text until the available last sew length with the step size of 3
    sentences.append(text[i: i+SEQ_LENGTH]) #from i to i+seqlength
    next_characters.append(text[i: i+SEQ_LENGTH])  #append is to add a single item to certain collection types

















