import tkinter as tk

root = tk.Tk()
root.geometry('600x800')
root.title("Jeeban")
#varibale type in tkinter
#BooleanVar, DoubleVar, IntVar,StringVar
# The variable class has two methods get and set

user_value = tk.StringVar()
password = tk.StringVar()

#creating a frame 
frame = tk.Frame(root,borderwidth=3)
frame.pack(anchor='w',padx=120,pady=130)

#adding username and password label
label1 = tk.Label(frame,text="UserName: ")
label1.grid(row=0,column=0)
label2 = tk.Label(frame,text="Password: ")
label2.grid(row=1,column=0)
#Entry Widget in which you can enter the value
user_entry = tk.Entry(frame,textvariable=user_value)
pass_entry = tk.Entry(frame,textvariable=password)

user_entry.grid(row=0,column=1)
pass_entry.grid(row=1,column=1)

def getvals():
    print(user_value.get())
    print(password.get())

button = tk.Button(frame,text="Submit",command=getvals,fg="white",bg='red')
button.grid(row=2,column=1)
root.mainloop()

