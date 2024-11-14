import tkinter as tk

g_w = tk.Tk()
g_w.geometry("1080x680")
g_w.title("Welcome to my chess game!♟️")

pl_hdr = tk.StringVar()
pl_hdr.set("Let's play some chess, baby!")
players_but_txt = tk.StringVar()
players_but_txt.set('PLAY 1 vs 1')
plcomp_but_txt = tk.StringVar()
plcomp_but_txt.set('PLAY 1 vs COMPUTER')

pl_hdr_txt = tk.Label(g_w,
                      background="black",
                      foreground="green",
                      relief="raised",
                      height=1,
                      width=60,
                      bd=4,
                      font=("TimesNewRoman", 32, "bold"),
                      textvariable=pl_hdr)

pl_hdr_txt.pack()

pl_but=tk.Button(g_w,
                 anchor="sw",
                 background="blue",
                 foreground="white",
                 relief="groove",
                 height=3,
                 width=20,
                 font=("TimesNewRoman", 16, "bold", "italic"),
                 textvariable=players_but_txt,
                 justify="center")

pl_but.pack()

plcomp_but=tk.Button(g_w,
                     anchor="se",
                     background="blue",
                     foreground="white",
                     relief="groove",
                     height=3,
                     width=20,
                     font=("TimesNewRoman", 16, "bold", "italic"),
                     textvariable=plcomp_but_txt,
                     justify="center")

plcomp_but.pack(anchor="s")

g_w.mainloop()
