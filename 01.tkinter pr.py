import tkinter as tk

root = tk.Tk()
root.geometry('600x800')
root.title("Jeeban")
#varibale type in tkinter
#BooleanVar, DoubleVar, IntVar,StringVar
# The variable class has two methods get and set

name = tk.StringVar()
phone_no = tk.IntVar()
gender = tk.StringVar()
#creating a frame 
frame0 = tk.Frame(root)
frame0.pack(fill="x")
label0 = tk.Label(frame0,text="Welcome to Python Class",font='Gerogia 15 bold')
label0.pack(pady=50)

frame = tk.Frame(root,borderwidth=3)
frame.pack(anchor='w',padx=165,pady=130)

#adding username and password label
label1 = tk.Label(frame,text="Name: ")
label1.grid(row=0,column=0,padx=20)
label2 = tk.Label(frame,text="Phone No: ")
label2.grid(row=1,column=0,padx=20)
label2 = tk.Label(frame,text="Gender: ")
label2.grid(row=2,column=0,padx=20)
#Entry Widget in which you can enter the value
user_entry = tk.Entry(frame,textvariable=name)
pass_entry = tk.Entry(frame,textvariable=phone_no)
gender_entry = tk.Entry(frame,textvariable=gender)

user_entry.grid(row=0,column=1)
pass_entry.grid(row=1,column=1)
gender_entry.grid(row=2,column=1)

def getvals():
    print(name.get())
    print(phone_no.get())
    print(gender.get())

button = tk.Button(frame,text="Submit",command=getvals,fg="white",bg='red')
button.grid(row=3,column=1)
root.mainloop()
