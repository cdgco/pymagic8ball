from random import randint
import tkinter

top = tkinter.Tk()
top.title("Magic 8 Ball")
top.geometry("450x400")
top.configure(background="white")
img2 = tkinter.PhotoImage(file='start.gif')
top.call('wm', 'iconphoto', top._w, img2)

img_path = "start.gif"
photo = tkinter.PhotoImage(file=img_path)
global label
label = tkinter.Label(top, image=photo)
label.photo = photo
label.pack(pady="10", side="top")
label.configure(bg="white")


def ball():
    global label
    label.pack_forget()
    dicenum = randint(0, 4)
    dicestr = str(dicenum)
    img_path = dicestr + ".gif"
    photo = tkinter.PhotoImage(file=img_path)
    label = tkinter.Label(top, image=photo)
    label.photo = photo
    label.pack(pady="10", side="top")
    label.configure(bg="white")


B = tkinter.Button(top, text="Shake Ball", command=ball)
B.pack(side="bottom", pady="50", ipadx="10")

top.mainloop()
