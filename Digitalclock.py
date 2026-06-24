# Digital Clock using Tkinter
# This project creates a GUI-based digital clock that displays
# the current time and date and updates every second.

import tkinter as tk
from time import strftime

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")

# Function to get and display the current time and date
def time():
    # %H = Hour (24-hour format)
    # %M = Minutes
    # %S = Seconds
    # %p = AM/PM
    # %D = Date (MM/DD/YY)
    string = strftime("%H:%M:%S %p \n %D")

    # Update the label with the current time and date
    Label.config(text=string)

    # Call the function again after 1000 milliseconds (1 second)
    Label.after(1000, time)

# Create a label widget to display the clock
Label = tk.Label(
    root,
    font=('calibri', 50, 'bold'),
    background='yellow',
    foreground='black'
)

# Place the label at the center of the window
Label.pack(anchor='center')

# Start updating the clock
time()

# Run the Tkinter event loop
root.mainloop()
                      
