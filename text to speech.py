from tkinter import*
import pyttsx3

win=Tk()
win.title('voice')
win.geometry('420x200')

def func():
    x = Entry.get()
    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
    
label0 = Label(win, text = 'Enter your text here: ',font=('Arial',25, 'bold') )
label0.grid(row =0, column = 0)
Entry = Entry(win, width=22, font=('Arial',25))
Entry.grid(row =1, column=0,padx=15, pady=5)
button = Button(win, text ='Speak',font=('Arial',15,'bold'),command=func)
button.grid(row =3, column = 0, pady=20, padx= 70)


mainloop()
