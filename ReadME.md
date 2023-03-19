Project name: Generating Poetic Texts with Recurrent Neural Networks in Python

Hello, this a fresh start to my AI coding journey. The goal of this journey is to learn about AI and learn as much as possible while doing projects from YouTube. (source down below)
Source: https://www.youtube.com/playlist?list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-

Contents of the readme:
1- How and what the goal exactly is of my journey.
2- Notes i take while learning , and notes about the code
3- Error and problems i faced and how i fixed them
4- My thoughts about the project at the end of the project and what i plan to do next 


1-----------------------------------------
<span style="background-color: #0000FF">THE GOAL EXPLAINED IN DETAILS:</span>


First of all i'm a second grade student at Gazi University. I want to see what ai is about and learn more about the subject. This is my official second project about ai. my first
experience was within a compition named Teknofest. Agter gaining interest in AI i'm willing to learn more about this topic and i think the best way to do that is through projects. 
So this is my first YouTube based project. While learning i also intend to get a fuller GitHub page. So that's a double win-win. After finishing the project i intend to continue the
YouTube playlist if it apeals to me and my goals.


2-----------------------------------------
<span style="background-color: #0000FF">CODING NOTES:</span>


About the first part:
Converting the sentences to numbers and vice-versa
explenation:
we want to convert the available characters given in the code to numbers. we do this becasue it's easier to work with the numpy library and convert the numbers back in to characters
 
About the code below: 
this is the traingin code with explenation, the main class will have the none explained code.
After we trained the model we don't have to train it over and over again so what we do is get this part out of the code (maybe use jupiter for future projects?).
for easier readability i modified the comment above the code section for easier commenting.


#-----------------------------------------------------------------TRAİNİNG PART

model = Sequential()
model.add(LSTM(128,input_shape =(SEQ_LENGTH, len(characters)))) #this layer is so it can remember the past given characters ----- also , means times (*)
model.add(Dense(len(characters)))
model.add(Activation('softmax')) #the softmax layer is used for probabilities for ex. the next character could be %70 a 'b' or %30 a 'n' 

"""
İMPORTANT:
when feeding the model it will always look at the given input atm and not the prev given inputs, that's why we use a memory layer (LSTM)
"""

#model.compile(loss ='categorical_crossentropy', optimizer=rmsprop_v2(lr = 0.01)) #lr = learningrate
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.01)) #lr = learningrate

model.fit(x,y, batch_size=256, epochs=4)

model.save('textgenerator.model')

#-----------------------------------------------------------------TRAİNİNG PART


<mark>NOTE:</mark>
We don't need to use some code that we've previous used to train the model, so what i can try to use is a jupiter notbook
instead of commenting out each part that i don't need to use anymore. That will make the code easier to understand later 
and it won't get confusing with commenting everything out.

Also try to use the HTML5 futures more ein the md folder for easier use such as markdowns etc..


3-----------------------------------------
<span style="background-color: #0000FF">FİXED PROBLEMS:</span>


i had an issue with keras and tensorflow.
my issue:

i wanted to use the RMSprop libray but the problem was that i could not import the RMSprop library.
İ used the rmsprop_v2 library thinking it would be no issue.
After completing the code until the training section i found out that i needed the RMSprop library instead the one i was using.
After reasearching for a few houres i thought it was a version problem (i had this issue before in another project.)
İn my research i found out this was not the problem. İ just couldn't wrap my head around why i couldn't use the RMSprop library not work.
İ found out in my research that 
"from tensorflow.keras.optimizers import RMSprop" was the library i needed but i just couldn't import it and i used a lower library
"from tensorflow.python.keras.optimizers import rmsprop_v2"
To get around this problem i used 
"import keras as ks
from keras.optimizers import RMSprop"
This solved the issue. 
Even if this is a simple issue to fix, for someone who is fairluy new to the concept it was a pretty iritating challenge.
While rersearching i learned a few things that will help me in my future projects.


4-----------------------------------------
<span style="background-color: #0000FF">PROJECT THOUGHTS AND TIPS:</span>

Thoughts:

First i think that it's a easy basic ai project to understand a bit about the topics.
It covers basic coding, training a model and sme other stuff.
I defenitly have to do many more projects before i start to become comfortable with doing projects on my own.

Let's see what the future holds for me.
I need to understand coding better and also the general python and AI stuff.

TIPS:
-Try to use jupiter Notebook.
-Watch tutorials and projects at the same time to get more information about the subjects. 





