from tkinter import *
from tkinter import ttk
import numpy as np

from config import *
from element import ElementsManager
from sort import Sort

def shuffle_elements():
    Em.set_element_quantity(element_quantity_scale.get())
    sorting_start_button["state"] = "normal"
    sorting_start_button["bg"] = COLOR_DARK_2
    Em.createElements()

def start_sorting():
    current_value = sorting_combobox.get()
    if current_value:
        element_quantity_scale['state'] = 'disabled'
        element_shuffle_button["state"] = "disabled"
        sorting_start_button["state"] = "disabled"
        element_shuffle_button["bg"] = COLOR_LIGHT_1
        sorting_start_button["bg"] = COLOR_LIGHT_1
        if current_value == Sort.BUBBLE_SORT.value: Em.bubble_sort()
        element_quantity_scale['state'] = 'active'
        element_shuffle_button["state"] = "normal"
        element_shuffle_button["bg"] = COLOR_DARK_2
    

window = Tk()
window.title("Sorting visualizer")
window['bg'] = COLOR_DARK_1 
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
window.resizable(width=False, height=False)

ui_frame = LabelFrame(window, text="UI", bg=COLOR_DARK_1 , fg=COLOR_LIGHT_2)
element_shuffle_button = Button(ui_frame, text="Shuffle", font=40, bg=COLOR_DARK_2, fg="White", command=shuffle_elements)
sorting_label = Label(ui_frame, text="Choose sorting algorithm:", font=36, bg=COLOR_DARK_1 , fg=COLOR_LIGHT_2)
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground=COLOR_LIGHT_2, background= COLOR_DARK_2)
sorting_combobox = ttk.Combobox(ui_frame)
sorting_combobox['values'] = [e.value for e in Sort]
sorting_start_button = Button(ui_frame, text="Start", font=40, bg=COLOR_DARK_2, fg="White", command=start_sorting)
element_quantity_scale = Scale(ui_frame, from_=50, to=450, orient=HORIZONTAL, bg=COLOR_DARK_2, fg=COLOR_LIGHT_2)


output_canvas = Canvas(window, bg='black')

ui_frame.place(relx = 0.05, rely = 0.05,  relwidth=0.9, relheight=0.15)
element_shuffle_button.place(relx=0.02, rely=0.5, relheight=0.5, relwidth=0.18)
sorting_label.place(relx=0.2, rely=0.25, relheight=0.5, relwidth=0.3)
sorting_combobox.place(relx=0.48, rely = 0.25, relheight=0.5, relwidth=0.28)
sorting_start_button.place(relx=0.8, rely=0.25, relheight=0.5, relwidth=0.18)
element_quantity_scale.place(relx=0.02, rely=0, relheight=0.48, relwidth=0.177)


output_canvas.place(relx = 0.05, rely = 0.3,  relwidth=0.9, relheight=0.65)


Em = ElementsManager(output_canvas)
window.mainloop()