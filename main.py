import random
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.models import Sequential #so we can create the neural network
from tensorflow.python.keras.layers import LSTM, Dense, Activation #this will be the memory of the model
from tensorflow.python.keras.optimizers import rmsprop_v2 #this is to compile the model

filepath = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt') #getting the text to train our model

text = open(filepath, 'rb').read().decode(encoding='udf-8').lower() #rb stands forread Binary, the lower case is so that the text will be guessing the text in lower case for better performance (it has les letter options)



