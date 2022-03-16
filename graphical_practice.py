from tkinter import *

root = Tk()

# give a title
root.title("My first App")

# define our window size
w = 750
h = 280

# query display size
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# position to the center
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# Another notation, in that case we need to cast x and y:
#x = int((ws/2) - (w/2))
#y = int((hs/2) - (h/2))
#root.geometry(f'{w}x{h}+{x}+{y})

# open the window
root.mainloop()