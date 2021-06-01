# Thank you Dev Ed!! you are a God
# https://www.youtube.com/watch?v=jE-SpRI3K5g

import tkinter as tk
from tkinter import filedialog, Text
import os

# The main (or 'root' haha) "window"
root = tk.Tk(className=' Video Downloader :)')

root.configure(bg='#ffa31a')
root.geometry=('200x400')
root.pack_propagate(0)

'''def displayApps():
    for app in apps:
        label = tk.Label(frame, text=app, bg='white')
        label.pack()'''

def useLink():
    dir = filedialog.askdirectory()
    print(dir)

    link = linkEntry.get()
    with open('temp.bat', 'w+') as bat:
        bat.write('youtube-dl.exe '+ '-f best ' + '-o "' +dir + '/%%(title)s-%%(id)s.%%(ext)s" ' + link)
        bat.write('\nPAUSE')
        bat.close()
    os.startfile('temp.bat')

backgroundColour = '#ffa31a'

title = tk.Label(root, text="Cool Video Downloader", bg=backgroundColour)
title.pack()

frame = tk.Frame(root, bg='black')
frame.place(relwidth=0.8, relheigh=0.8, relx= 0.1, rely=0.15 )

# Link entry textbox
linkEntry = tk.Entry(frame)
linkEntry.pack()

# Creating buttons
download = tk.Button(frame, text='Download!', padx=10, pady=5, fg='black', bg=backgroundColour, command=useLink)
download.pack()

#directory = tk.Button(frame, text="Change Directory", padx=10, pady=5, fg='black', bg=backgroundColour, command=changeDir)
# directory.pack()
# Creating buttons
# runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg='black', bg=backgroundColour, command=runApps)
# runApps.pack()

# Execute the app
root.protocol("WM_DELETE_WINDOW", root.iconify())
root.mainloop()
