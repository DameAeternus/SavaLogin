import tkinter as tk
from PIL import Image, ImageTk

def show_password():
    if show_password_var.get():
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

root = tk.Tk()
root.title("Login Form")
root.geometry("1280x768+150+50")

# Initialize the Tkinter variable for the checkbox
show_password_var = tk.BooleanVar()
show_password_var.set(False)  # Set it to unchecked by default

# Load the background image
background_image = Image.open("background.jpg")

# Create the Tkinter image variable
background_photo = ImageTk.PhotoImage(background_image)

# Create the background label with the image
background_label = tk.Label(root, image=background_photo)
background_label.pack(fill="both", expand=True)

# Username Label and Entry
username_label = tk.Label(root, text="Username:", font=("Arial", 12))
username_label.config(borderwidth=0, highlightthickness=0)
username_label.place(relx=0.3, rely=0.4)
username_entry = tk.Entry(root)
username_entry.place(relx=0.45, rely=0.4)

# Password Checkbutton
password_checkbutton = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=show_password, font=("Arial", 12))
password_checkbutton.pack()
# Password Label and Entry
password_label = tk.Label(root, text="Password:", font=("Arial", 12))
password_label.place(relx=0.3, rely=0.5)
password_entry = tk.Entry(root, show='*')
password_entry.place(relx=0.45, rely=0.5)
password_checkbutton.place(relx=0.45, rely=0.6)

button= tk.Button(root,text="Log in")
button.place(relx=0.35,rely=0.605)
# Function to resize the background image
def resize_image(e):
    bg_width = e.width
    bg_height = e.height
    resized_image = background_image.resize((bg_width, bg_height))
    new_photo = ImageTk.PhotoImage(resized_image)
    background_label.config(image=new_photo)
    background_label.image = new_photo

root.bind("<Configure>", resize_image)
root.mainloop()