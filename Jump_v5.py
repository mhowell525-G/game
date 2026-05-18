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
        self.square = canvas.create_rectangle(300, 340, 340, 400, fill="red")
        
        self.y_velocity = 0
        self.x_velocity = 0
        self.gravity = 0.5
        self.jump_velocity = -10
        self.on_ground = False
        
        
        
    
        
        self.y = 0
        self.canvas.move(self.id, 245, 100) 
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = True
        self.canvas.bind_all('<KeyPress-w>', self.jump)
        self.canvas.bind_all('<KeyPress-a>', self.left)
        self.canvas.bind_all('<KeyRelease-a>', self.release) 
        self.canvas.bind_all('<KeyPress-d>', self.right)
        self.canvas.bind_all('<KeyRelease-d>', self.release) 
        
        self.update()
    
    def update(self):
        self.y_velocity += self.gravity
        
        self.canvas.move(self.id, self.x_velocity, self.y_velocity)
        
        
        pos = self.canvas.coords(self.id)
        
        # ground collision
        if pos[3] >= self.canvas_height:
            self.canvas.move(self.id, self.x_velocity, self.canvas_height - pos[3])
            self.y_velocity = 0
            self.on_ground = True
        else:
            self.on_ground = False
        
        overlapping_items = self.canvas.find_overlapping(pos[0], pos[1], pos[2], pos[3])
        
        if self.square in overlapping_items:
            print(f"Game Over")
            self.canvas.coords(self.id, 245, 100, 260, 115)
            self.y_velocity = 0
            square_pos = self.canvas.coords(self.square)
        
            if self.y_velocity > 0:
               self.canvas.move(self.id, 0, square_pos[1] - pos [3])
               self.y_velocity = 0
               self.on_ground = True
                
        
        
        #self.x_velocity = 0
        self.canvas.after(20, self.update)
        
        
        
    
    def jump(self, evt):
        
        if self.on_ground:
        
            self.y_velocity = self.jump_velocity
            self.on_ground = False
            
            
    def left(self, evt):
        if self.x_velocity > -10:
            self.x_velocity -= 5
    
    def right(self, evt):
        if self.x_velocity < 10:
            self.x_velocity += 5

    def release(self, evt):
        self.x_velocity = 0 #to make the ball stop (left/right)



    
        
    

root = Tk()
menu = GameMenu(root)
root.mainloop()