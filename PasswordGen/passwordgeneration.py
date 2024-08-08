from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("600x600")
root.resizable(0, 0)
root.title("PASSWORD GENERATOR")

Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(root, text='AmenAllahMelki', font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold')
pass_label.pack()

pass_len = IntVar()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15)
length.pack()

pass_str = StringVar()

def Generator():
    password = []
    # Create a base password with at least one of each type
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))
    
    # Fill the rest of the password
    for _ in range(pass_len.get() - 4):
        password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))

    # Shuffle the list to make it more random and convert back to string
    random.shuffle(password)
    final_password = ''.join(password)
    pass_str.set(final_password)

Button(root, text="GENERATE PASSWORD", command=Generator).pack(pady=5)

Entry(root, textvariable=pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)

root.mainloop()
