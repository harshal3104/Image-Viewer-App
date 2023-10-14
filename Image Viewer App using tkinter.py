from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Image Viewer")
ico = Image.open('C:/Users/Lenovo/Downloads/image___s___/camera.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.resizable(False,False)


img1=ImageTk.PhotoImage(Image.open("C:/Users/Lenovo/Downloads/image___s___/shinchan.png"))
img2=ImageTk.PhotoImage(Image.open("C:/Users/Lenovo/Downloads/image___s___/spongebob.png"))
img3=ImageTk.PhotoImage(Image.open("C:/Users/Lenovo/Downloads/image___s___/squidward.png"))
img4=ImageTk.PhotoImage(Image.open("C:/Users/Lenovo/Downloads/image___s___/spongebob-patrick.png"))
img5=ImageTk.PhotoImage(Image.open("C:/Users/Lenovo/Downloads/image___s___/umaru-chan.png"))

imgs=[img1,img2,img3,img4,img5]

status=Label(root,text="Image 1 of " + str(len(imgs)),bd=1,relief=SUNKEN,anchor=E)

my_label=Label(image=img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=imgs[img_num-1])
    button_forward=Button(root,text=">>",command=lambda:forward(img_num+1))
    button_back=Button(root,text="<<",command=lambda:back(img_num-1))

    if img_num==5:
        button_forward=Button(root,text=">>",state=DISABLED)
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status=Label(root,text="Image " + str(img_num) + " of " + str(len(imgs)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)





def back(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=imgs[img_num-1])
    button_forward=Button(root,text=">>",command=lambda:forward(img_num+1))
    button_back=Button(root,text="<<",command=lambda:back(img_num-1))

    if img_num==1:
        button_back=Button(root,text="<<",state=DISABLED)

    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status=Label(root,text="Image " + str(img_num) + " of " + str(len(imgs)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)





button_back=Button(root,text="<<",command=back,state=DISABLED)
button_exit=Button(root,text="Exit Program",command=root.destroy)
button_forward=Button(root,text=">>",command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)




root.mainloop()
