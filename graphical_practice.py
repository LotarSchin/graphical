from tkinter import *

def print_myvar(myvar):
    print(f'myvar = {myvar.get()}')


root = Tk()
# give a title
root.title("My first App")

# define our window size
w = 750
h = 280

# define canvas
canvas = Canvas(root, width=w, height=h)
canvas.pack()

#######################################################################
# draw a line on the canvas
my_line = canvas.create_line(100, 0, 100, 150, fill='dark sea green')

# draw a rectangle
my_rect = canvas.create_rectangle(50, 50, 100, 90, fill='green')

# draw an oval
my_oval = canvas.create_oval(120, 10, 180, 90, fill='cyan')

# draw text
my_text = canvas.create_text(260, 50, text='Hello World!', fill='blue', font='Arial 15 bold')
########################################################################

# create a button
my_btn = Button(root, text='close', width=20, height=1, bd='2', command=root.destroy)
my_btn.place(x=350, y=200)

# place an input field
my_input_text = StringVar()
input_field = Entry(textvariable=my_input_text)
my_win=canvas.create_window(400, 10, window=input_field)
input_field.place(x=100, y=150)

# place a checkbox
myvar = BooleanVar(name="MyInVar")
ckbox = Checkbutton(
    root,
    text="Yes or No?",
    variable=myvar,
    onvalue=True,
    offvalue=False,
    command=lambda: print_myvar(myvar)
    )
ckbox.place(x=150, y=200)

# create a button
my_btn = Button(root, text='Set text', width=20, height=1, bd='2', command=lambda: my_input_text.set(str(myvar.get())))
my_btn.place(x=350, y=120)


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