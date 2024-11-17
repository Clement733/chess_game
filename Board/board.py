from tkinter import ttk
import tkinter as tk
import GUI.Interface as gu

def bd():
    gu.pl_but.config(state="disable")
    gu.plcomp_but.config(state="disable")

    bd = tk.Toplevel()
    """bd.geometry("1150x850")"""
    bd.title("This is my try at a board window")

    bd_canvas = tk.Canvas(bd, borderwidth=1, width=800, height=100)
    bd_canvas.grid(row=1,
                   sticky="nsew",
                   columnspan=8,
                   rowspan=8)

    x=100
    y=100
    i = 0


    a1 = bd_canvas.create_rectangle(0, 0, x, y, fill='black')
    a2 = bd_canvas.create_rectangle(100, 0, 200, y, fill='white')
    a3 = bd_canvas.create_rectangle(200, 0, 300, y, fill='black')
    a4 = bd_canvas.create_rectangle(300, 0, 400, y, fill='white')
    a5 = bd_canvas.create_rectangle(400, 0, 500, y, fill='black')
    a6 = bd_canvas.create_rectangle(500, 0, 600, y, fill='white')
    a7 = bd_canvas.create_rectangle(600, 0, 700, y, fill='black')
    a8 = bd_canvas.create_rectangle(700, 0, 800, y, fill='white')


    def on_close():
        gu.pl_but.config(state="active")
        bd.destroy()

        gu.plcomp_but.config(state="active")
        bd.destroy()

    bd.protocol("WM_DELETE_WINDOW", on_close)
