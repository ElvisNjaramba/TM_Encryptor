from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
import os
from cryptography.fernet import Fernet

# Create an instance of tkinter frame or window
win = Tk()

# Set the geometry of tkinter frame
win.geometry("700x350")
win.title("@Tariq Marcel")
bgimg= PhotoImage(file = "hacker-25938.png")
win.iconphoto(True, bgimg)
win.configure(bg='black')

def open_file():
    global file1
    file1 = fd.askopenfilenames(parent=win, title='Choose a File')
    print(win.splitlist(file1))

# Add a Label widget
label = Label(win, text="This is an encryption decryption program which one can use to encrypt any type of file.", font=('Aerial 11'))
label.pack(pady=30)
label1 =Label(win, text=" One can only decrypt the files with the key generated and also the pass phrase set.", pady=5).pack()
# Add a Button Widget
ttk.Button(win, text="Select a File", command=open_file).pack()

def encryptor():
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)
        for file in file1:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_encrypted)

    print("YOUR FILES HAVE BEEN ENCRYPTED")

ttk.Button(win, text="Encrypt", command=encryptor).pack()

def decryptor():
    secret_phrase = "Tariq"
    user_phrase = input("ENTER KEY TO DECRYPT: ")
    if secret_phrase == user_phrase:
            with open("thekey.key", "rb") as key:
                secretkey = key.read()
            for file in file1:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, "wb") as thefile:
                    thefile.write(contents_decrypted)

            print("YOUR FILES HAVE BEEN DECRYPTED")
ttk.Button(win, text="Decrypt", command=decryptor).pack()


exit_button = Button(win, text="Exit", command=win.destroy)
exit_button.pack(pady=20)

win.mainloop()