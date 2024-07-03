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
CalculationFieldTextBox = customtkinter.CTkTextbox(frame, height=50, width=460, font=("Roboto",26))
CalculationFieldTextBox.pack(fill="both", expand=True)
CalculationFieldTextBox.place(x=10, y=10)
CalculationFieldTextBox.insert('0.0', 'new text to insert')  # insert at line 0 character 0
text = CalculationFieldTextBox.get('0.0', 'end')  # get text from line 0 character 0 till the end
CalculationFieldTextBox.delete('0.0', 'end')  # delete all text
CalculationFieldTextBox.configure(state='normal')  # configure textbox to be read-only

root.mainloop()
