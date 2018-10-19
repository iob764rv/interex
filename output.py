#A sample

import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk 	# for Python 2
else:
	import tkinter as Tk   	# for Python 3

print('Click to close')
string="String" #string displayed after click
def entryinformation():
    #
    L2.config(text=string.get())
	
root = Tk.Tk()      # top
L2 = Tk.Label(root, text = string)
L2.pack()

B1 = Tk.Button(root, text = 'Button', command = entryinformation)
B1.pack(side = Tk.BOTTOM)

#Entry
string = Tk.StringVar()
E1 = Tk.Entry(root, textvariable = string)
E1.pack()

S1 = Tk.Scale(root, orient=HORIZONTAL, from_=1, to=10,)
S1.pack()

root.mainloop()
