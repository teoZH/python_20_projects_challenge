from PIL import Image
import tkinter
import random
from PIL import Image, ImageTk

choices = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']


def get_new_dice():
    global widget
    print('Click')
    some = ImageTk.PhotoImage(Image.open(random.choice(choices)))
    widget.configure(image=some)
    widget.image = some


root = tkinter.Tk()
img = ImageTk.PhotoImage(Image.open(random.choice(choices)))

widget = tkinter.Label(root, image=img)
widget.pack()
button = tkinter.Button(root, text='Dice', command=get_new_dice)
button.pack()

root.mainloop()
