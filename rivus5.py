from tkinter import *
root = Tk()
root.overrideredirect(1)


image = PhotoImage(file= "anonymous.jpg")
zx = int (image.width())
zy = int (image.height())
copy = image.copy()




canvas = Canvas(root,height=zy, width=zx, highlightthickness=0)
canvas.create_image(zx/2, zy/2, image=image)
canvas.pack()
root.mainloop()