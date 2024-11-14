import tkinter as tk

g_w = tk.Tk()
g_w.geometry("1080x680")
g_w.title("Welcome to my chess game!♟️")

pl_but = tk.StringVar()
pl_but.set("Let's play some chess, baby!")

pl_but_txt = tk.Label(g_w,
                      anchor='n',
                      background="black",
                      foreground="green",
                      justify="center",
                      relief="raised",
                      height=1,
                      width=60,
                      bd=4,
                      font=("TimesNewRoman", 32, "bold"),
                      textvariable=pl_but)

pl_but_txt.pack()
g_w.mainloop()
