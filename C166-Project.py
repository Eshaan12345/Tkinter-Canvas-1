from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("900x600")
root.title("Canvas Painter")
root.configure(background = "gray25")

canvas = Canvas(root, width = 870, height = 440)
canvas.place(relx = 0.5, rely = 0.38, anchor = CENTER)

startx_label = Label(root, text = "Start X")
startx_label.place(relx = 0.05, rely = 0.85, anchor = CENTER)

startx_entry = Entry(root, width = 10)
startx_entry.place(relx = 0.12, rely = 0.85, anchor = CENTER)

starty_label = Label(root, text = "Start Y")
starty_label.place(relx = 0.05, rely = 0.9, anchor = CENTER)

starty_entry = Entry(root, width = 10)
starty_entry.place(relx = 0.12, rely = 0.9, anchor = CENTER)

endx_label = Label(root, text = "End X")
endx_label.place(relx = 0.2, rely = 0.85, anchor = CENTER)

endx_entry = Entry(root, width = 10)
endx_entry.place(relx = 0.28, rely = 0.85, anchor = CENTER)

endy_label = Label(root, text = "End Y")
endy_label.place(relx = 0.2, rely = 0.9, anchor = CENTER)

endy_entry = Entry(root, width = 10)
endy_entry.place(relx = 0.28, rely = 0.9, anchor = CENTER)

color_label = Label(root, text = "Color")
color_label.place(relx = 0.4, rely = 0.87, anchor = CENTER)

color = StringVar()
values = ["Black", "Blue", "Green", "Red", "Yellow", "Orange", "Purple", "Pink"]
dropdown = ttk.Combobox(root, value = values, textvariable = color)
dropdown.place(relx = 0.52, rely = 0.87, anchor = CENTER)

startx = 0 
starty = 0 
endx = 0 
endy = 0 

def confirm():
    global color
    global startx
    global starty
    global endx
    global endy
    
    startx = int(startx_entry.get())
    starty = int(starty_entry.get())
    endx = int(endx_entry.get())
    endy = int(endy_entry.get())
    
    print(startx)
    print(starty)
    print(endx)
    print(endy)
    
confirm_button = Button(root, text = "Confirm", command = confirm)
confirm_button.place(relx = 0.8, rely = 0.87, anchor = CENTER)

root.mainloop()