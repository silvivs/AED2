import turtle as t
import tkinter as tk
from tkinter import simpledialog

def posCaneta(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()

def setup():
    t.hideturtle()
    t.speed(0)
    t.pensize(1)
    posCaneta(0, 200)

def curvaSnowflake(nivel, tamLado):
    tamSegmento = tamLado / 3
    
    if nivel == 1:
        t.forward(tamSegmento)
    else:
        curvaSnowflake(nivel - 1, tamSegmento)
        t.left(60)
        curvaSnowflake(nivel - 1, tamSegmento)
        t.right(120)
        curvaSnowflake(nivel - 1, tamSegmento)
        t.left(60)
        curvaSnowflake(nivel - 1, tamSegmento)

def main():
    root = tk.Tk()
    root.withdraw()

    nivel = simpledialog.askinteger("Niveis", "Digite a quantidade de niveis:")
    tamCurva = simpledialog.askinteger("Tamanho da curva", "Digite o tamanho da curva:")

    root.destroy()

    setup()

    angulos = [60, 120, 120]

    for angulo in angulos:
        t.right(angulo)
        curvaSnowflake(nivel, tamCurva)

    t.mainloop()

if __name__ == "__main__":
    main()
