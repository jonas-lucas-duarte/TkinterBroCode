from tkinter import *

# label = an area widget that holds text and /or an image within a window

window = Tk()

photo = PhotoImage(file='emoji.png')

label = Label(window, 
              text="bro, do you even code?",
              font=('Arial', 40, 'bold'), 
              fg='#00FF00', 
              bg='black',
              relief=RAISED,
              #relief=SUNKEN,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              #compound='top'
              compound='bottom')
label.pack()
#label.place(x=0, y=0)
#label.place(x=100, y=100)

window.mainloop()
