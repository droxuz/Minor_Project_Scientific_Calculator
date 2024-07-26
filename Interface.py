import customtkinter
import re
import ArithmeticFunctions
import database

#Sets base appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Creates connection to database
db = database.create_database()

#Creates root
#Adds frame to root 
root = customtkinter.CTk()
root.geometry("500x500")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)
root.resizable(False,False)

#Creates the text box to input values
entry = customtkinter.CTkEntry(frame, placeholder_text='', width=460, height=50, font=("Roboto",26))
entry.place(x=10, y=10)

#Creates functions for each button
def division_func():
    box_content = entry.get()
    if box_content and box_content[-1].isdigit() or box_content[-1] == ')':
        entry.insert(customtkinter.END,chr(247))

def multiplication_button():
    box_content = entry.get()
    if box_content and box_content[-1].isdigit() or box_content[-1] == ')':
        entry.insert(customtkinter.END,chr(215))

def subtraction_button():
    box_content = entry.get()
    if box_content and box_content[-1].isdigit() or box_content[-1] == ')':
        entry.insert(customtkinter.END,"−")

def addition_button():
    box_content = entry.get()
    if box_content and box_content[-1].isdigit() or box_content[-1] == ')':
        entry.insert(customtkinter.END,chr(43))
    
def updating_history(database_data):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    for i in database_data:
        history_button = customtkinter.CTkButton(scrollable_frame, text=i, width=140, height=28, font=('Roboto',28), fg_color=('transparent'))
        history_button.pack(padx=5, pady=5)

def equal_button():
    box_content = entry.get()
    print(box_content)
    box_content = box_content.replace(chr(247), '/')
    box_content = box_content.replace(chr(215), '*')
    box_content = box_content.replace("−", '-')
    if not re.match(r'^[0-9\+\-\*/\(\)\s]+$', box_content):
        print('Syntax Error: Invalid characters in expression')
        return
    result = ArithmeticFunctions.evaluate_expression(box_content)
    print(f"Result: {result}")
    entry.delete(0,customtkinter.END)
    entry.insert(0,result)    
    database.insert_data(db, box_content)
    database_data = database.fetch_data(db)
    print(database_data)
    updating_history(database_data)
    
    
def one_button():
    entry.insert(customtkinter.END,"1")
def two_button():
    entry.insert(customtkinter.END,"2")
def three_button():
    entry.insert(customtkinter.END,"3")
def four_button():
    entry.insert(customtkinter.END,"4")
def five_button():
    entry.insert(customtkinter.END,"5")
def six_button():
    entry.insert(customtkinter.END,"6")
def seven_button():
    entry.insert(customtkinter.END,"7")
def eight_button():
    entry.insert(customtkinter.END,"8")
def nine_button():
    entry.insert(customtkinter.END,"9")
def zero_button():
    entry.insert(customtkinter.END,"0")
def openbracket_button():
    entry.insert(customtkinter.END,"(")
def closebracket_button():
    entry.insert(customtkinter.END,")")
def clear_button():
    entry.delete(0,customtkinter.END)

#Creates Visual UI buttons
Division_Button = customtkinter.CTkButton(frame, command=division_func,text=chr(247), width=140, height=50, font=("Roboto", 26))
Division_Button.place(x=330, y=60)

Multiplication_Button = customtkinter.CTkButton(frame, command=multiplication_button, text=chr(215), width=140, height=50, font=("Roboto", 26))
Multiplication_Button.place(x=330, y=110)

Subtraction_Button = customtkinter.CTkButton(frame, command=subtraction_button, text="−", width=140, height=50, font=("Roboto", 26))
Subtraction_Button.place(x=330, y=160)

Addition_Button = customtkinter.CTkButton(frame, command=addition_button, text=chr(43), width=140, height=50, font=("Roboto", 26))
Addition_Button.place(x=330, y=210)

One_Button = customtkinter.CTkButton(frame, text='1', command=one_button, width=106.66, height=50, font=('Roboto',26))
One_Button.place(x=10, y=160)

Two_Button = customtkinter.CTkButton(frame, text='2', command=two_button, width=106.66, height=50, font=('Roboto',28))
Two_Button.place(x=115.66, y=160)

Three_Button = customtkinter.CTkButton(frame, text='3', command=three_button, width=106.66, height=50, font=('Roboto',28))
Three_Button.place(x=222.32, y=160)

Four_Button = customtkinter.CTkButton(frame, text='4', command=four_button, width=106.66, height=50, font=('Roboto',28))
Four_Button.place(x=10, y=110)

Five_Button = customtkinter.CTkButton(frame, text='5', command=five_button, width=106.66, height=50, font=('Roboto',28))
Five_Button.place(x=115.66, y=110)

Six_Button = customtkinter.CTkButton(frame, text='6', command=six_button, width=106.66, height=50, font=('Roboto',28))
Six_Button.place(x=222.32, y=110)

Seven_Button = customtkinter.CTkButton(frame, text='7', command=seven_button, width=106.66, height=50, font=('Roboto',28))
Seven_Button.place(x=10, y=60)

Eight_Button = customtkinter.CTkButton(frame, text='8', command=eight_button, width=106.66, height=50, font=('Roboto',28))
Eight_Button.place(x=115.66, y=60)

Nine_Button = customtkinter.CTkButton(frame, text='9', command=nine_button, width=106.66, height=50, font=('Roboto',28))
Nine_Button.place(x=222.32, y=60)

Zero_Button = customtkinter.CTkButton(frame, text='0', command=zero_button,width=106.66, height=50, font=('Roboto',28))
Zero_Button.place(x=10, y=210)

OpenBracket_Button = customtkinter.CTkButton(frame, text='(', command=openbracket_button, width=106.66, height=50, font=('Roboto',28))
OpenBracket_Button.place(x=115.66, y=210)

CloseBracket_Button = customtkinter.CTkButton(frame, text=')', command=closebracket_button, width=106.66, height=50, font=('Roboto',28))
CloseBracket_Button.place(x=222.32, y=210)

Equals_Button = customtkinter.CTkButton(frame, command=equal_button, text='=', width=140, height=50, font=('Robobto', 28))
Equals_Button.place(x=330, y=260)

Clear_Button = customtkinter.CTkButton(frame, command=clear_button, text='Clear', width=140, height=50, font=('Roboto',28))
Clear_Button.place(x=330, y=310)

scrollable_frame = customtkinter.CTkScrollableFrame(frame, width=297, height=20)
scrollable_frame.place(x=10, y=261)

#Example for showing history of equations

root.mainloop()