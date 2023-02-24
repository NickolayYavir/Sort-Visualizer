from tkinter import *
from tkinter import ttk
import numpy as np

from config import *

window = Tk()
window.title("Sorting visualizer")
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
window.resizable(width=False, height=False)

canvas = Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, bg='#18122B')
canvas.pack()

ui_frame = LabelFrame(canvas, text="UI", bg='#18122B', fg='#635985')
ui_frame.place(relx = 0.05, rely = 0.05,  relwidth=0.9, relheight=0.15)

element_shuffle_button = Button(ui_frame, text="Shuffle", font=40, bg='#393053', fg="#635985")
element_shuffle_button.place(relx=0.02, rely=0.25, relheight=0.5, relwidth=0.18)

sorting_label = Label(ui_frame, text="Choose sorting algorithm:", font=36, bg="#18122B", fg="#635985")
sorting_label.place(relx=0.2, rely=0.25, relheight=0.5, relwidth=0.3)

style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#635985", background= "#393053")
sorting_combobox = ttk.Combobox(ui_frame)
sorting_combobox.place(relx=0.48, rely = 0.25, relheight=0.5, relwidth=0.28)

sorting_start_button = Button(ui_frame, text="Start", font=40, bg='#393053', fg='#635985')
sorting_start_button.place(relx=0.8, rely=0.25, relheight=0.5, relwidth=0.18)



output_frame = Frame(window, bg='black')
output_frame.place(relx = 0.05, rely = 0.3,  relwidth=0.9, relheight=0.65)


window.mainloop()