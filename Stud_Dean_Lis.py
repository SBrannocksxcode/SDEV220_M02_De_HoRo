# Author: [Steven Brannock]
# File Name: student_awards.py
# Description: This Python app accepts student names and GPAs, checks if they qualify for the Dean's List or Honor Roll, and prints corresponding messages.

# Import the tkinter module to create GUI
import tkinter as tk
# Import the messagebox module for displaying messages
from tkinter import messagebox

class StudentAwardsApp:
    def __init__(self, master):
        # Initialize the GUI window
        self.master = master
        master.title("Student Awards Program")

        # Create labels for input fields
        self.label_last_name = tk.Label(master, text="Last Name:")
        self.label_last_name.grid(row=0, column=0, padx=10, pady=5)
        self.last_name_entry = tk.Entry(master)
        self.last_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.label_first_name = tk.Label(master, text="First Name:")
        self.label_first_name.grid(row=1, column=0, padx=10, pady=5)
        self.first_name_entry = tk.Entry(master)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.label_gpa = tk.Label(master, text="GPA:")
        self.label_gpa.grid(row=2, column=0, padx=10, pady=5)
        self.gpa_entry = tk.Entry(master)
        self.gpa_entry.grid(row=2, column=1, padx=10, pady=5)

        # Create a submit button to process the entered data
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_record)
        self.submit_button.grid(row=3, columnspan=2, padx=10, pady=10)

    def submit_record(self):
        # Get the input values from the user
        last_name = self.last_name_entry.get()
        # Close the window if 'ZZZ' is entered as the last name
        if last_name == 'ZZZ':
            self.master.destroy()  
        first_name = self.first_name_entry.get()
        gpa = float(self.gpa_entry.get())

        # Check if the GPA qualifies for an award and display a message accordingly
        if gpa >= 3.5:
            messagebox.showinfo("Dean's List", f"{first_name} {last_name} made the Dean's List!")
        elif gpa >= 3.25:
            messagebox.showinfo("Honor Roll", f"{first_name} {last_name} made the Honor Roll!")
        else:
            messagebox.showinfo("No Award", f"{first_name} {last_name} did not qualify for any award.")

def main():
    # Create the main window for the GUI
    root = tk.Tk()
    # Instantiate the StudentAwardsApp class
    app = StudentAwardsApp(root)
    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()