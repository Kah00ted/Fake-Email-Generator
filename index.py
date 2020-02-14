# import stuff here
try:
    import Tkinter as tk
    from Tkinter import *
except:
    import tkinter as tk
    from tkinter import *


# Create Instances
win = tk.Tk()

# -----Functions------
def joinClick():
    subject=gmailSubject.get()
    message=gmailMessage.get()
    fromT=gmailFrom.get()
    time=gmailTime.get()

    SubjectIs = tk.Label(gmailFrame, text=subject, bg="#ffffff", fg="#202124", font="roboto 14")
    SubjectIs.place(x=75, y=175)

    whoFromIs = tk.Label(gmailFrame, text=fromT, bg="#ffffff", fg="#202124", font="none 11 bold")
    whoFromIs.place(x=102, y=215)

    timeIs = tk.Label(gmailFrame, text=time, bg="#ffffff", fg="#5f6368", font="none 10")
    timeIs.place(x=780, y=217)

    messageIs = tk.Label(gmailFrame, text=message, bg="#ffffff", fg="#222222", font="Areil 10")
    messageIs.place(x=102, y=250)


# Set window title
win.title("Fake Email Creator")

# makes window non resizable
win.resizable(False, False)

#set background color
win.configure(bg="#ffffff")

# Set background canvas
canvas = tk.Canvas(win, height=563, width=1250, bg="#f5f5f5", highlightthickness=0)
canvas.pack()

# -----Frames------
# Frame for main gmail preview window
gmailFrame = tk.Frame(win, bg="#ffffff", highlightthickness=0)
gmailFrame.place(x=250, y=0, width=1000, height=563)

inputFrame = tk.Frame(win, bg="#f5f5f5", highlightthickness=0)
inputFrame.place(x=0, y=0, width=250, height=563)


# template:  tk.[widget name](rootwindow, proprities)

# -----Widgets------

# Adds gmail preview to GUI
gmailPhoto = tk.PhotoImage(file="images/gmailWindowSmall.gif")
smallGmailPic = tk.Label(gmailFrame, image=gmailPhoto)
smallGmailPic.pack()

# Defaults
SubjectIs = tk.Label(gmailFrame, text="subject:", bg="#ffffff", fg="#202124", font="roboto 14")
SubjectIs.place(x=75, y=175)

whoFromIs = tk.Label(gmailFrame, text="From:", bg="#ffffff", fg="#202124", font="none 11 bold")
whoFromIs.place(x=102, y=215)

timeIs = tk.Label(gmailFrame, text="Feb 7, 2020, 1:09 PM", bg="#ffffff", fg="#5f6368", font="none 10")
timeIs.place(x=780, y=217)

messageIs = tk.Label(gmailFrame, text="Message:", bg="#ffffff", fg="#222222", font="Areil 10")
messageIs.place(x=102, y=250)

# Adds gmail inputs to GUI
gmailSubjectIndicator = tk.Label(inputFrame, text="Subject:", bg="#f5f5f5", fg="black", font="none 15")
gmailSubjectIndicator.place(x=0, y=10)

gmailSubject = tk.Entry(inputFrame, width=20, bg="#ffffff", highlightthickness=0, borderwidth=3)
gmailSubject.place(x=10, y=30)

gmailMessageIndicator = tk.Label(inputFrame, text="Message:", bg="#f5f5f5", fg="black", font="none 15")
gmailMessageIndicator.place(x=0, y=60)

gmailMessage = tk.Entry(inputFrame, width=20, bg="#ffffff", highlightthickness=0, borderwidth=3)
gmailMessage.place(x=10, y=80)

gmailFromIndicator = tk.Label(inputFrame, text="From:", bg="#f5f5f5", fg="black", font="none 15")
gmailFromIndicator.place(x=0, y=110)

gmailFrom = tk.Entry(inputFrame, width=20, bg="#ffffff", highlightthickness=0, borderwidth=3)
gmailFrom.place(x=10, y=130)

gmailTimeIndicator = tk.Label(inputFrame, text="Time:", bg="#f5f5f5", fg="black", font="none 15")
gmailTimeIndicator.place(x=0, y=160)

timeExample = tk.Label(inputFrame, text="(example: Feb 7, 2020, 1:09 PM)", bg="#f5f5f5", fg="black", font="none 9")
timeExample.place(x=40, y=165)

gmailTime = tk.Entry(inputFrame, width=20, bg="#ffffff", highlightthickness=0, borderwidth=3)
gmailTime.place(x=10, y=180)


button = tk.Button(inputFrame, text="Generate Email", width=14, highlightbackground="#f5f5f5", command=joinClick)
button.place(x=10, y=210)

# start GUI/Start the main loop
win.mainloop()