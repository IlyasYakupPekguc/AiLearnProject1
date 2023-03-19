import random
import numpy as np
import tensorflow as tf
import keras as ks
from keras.models import Sequential #so we can create the neural network
from keras.layers import LSTM, Dense, Activation #this will be the memory of the model
from keras.optimizers import RMSprop #this is to compile the model 


filepath = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt') #getting the text to train our model

text = open(filepath, 'rb').read().decode(encoding='utf-8').lower() #rb stands forread Binary, the lower case is so that the text will be guessing the text in lower case for better performance (it has les letter options)

#-----------------------------------------Part1


#NOTE: We need to change the format of the sentences to a numerical fomat so we can use the numpy library. the model canot train on sentences and let it predict the next senctences

#we're selecting a pat of the text so it's easier to train on
text = text[300000:800000] #from karakter 300000 to 800000

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
STEP_SIZE  = 3
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
next_char = []

#we give an sentence and the next character should be predicted by the model
#"how are yo" "u"

for i in range(0,len(text) - SEQ_LENGTH, STEP_SIZE): # from the beginning of the text until the available last sew length with the step size of 3
    sentences.append(text[i: i+SEQ_LENGTH]) #from i to i+seqlength
    next_char.append(text[i+SEQ_LENGTH])  #append is to add a single item to certain collection types


x = np.zeros((len(sentences), SEQ_LENGTH,len(characters)), dtype= bool) #let's think about a 3d shape,for ex.: x is for sentences, y is for characters, z is for seq lngth so if in a specific koordinate a sertain character occurs we gpnna set that to true
#the use for zeros is that the table is full of zeros , only the needed chgaracter is given true (1)

y = np.zeros((len(sentences), len(characters)), dtype=bool)

#enumurate: allows you to keep track of the number of iterations (loops) in a loop
for i, sentence in enumerate(sentences):  #running one for loop over all sentences   
    for t, character in enumerate(sentence):
        x[i,t,char_to_index[character]] = 1 #(1 stands for true)
    y[i, char_to_index[next_char[i]]] = 1

"""
we enumurate each sentences with the first for loop, after that we enumurate each character of the sentences with 
the second for loop 
"""
#-----------------------------------------------------------------TRAİNİNG PART See README.md 28-49
"""
İMPORTANT:
when feeding the model it will always look at the given input atm and not the prev given inputs, that's why we use a memory layer (LSTM)
"""
"""model = Sequential()
model.add(LSTM(128,input_shape =(SEQ_LENGTH, len(characters)))) #this layer is so it can remember the past given characters ----- also , means times (*)
model.add(Dense(len(characters)))
model.add(Activation('softmax')) #the softmax layer is used for probabilities for ex. the next character could be %70 a 'b' or %30 a 'n' 

#model.compile(loss ='categorical_crossentropy', optimizer=rmsprop_v2(lr = 0.01)) #lr = learningrate
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.01)) #lr = learningrate

model.fit(x,y, batch_size=256, epochs=4)

model.save('textgenerator.model')
"""
#-----------------------------------------------------------------TRAİNİNG PART


model = tf.keras.models.load_model('texgenerator.model') #after the training we can just load he model instead of training the model over and over again.

#this function is explained in the keras tutorial of the instructor, so what i'm gonna do is watch that video while doing another project.
#what this function basicly is that charachter it's gonna predict is gonna have a tempurature, based on the tempirature it's gonna be experimental or not.
# the higher the tempurature the more experimental the character is going to be   

def sample(preds, temperature = 1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1,preds ,1)
    return np.argmax(probas)

#we're coping the first 40 characters direkt from the shakespeare text, but if we want to have thee text completely generated we have to delete the first 40 characters first 
def generate_text(length, temperature): 
    start_index = random.randint(0, len(text) - SEQ_LENGTH-1)
    generate_text = ''
    sentence = text[start_index: start_index + SEQ_LENGTH]
    generate_text += sentence
    for i in range(length):
        x = np.zeros((1,SEQ_LENGTH,len(characters)))
        for t , character in enumerate(sentence):
            x[0, t, char_to_index[character]] = 1

        predictions = model.predict(x, verbose = 0)[0] #some complicated stuff :(
        next_index = sample(predictions,temperature)
        next_chararcter = index_to_char[next_index]

        generated += next_chararcter
        sentence = sentence[1:] + next_chararcter

    return generated



