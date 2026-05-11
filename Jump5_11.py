from tkinter import *
import random
import time

game_title = "Jump"

class GameMenu(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title(game_title)
        self.master.geometry("400x400")
        self.pack(fill="both", expand=True)
        
        self.create_widgets()

    def create_widgets(self):
    
        self.title_label = Label(self, text=game_title, font=("Helvectia", 24, "bold"))
        self.title_label.pack(pady= 40)
        
        self.start_button = Button(self, text="Play", width=20, command=self.start_game)
        self.start_button.pack(pady= 10)
        
        self.start_button = Button(self, text="Quit", width=20, command=quit)
        self.start_button.pack(pady= 10)
        
    def start_game(self):
        
        tk = Tk()
        tk.title("Jump")
        tk.resizable(0, 0)
        tk.wm_attributes("-topmost", 1)
        canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
        canvas.pack()
        tk.update()
        Player(canvas, "blue")
        
        
class Player:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.y = 0
        self.canvas.move(self.id, 245, 100) 
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = True
        self.canvas.bind_all('<KeyPress-w>', self.jump)
        
    
    def draw(self):
        self.canvas.move(self.id, self.y, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <=0:
            self.y = 0
        elif pos [2] >= self.canvas_height:
            self.y = 0
    
    def jump(self, evt):
        self.y = +5
        self.draw()

    
        
    

root = Tk()
menu = GameMenu(root)
root.mainloop()