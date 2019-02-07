#chain of inputs using Markov
import numpy as np
import threading
import random

#import file
file1='input.csv'
file2='input2.csv'

text= open(file2, ).read()
layout= textLower.lower().split()

dictionaryText={}
pygame.init()
pygame.mixer.music.load('audio.wav')

root=Tk()
root.title("Link")
#the number of words
randomNum=random.randint(6,22)
textOutline=Text(root, font=('Arial MS', 20))

#Center
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2



def resetButton():
    textOutline.delete('1.0', END)
    
def concat_pair(var1, var2):
    
def runLoop():
    root.mainloop()
    
    
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Clear", command=resetButton)
root.config(menu=menubar)
root.mainloop()
