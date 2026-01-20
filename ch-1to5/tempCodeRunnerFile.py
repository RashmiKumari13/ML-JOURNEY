"""1. Write a program to print Twinkle twinkle little star poem in python. 
2. Use REPL and print the table of 5 using it.  
3. Install an external module and use it to perform an operation of your interest.  
4. Write a python program to print the contents of a directory using the os module. 
Search online for the function which does that.  
5. Label the program written in problem 4 with comments.
"""

print("FIRST ANSWER: ")
print(''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr * 2)


#voices generate hogiiii 
import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, I am speaking from RASHMI SINGH SIDE")
engine.runAndWait()

from gtts import gTTS
import os
text = "नमस्ते, यह पाइथन से बनाई गई आवाज़ है"
tts = gTTS(text=text, lang='hi')
tts.save("voice.mp3")
os.system("start voice.mp3")   # Windows

import asyncio
import edge_tts
async def speak():
    communicate = edge_tts.Communicate(
        "नमस्ते, यह बहुत ही प्राकृतिक आवाज़ है",
        voice="hi-IN-SwaraNeural"
    )
    await communicate.save("edge_voice.mp3")
asyncio.run(speak())

#4. Write a python program to print the contents of a directory using the os module. 
#      Search online for the function which does that.
# 

import os  #  os inbuilt library h python me 
path = "E:/ML/python/Python_ChapterWise_Notes/code/ch-1to5"  #path h humare directory ka
contents = os.listdir(path)
print("Contents of the directory:")   
for item in contents:
    print(item)       #list de dega sare 


p1="ram"
p2="sam"
word=input("enter word:")
if((p1 in word) or (p2 in word)):
    print("TRUE")
else:
    print("FALSE")

for i in range(64):
    pass
i=0
while(i<45):
    print(i)
    i+=1