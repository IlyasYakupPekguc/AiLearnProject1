Project name: Generating Poetic Texts with Recurrent Neural Networks in Python

Hello, this a fresh start to my AI coding journey. The goal of this journey is to learn about AI and learn as much as possible while doing projects from YouTube. (source down below)
Source: https://www.youtube.com/playlist?list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-

Contents of the readme:
1- How and what the goal exactly is of my journey.
2- Notes i take while learning , and notes about the code
3- Error and problems i faced and how i fixed them
4- My thoughts about the project at the end of the project and what i plan to do next 

1-----------------------------------------
The goal explained in details:

First of all i'm a second grade student at Gazi University. I want to see what ai is about and learn more about the subject. This is my official second project about ai. my first
experience was within a compition named Teknofest. Agter gaining interest in AI i'm willing to learn more about this topic and i think the best way to do that is through projects. 
So this is my first YouTube based project. While learning i also intend to get a fuller GitHub page. So that's a double win-win. After finishing the project i intend to continue the
YouTube playlist if it apeals to me and my goals.

2-----------------------------------------
Coding Notes:

About the first part:
Converting the sentences to numbers and vice-versa
explenation:
we want to convert the available characters given in the code to numbers. we do this becasue it's easier to work with the numpy library and convert the numbers back in to characters

3-----------------------------------------
FİXED PROBLEMS:

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







