from tkinter import *
from tkinter import messagebox

def measure_bmi():
    weight = int(weight_en.get())  #get value of weight
    height = int(height_en.get())/100  #get the value of height and convert to meters
    BMI = weight/(height*height)  #formula to calculate the BMI
    bmi = round(BMI, 1)  #to round off the decimal places to 1 (for easy understanding)
    bmi_index(BMI)

def bmi_index(BMI):
    
    if (BMI < 18.5):
        messagebox.showinfo('BMI Calculator', f'BMI = {BMI} is Underweight, It is time to intake Proteins and Fats')
    elif (BMI > 18.5) and (BMI < 24.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {BMI} is Normal, Keep Going')
    elif (BMI > 24.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {BMI} is Overweight, It is time to join gym and lose weight')
    else:
        messagebox.showerror('BMI Calculator', 'something went wrong!')   

BMI = Tk()
BMI.title('BMI Calculator')
BMI.geometry('520x470')
BMI.config(bg='orange')

var = IntVar()

#Creating frames for data insertion like height, weight and age

frame = Frame(  
    BMI,
    padx=15, 
    pady=15,
    bg='light grey'
)
frame.pack(expand=True)

#Label the frames
age_lb = Label(
    frame,
    text="Enter Your Age",
    bg='light grey'
)
age_lb.grid(row=1, column=1)

height_lb = Label(
    frame,
    text="Enter Height (in cm)  ",
    bg='light grey'
)
height_lb.grid(row=3, column=1, pady=8)

weight_lb = Label(
    frame,
    text="Enter Weight (in kg)  ",
    bg='light grey'
)
weight_lb.grid(row=4, column=1)

#Get values/entries from the users
age_en = Entry(
    frame, 
)
age_en.grid(row=1, column=2, pady=8)

height_en = Entry(
    frame,
)
height_en.grid(row=3, column=2, pady=8)



weight_en = Entry(
    frame,
)
weight_en.grid(row=4, column=2, pady=8)

frame2 = Frame(
    frame
)
frame2.grid(row=5, columnspan=3, pady=16)

#Including buttons like calculate and exit
calculate_btn = Button(
    frame2,
    text='Calculate',
    command=measure_bmi
)
calculate_btn.pack(side=LEFT)


exit_btn = Button(
    frame2,
    text='Exit',
    command=lambda:BMI.destroy()
)
exit_btn.pack(side=RIGHT)

BMI.mainloop()
