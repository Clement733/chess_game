import tkinter as tk
from Board.board import bd

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
                      width=55,
                      bd=4,
                      font=("TimesNewRoman", 32, "bold"),
                      textvariable=pl_hdr)

pl_hdr_txt.grid(columnspan=2)

pl_but=tk.Button(g_w,
                 anchor="sw",
                 background="blue",
                 foreground="white",
                 relief="groove",
                 height=3,
                 width=20,
                 font=("TimesNewRoman", 16, "bold", "italic"),
                 textvariable=players_but_txt,
                 justify="center",
                 command=bd)

pl_but.grid(row=5,
            column=0)

plcomp_but=tk.Button(g_w,
                     anchor="se",
                     background="blue",
                     foreground="white",
                     relief="groove",
                     height=3,
                     width=20,
                     font=("TimesNewRoman", 16, "bold", "italic"),
                     textvariable=plcomp_but_txt,
                     justify="center",
                     command=bd)

plcomp_but.grid(row=5,
                column=1,
                sticky="sw")

g_w.mainloop()
