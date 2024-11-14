from tkinter import ttk
import tkinter as tk
import GUI.Interface as gu

def bd():
    gu.pl_but.config(state="disable")
    gu.plcomp_but.config(state="disable")

    bd = tk.Toplevel(gu.g_w)
    bd.grid()
    bd.geometry("1150x850")
    bd.title("This is my try at a board window")

    def on_close():
        gu.pl_but.config(state="active")
        bd.destroy()

        gu.plcomp_but.config(state="active")
        bd.destroy()

    bd.protocol("WM_DELETE_WINDOW", on_close)
