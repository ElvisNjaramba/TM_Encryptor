import tkinter as Tk
import tkinter.filedialog as fd
from PIL import ImageTk
import os
from cryptography.fernet import Fernet
import os
import speech_recognition as sr
import pyttsx3

win= Tk.Tk()
win.geometry("650x300")
win.title("Tm_encryptor")
r = sr.Recognizer()

lbl = Tk.Label(win, text='welcome to Tmspace').pack()


def openNewWindow():
    new= Tk.Toplevel(win)
    new.geometry("650x300")
    new.title("@TM Encryptor")
    new.configure(bg="black")

    new.wm_transient(win)


    def open_file():
        global file1
        file1 = fd.askopenfilenames(parent=new, title='Choose a File')
        label1 = Tk.Label(new, text=file1).pack(pady=20)


    menubar = Tk.Menu(new)
    new.config(menu=menubar)
    file_menu = Tk.Menu(menubar)

    # add a menu item to the menu
    file_menu.add_command(
        label='open file',
        command=open_file
    )

    file_menu.add_command(
        label='Exit',
        command=win.destroy
    )

    # add the File menu to the menubar
    menubar.add_cascade(
        label="Menu",
        menu=file_menu
    )

    # Add a Label widget
    label = Tk.Label(new, text="This is an encryption decryption program which one can use to encrypt any type of file.",
                  font=('Aerial 11')).pack(pady=30)

    def encryptor():
        try:
            key = Fernet.generate_key()
            with open("thekey.key", "wb") as thekey:
                thekey.write(key)
            for file in file1:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_encrypted = Fernet(key).encrypt(contents)
                with open(file, "wb") as thefile:
                    thefile.write(contents_encrypted)
            label2 = Tk.Label(new,
                           text="Your files have been encrypted!!").pack()

        except:
            label9 = Tk.Label(new, text="An Error Occured.").pack()

    Tk.Button(new, text="Encrypt", command=encryptor).pack()

    def decryptor():
        try:
            with open("thekey.key", "rb") as key:
                secretkey = key.read()
            for file in file1:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, "wb") as thefile:
                    thefile.write(contents_decrypted)

            label3 = Tk.Label(new, text="YOUR FILES HAVE BEEN DECRYPTED").pack()

        except:
            label4 = Tk.Label(new, text="An error occured").pack()

    quit = Tk.Button(new, text="Decrypt", command=decryptor).pack()

def open():
    openNewWindow()

submit1= Tk.Button(win, text="open", command=open).pack()

win.mainloop()

