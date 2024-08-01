from tkinter import Label, Tk, Button, Entry
from PIL import Image, ImageTk

# Define l3 as a global variable
l3 = None

def convertor():
    global l3
    val = float(e.get())
    ans = (val * 9 / 5) + 32

    #destroying the already existing label
    if l3:
        l3.destroy()
    
    # Create a label to display the result
    l3 = Label(text=f'Temperature in Fahrenheit: {ans}', bg='grey', fg='white', font='timesnewroman 10 bold italic')
    l3.pack(anchor='nw')
    
    

r = Tk()
r.title('Temperature Converter')
r.geometry('250x350')
r.resizable(False,False)

# Open and convert JPEG image to PhotoImage format
background_image = Image.open("pic1.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to hold the background image
background_label = Label(r, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Create other widgets on top of the background
l1 = Label(r, text='Temperature Converter', font='timesnewroman 15 bold italic', bg='grey', fg='white', relief='raised', borderwidth='4')
l1.pack(fill='x')
l2 = Label(r, text='Enter the Temperature in Celsius:', font='timesnewroman 10 bold italic', bg='grey', fg='white', borderwidth='4', relief='ridge')
l2.pack(anchor='nw', pady='15')
e = Entry(r)
e.pack(anchor='nw')
b = Button(r, text='Enter', font='timesnewroman 10 bold italic', fg='white', bg='black', padx='8', borderwidth='5', relief='sunken', command=convertor)
b.pack(anchor='nw', pady='15', padx='20')



r.mainloop()
