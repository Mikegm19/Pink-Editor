import sys
from tkinter import Tk, Text, Button, Menubutton, Menu, IntVar, PhotoImage
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk  # Import ttk for themed widgets

# Create the main window
root = Tk()
root.title("Pink Editor")
root.config(background="green")
root.geometry("600x400")  # Set window size

# Create a Text widget
text = Text(root, font=("Courier", 12))
text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Configure grid weights for resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

try:
    # Load icon (ensure 'pinklog.png' is in the same directory)
    icon = PhotoImage(file="pinklog.png")
    root.iconphoto(True, icon)
except Exception as e:
    print(f"Error loading icon: {e}")

def saveas():
    try:
        # Get the text from the Text widget
        t = text.get("1.0", "end-1c")
        # Open a save file dialog
        savelocation = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if savelocation:  # Only proceed if a file was selected
            with open(savelocation, "w") as file1:
                file1.write(t)
            messagebox.showinfo("Success", "File saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

def FontHelvetica():
    root.config(background="blue")
    text.config(font=("Helvetica", 12))

def FontCourier():
    text.config(font=("Courier", 12))

# Create a style for ttk buttons
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=10)
style.configure("TMenubutton", font=("Helvetica", 10), padding=10)

# Hover effect functions
def on_enter_save(e):
    save_button.state(['active'])  # Simulate active state on hover
def on_leave_save(e):
    save_button.state(['!active'])  # Revert to normal state

def on_enter_font(e):
    font_button.state(['active'])
def on_leave_font(e):
    font_button.state(['!active'])

# Create a Save button (using ttk.Button)
save_button = ttk.Button(root, text="Save", command=saveas)
save_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")
save_button.bind("<Enter>", on_enter_save)  # Bind hover effect
save_button.bind("<Leave>", on_leave_save)

# Create a Font Menubutton (using ttk.Menubutton)
font_button = ttk.Menubutton(root, text="Font")
font_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")
font_button.menu = Menu(font_button, tearoff=0, font=("Helvetica", 10))
font_button["menu"] = font_button.menu

# Use Radiobutton for mutually exclusive font selection
font_var = IntVar(value=0)  # Default to no font selected
font_button.menu.add_radiobutton(label="Courier", variable=font_var, value=1, command=FontCourier)
font_button.menu.add_radiobutton(label="Helvetica", variable=font_var, value=2, command=FontHelvetica)

# Bind hover effects for Font button
font_button.bind("<Enter>", on_enter_font)
font_button.bind("<Leave>", on_leave_font)

# Start the main loop
root.mainloop()
