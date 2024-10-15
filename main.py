import minecraft_launcher_lib
import subprocess
from tkinter import *
import time

root = Tk()

root['bg'] = "#fafafa"
root.title("CharaLauncher")
root.geometry('250x250')

root.resizable(width=False, height=False)

canvas = canvas = Canvas(root, height=250, width=250)
canvas.pack()

vis1=PhotoImage(file='CharaLauncherLogo.png')
vis1L=Label(canvas)
vis1L.image=vis1
vis1L['image']=vis1L.image
vis1L.place(relwidth=1, relheight=1)

#title = Label(vis1L, text="CharaLauncher", bg="white", font=40)
#title.pack()

def download():
    us = NickInput.get()

    options = {
        'username': us
    }
    version_id = VersInput.get()
    subprocess.call(minecraft_launcher_lib.install.install_minecraft_version(version_id, minecraft_directory='.launcher'))

def zapusk():
    us = NickInput.get()
    if us == "":
        Error = Label(vis1L, text="Введите ник", bg="red", font=40)
        Error.place(x=90, y=120)
    options = {
        'username': us
    }
    version_id = VersInput.get()
    if version_id == "":
        Error2 = Label(vis1L, text="Введите версию", bg="red", font=40)
        Error2.place(x=70, y=180)
    if version_id!="" and us!="":
        subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version_id, minecraft_directory='.launcher', options=options))
btn = Button(vis1L, text="Скачать", bg="gray",command=download)
btn.place(x=102, y=60)

btn2 = Button(vis1L, text="Запуск", bg="gray",command=zapusk)
btn2.place(x=105, y=90)

title1 = Label(vis1L, text="Ник:", bg="white", font=40)
title1.place(x=110, y=120)

NickInput = Entry(vis1L, bg="white")
NickInput.place(x=70, y=150)

title2 = Label(vis1L, text="Версия:", bg="white", font=40)
title2.place(x=100, y=180)

VersInput = Entry(vis1L, bg="white")
VersInput.place(x=70, y=210)

root.mainloop()