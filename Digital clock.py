import tkinter as tk
from time import strftime
# Function to fetch current time and update the label
def time():
    current_time = strftime('%H:%M:%S %p')  # Fetch current time in desired format
    label.config(text=current_time)         # Update label with current time
    label.after(1000, time)                 # Call the time function every 1000ms (1 second)

# Create main application window
root = tk.Tk()
root.title('Digital Clock')

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call the time function to update the label initially
time()

# Run the main loop
root.mainloop()