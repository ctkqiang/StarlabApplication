import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk, ImageGrab
import os as computer

window = tkinter.Tk()
window.geometry("520x800")
window.title("StarLab Bioscience Sdn Bhd")
window.resizable(False, False)
window.config(background="#150051")
window.iconbitmap("a.ico")

MENUBAR = Menu(window)
window.config(menu=MENUBAR)

image = Image.open("s.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(window, image=photo, text="", fg="white").pack()
venuelabel = Label(window, text="地點: ", background="#150051", fg="white", font=("kaiti", 13)).place(x=0, y=660)
contactLabel = Label(window, text="聯絡: ", background="#150051", font=("kaiti", 13), foreground="White").place(x=0,
                                                                                                                  y=720)
dateTEXT = Entry(window, width=27, font=("kaiti", 13)).place(x=170, y=380)
Venue = Text(window, width=35, background="#150051", fg="white", font=("kaiti", 13)).place(x=72, y=660, height=60)
person = Entry(window, width=35, background="#150051", fg="white", font=("kaiti",  13)).place(x=72, y=720)


# function :
def exitWindow():
    window.destroy()


def save():
    print("save")
    result = image.filename = asksaveasfilename(initialdir="/", title="Save As", filetypes=(
        ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif')))
    if result:
        x = window.winfo_rootx()
        y = window.winfo_rooty()
        height = window.winfo_height() + y
        width = window.winfo_width() + x
        ImageGrab.grab().crop((x, y, width, height)).save(result)


def website():
    computer.system("start https://www.starlabs.com.my/")


def tutorial():
    computer.system("start index.html")


# Add Menu Items:
file_menu = Menu(MENUBAR, tearoff=0)
file_menu.add_cascade(label="保存", command=save)
addon = Menu(file_menu, tearoff=0)
addon.add_command(label="保存到文件")
addon.add_command(label="Email To")
file_menu.add_command(label="進出", command=exitWindow)
MENUBAR.add_cascade(label="檔案", menu=file_menu)
help_menu = Menu(MENUBAR, tearoff=0)
MENUBAR.add_cascade(label="幫助", menu=help_menu)
help_menu.add_command(label="關於我們", command=website)
help_menu.add_command(label="如何用法?", command=tutorial)

window.mainloop()