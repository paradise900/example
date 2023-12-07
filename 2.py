from tkinter import *
from tkinter.ttk import *


def slide(Progress_Bar):
    WAIT_TIME = 0.6
    import time
    Progress_Bar['value'] = 20
    window.update_idletasks()

    time.sleep(WAIT_TIME)
    Progress_Bar['value'] = 50
    window.update_idletasks()

    time.sleep(WAIT_TIME)
    Progress_Bar['value'] = 80
    window.update_idletasks()

    time.sleep(WAIT_TIME)
    Progress_Bar['value'] = 100


LENGTH = 250
window = Tk()
Progress_Bar = Progressbar(window, orient=HORIZONTAL,\
                        length=LENGTH, mode='determinate')
Progress_Bar.pack()
Button(window, text='Run', command=slide(Progress_Bar)).pack(pady=10)
mainloop()