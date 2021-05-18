from tkinter import *
from tkinter import messagebox


def reset_entry():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')


def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)


def bmi_index(bmi):
    if bmi < 18:
        messagebox.showinfo('bmi ', f'BMI = {bmi} is Underweight')
    elif (bmi >= 18) and (bmi < 25) :
        messagebox.showinfo('bmi', f'BMI = {bmi} is Normal')
    elif (bmi >=25) and (bmi < 30):
        messagebox.showinfo('bmi', f'BMI = {bmi} is Overweight')
    elif (bmi >= 30):
        messagebox.showinfo('bmi', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('bmi', 'something went wrong!')

def ideal_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100
    Age=int(age_tf.get())

    if var.get()== 1:
        idealbmi= 0.5 * kg / (m / 100)**2 + 11.5
        idealbmi=round(idealbmi , 2)
        bmi_index(idealbmi)
    else:
        idealbmi=0.5 * kg / (m / 100)**2 + 0.03 * Age + 11
        idealbmi = round(idealbmi, 2)
        bmi_index(idealbmi)

def ideal_index(idealbmi):
    if idealbmi < 18:
        messagebox.showinfo('bmi ', f'BMI = {idealbmi} is Underweight')
    elif (idealbmi >= 18) and (idealbmi > 25) :
        messagebox.showinfo('bmi', f'BMI = {idealbmi} is Normal')
    elif (idealbmi >=25) and (idealbmi < 30):
        messagebox.showinfo('bmi', f'BMI = {idealbmi} is Overweight')
    elif (idealbmi >= 30):
        messagebox.showinfo('bmi', f'BMI = {idealbmi} is Obesity')
    else:
        messagebox.showerror('bmi', 'something went wrong!')


ws = Tk()
ws.title('BMI calculator')
ws.geometry('400x300')


var = IntVar()

frame = Frame(
    ws,
    padx=10,
    pady=10
)
frame.pack(expand=True)

age_lb = Label(
    frame,
    text="Enter Age (2 - 50)"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame,
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text='Male',
    variable=var,
    value=1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text='Female',
    variable=var,
    value=2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

frame4 = Frame(frame)
frame4.grid(row=6, column=2 ,pady=10)

reset_btn = Button(
    frame4,
    text='Reset',
    borderwidth=12,
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame4,
    text='Exit',
    borderwidth=12,
    command=lambda: ws.destroy()
)
exit_btn.pack(side=RIGHT)
ideal_Button = Button(
    frame3,
    text='Calculate ideal bmi',
    command=ideal_bmi
)
ideal_Button.pack(side=LEFT)


ws.mainloop()

