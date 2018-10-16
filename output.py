#A sample

import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk 	# for Python 2
else:
	import tkinter as Tk   	# for Python 3

print('Click to close')
string="String" #string displayed after click
root = Tk.Tk()      # top
L2 = Tk.Label(root, text = string)
L2.pack()
root.mainloop()
