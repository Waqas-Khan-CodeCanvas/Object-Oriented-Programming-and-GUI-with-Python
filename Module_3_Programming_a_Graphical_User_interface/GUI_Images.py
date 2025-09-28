from tkinter import *

root = Tk()
root.title('PythonGuides')


photo = PhotoImage(file=r"smile.png")

# photo = photo.subsample(2)
lbl = Label(root,image = photo)
# lbl.image = photo
lbl.grid(column=0, row=3)

mainloop()