import customtkinter

#Sets base appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#creates root & adds root to frame
root = customtkinter.CTk()
root.geometry("500x400")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)
root.resizable(False,False)

#Creates the text box to input values
entry = customtkinter.CTkEntry(frame, placeholder_text='', width=460, height=50, font=("Roboto",26))
entry.place(x=10, y=10)

#Creates the function for buttons
def division_func():
        box_content = entry.get()
        if box_content and box_content[-1].isdigit():
            entry.insert(customtkinter.END,chr(247))
        #entry.insert(root.END," "+chr(247)+" ")

def multiplication_button():
    box_content = entry.get()
    for index, char in enumerate(box_content):
        if char.isdigit():
            entry.insert(index+1," "+"×"+" ")
            break
    else:
        entry.insert(1," "+"×"+" ")

def subtraction_button():
    entry.insert(-1," "+"-"+" ")

def addition_button():
    entry.insert(-1," "+"+"+" ")

#Creates Division Button
Division_Button = customtkinter.CTkButton(frame, command=division_func,text="÷", width=140, height=50, font=("Roboto", 26))
Division_Button.place(x=330, y=60)

#Creates Multiplication Button
Multiplication_Button = customtkinter.CTkButton(frame, command=multiplication_button, text="×", width=140, height=50, font=("Roboto", 26))
Multiplication_Button.place(x=330, y=110)

#Creates Subtraction Button
Subtraction_Button = customtkinter.CTkButton(frame, command=subtraction_button, text='-', width=140, height=50, font=("Roboto", 26))
Subtraction_Button.place(x=330, y=160)

#Creates Addition Button
Addition_Button = customtkinter.CTkButton(frame, command=addition_button, text='+', width=140, height=50, font=("Roboto", 26))
Addition_Button.place(x=330, y=210)

root.mainloop()