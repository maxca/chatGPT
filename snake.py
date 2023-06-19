import tkinter as tk
import random

# Constants
GRID_SIZE = 20
GRID_WIDTH = 40
GRID_HEIGHT = 30
MOVE_INTERVAL = 200

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")

        self.canvas = tk.Canvas(master, width=GRID_WIDTH*GRID_SIZE, height=GRID_HEIGHT*GRID_SIZE)
        self.canvas.pack()

        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = "Right"
        self.food = self.generate_food()

        self.canvas.bind_all("<Key>", self.handle_keypress)

        self.move_snake()

    def generate_food(self):
        while True:
            x = random.randint(0, GRID_WIDTH-1)
            y = random.randint(0, GRID_HEIGHT-1)
            if (x, y) not in self.snake:
                return (x, y)

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Right":
            new_head = (head_x + 1, head_y)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)

        if (
            new_head[0] < 0 or
            new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or
            new_head[1] >= GRID_HEIGHT or
            new_head in self.snake[1:]
        ):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop()

        self.draw()

        self.master.after(MOVE_INTERVAL, self.move_snake)

    def draw(self):
        self.canvas.delete(tk.ALL)

        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(
                x * GRID_SIZE, y * GRID_SIZE,
                (x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE,
                fill="green"
            )

        food_x, food_y = self.food
        self.canvas.create_oval(
            food_x * GRID_SIZE, food_y * GRID_SIZE,
            (food_x + 1) * GRID_SIZE, (food_y + 1) * GRID_SIZE,
            fill="red"
        )

    def handle_keypress(self, event):
        if event.keysym == "Right" and self.direction != "Left":
            self.direction = "Right"
        elif event.keysym == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif event.keysym == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif event.keysym == "Down" and self.direction != "Up":
            self.direction = "Down"

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(
            GRID_WIDTH * GRID_SIZE / 2, GRID_HEIGHT * GRID_SIZE / 2,
            text="Game Over!", font=("Helvetica", 24), fill="red"
        )

# Create the tkinter window
window = tk.Tk()

# Create an instance of the SnakeGame class
game = SnakeGame(window)

# Run the tkinter event loop
window.mainloop()
