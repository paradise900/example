from tkinter import * 
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import ttk
import pygame


def clicked(input_text, tab1):
    key = input_text[:3] + '-'
    for ch in input_text:
        key += str((ord(ch) - ord('A')) % 10)
    key += '-' + input_text[-3:]
    lbl = Label(tab1, text=f'Your key: {key}', \
        font=('Arial Bold', 30), relief="groove")
    lbl.grid(row=4)
    lbl.place(anchor=CENTER, relx=0.5, rely=0.5)


def play():
    pygame.mixer.music.load("Glass.aiff")
    pygame.mixer.music.play()


HIGHT = 720
WIDTH = 1280
window = Tk()
window.title('Key generator for GTA 6')
window.geometry(f"{WIDTH}x{HIGHT}")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='main')  
tab_control.add(tab2, text='extra')  
tab_control.pack(expand=1, fill='both') 

image_game = PhotoImage(file="9516f5b5e60f601ec961deaeddd6f3e4.png")
background_label = Label(tab1, image=image_game)  
background_label.place(x=0, y=0, relwidth=1, relheight=1)

image_bg = PhotoImage(file="maxresdefault.png")
background_label1 = Label(tab2, image=image_bg, border=50)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)

lbl_hi = Label(tab1, text='Enter part of key!', \
    font=('Arial Bold', 40), relief="groove")
lbl_hi.grid(column=0, row=0)
lbl_hi.place(anchor=CENTER, relx=0.5, rely=0.1)

text_enter = Entry(tab1, width=10, borderwidth=0)
text_enter.grid(column=0, row=0)
text_enter.place(anchor=CENTER, relx=0.5, rely=0.25)
text_enter.focus()

btn = Button(tab1, text='generate', bg='red', fg='black', \
    command=lambda: clicked(text_enter.get(), tab1), border=0)
btn.grid(column=0)
btn.place(anchor=CENTER, relx=0.5, rely=0.35)

pygame.mixer.init()

my_button = Button(tab2, text="Play Song", \
    font=("Helvetica", 32), command=play)
my_button.pack(pady=200)

window.mainloop()