#A sample

import sys

if sys.version_info[0] < 3:
	import Tkinter as Tk 	# for Python 2
else:
	import tkinter as Tk   	# for Python 3

print('Click to close')

root = Tk.Tk()      # or 'top'

L2 = Tk.Label(root, text = 'This is another label')
L2.pack()
root.mainloop()
