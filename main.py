from tkinter import *
from tkinter import ttk

from config import *
from element import ElementsManager
from sort import Sort

def shuffle_elements():
    Em.set_element_quantity(element_quantity_scale.get())
    sorting_start_button.configure(text="Start", state='normal', bg=COLOR_DARK_2)
    sorting_delay_scale['state'] = 'normal'
    sorting_combobox['state'] = 'readonly'
    
    Em.createElements()

def stop_sorting():
    Em.change_sorting_state()
    sorting_start_button.configure(text="Start", command=start_sorting, state='disabled', bg=COLOR_LIGHT_1)

def start_sorting():
    Em.set_sotring_delay(sorting_delay_scale.get())
    sorting_algorithm = sorting_combobox.get()
    if sorting_algorithm:
        Em.change_sorting_state()
        element_quantity_scale['state'] = 'disabled'
        sorting_delay_scale['state'] = 'disabled'
        element_shuffle_button["state"] = "disabled"
        sorting_combobox['state'] = 'disable'
        sorting_start_button.configure(text="Stop", command=stop_sorting) 
        element_shuffle_button["bg"] = COLOR_LIGHT_1
        sorting_start_button["bg"] = COLOR_LIGHT_1
        if sorting_algorithm == Sort.BUBBLE_SORT.value: Em.bubble_sort()
        if sorting_algorithm == Sort.INSERTION_SORT.value: Em.insertion_sort()
        if sorting_algorithm == Sort.SELECTION_SORT.value: Em.selection_sort()
        if sorting_algorithm == Sort.QUIK_SORT.value: Em.quick_sort()
        sorting_start_button.configure(text="Start", command=start_sorting, state='disabled', bg=COLOR_LIGHT_1)
        element_quantity_scale['state'] = 'normal'
        element_shuffle_button.config(state='normal', bg=COLOR_DARK_2)

    
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
sorting_combobox = ttk.Combobox(ui_frame, state='readonly')
sorting_combobox['values'] = [e.value for e in Sort]
sorting_combobox.current(0)
sorting_start_button = Button(ui_frame, text="Start", font=40, bg=COLOR_DARK_2, fg="White", command=start_sorting)
element_quantity_scale = Scale(ui_frame, from_=50, to=450, orient=HORIZONTAL, bg=COLOR_DARK_2, fg=COLOR_LIGHT_2)
sorting_delay_scale = Scale(ui_frame, from_=0.0, to=1.0, digits=3, resolution=0.01, orient=HORIZONTAL, bg=COLOR_DARK_2, fg=COLOR_LIGHT_2)
output_canvas = Canvas(window, bg='black')

ui_frame.place(relx = 0.05, rely = 0.05,  relwidth=0.9, relheight=0.15)
element_shuffle_button.place(relx=0.02, rely=0.5, relheight=0.5, relwidth=0.18)
sorting_label.place(relx=0.2, rely=0.25, relheight=0.5, relwidth=0.3)
sorting_combobox.place(relx=0.48, rely = 0.25, relheight=0.5, relwidth=0.28)
sorting_start_button.place(relx=0.8, rely=0.5, relheight=0.5, relwidth=0.18)
element_quantity_scale.place(relx=0.02, rely=0, relheight=0.48, relwidth=0.177)
sorting_delay_scale.place(relx=0.8, rely=0, relheight=0.48, relwidth=0.177)
output_canvas.place(relx = 0.05, rely = 0.3,  relwidth=0.9, relheight=0.65)

Em = ElementsManager(output_canvas)
window.mainloop()