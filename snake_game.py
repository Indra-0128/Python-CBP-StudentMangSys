import tkinter as tk
import random

WIDTH = 600
HEIGHT = 500
CELL = 20

COLS = WIDTH // CELL
ROWS = (HEIGHT - 60) // CELL


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake Game")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                                bg="#0f172a", highlightthickness=0)
        self.canvas.pack()

        self.reset()

        root.bind("<Up>", lambda e: self.set_dir(0, -1))
        root.bind("<Down>", lambda e: self.set_dir(0, 1))
        root.bind("<Left>", lambda e: self.set_dir(-1, 0))
        root.bind("<Right>", lambda e: self.set_dir(1, 0))
        root.bind("<space>", lambda e: self.toggle_pause())

        root.bind("<r>", lambda e: self.reset())
        root.bind("<R>", lambda e: self.reset())

        self.loop()

    def reset(self):
        self.snake = [(10, 10)]
        self.dir = (1, 0)
        self.food = self.spawn_food()
        self.score = 0
        self.running = True
        self.paused = False

        self.base_speed = 140  # slow start

    def spawn_food(self):
        while True:
            f = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            if f not in self.snake:
                return f

    def set_dir(self, dx, dy):
        if (-dx, -dy) != self.dir:
            self.dir = (dx, dy)

    def toggle_pause(self):
        self.paused = not self.paused

    # ⭐ SPEED CONTROL LOGIC
    def get_speed(self):
        if self.score < 30:
            return 140   # slow
        elif self.score < 80:
            return 100   # medium
        elif self.score < 150:
            return 80    # fast
        else:
            return 60    # very fast (max difficulty)

    def update(self):
        if not self.running or self.paused:
            return

        head = self.snake[0]
        new = (head[0] + self.dir[0], head[1] + self.dir[1])

        if (new[0] < 0 or new[0] >= COLS or
            new[1] < 0 or new[1] >= ROWS or
            new in self.snake):
            self.running = False
            return

        self.snake.insert(0, new)

        if new == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def draw_snake(self):
        for i, (x, y) in enumerate(self.snake):
            x1 = x * CELL + 3
            y1 = y * CELL + 60 + 3
            x2 = (x + 1) * CELL - 3
            y2 = (y + 1) * CELL + 60 - 3

            if i == 0:
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="#22c55e", outline="")

                # eyes
                self.canvas.create_rectangle(x1+5, y1+5, x1+9, y1+9, fill="white")
                self.canvas.create_rectangle(x2-9, y1+5, x2-5, y1+9, fill="white")
            else:
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="#4ade80", outline="")

    def draw_food(self):
        x, y = self.food
        x1 = x * CELL + 4
        y1 = y * CELL + 60 + 4
        x2 = (x + 1) * CELL - 4
        y2 = (y + 1) * CELL + 60 - 4

        self.canvas.create_oval(x1, y1, x2, y2, fill="#ef4444", outline="")

    def draw(self):
        self.canvas.delete("all")

        # Header
        self.canvas.create_rectangle(0, 0, WIDTH, 60, fill="#1e293b", outline="")
        self.canvas.create_text(20, 30, text="🐍 Snake Game", fill="white",
                                anchor="w", font=("Segoe UI", 18, "bold"))

        self.canvas.create_text(WIDTH-20, 30,
                                text=f"Score: {self.score}",
                                fill="#38bdf8",
                                anchor="e",
                                font=("Segoe UI", 16, "bold"))

        # Speed indicator
        speed = self.get_speed()
        self.canvas.create_text(WIDTH//2, 30,
                                text=f"Speed: {speed}ms",
                                fill="#facc15",
                                font=("Segoe UI", 12, "bold"))

        self.draw_food()
        self.draw_snake()

        if self.paused:
            self.canvas.create_text(WIDTH//2, HEIGHT//2,
                                    text="PAUSED",
                                    fill="yellow",
                                    font=("Segoe UI", 28, "bold"))

        if not self.running:
            self.canvas.create_text(WIDTH//2, HEIGHT//2,
                                    text="GAME OVER\nPress R",
                                    fill="#f87171",
                                    font=("Segoe UI", 26, "bold"))

    def loop(self):
        self.update()
        self.draw()

        # ⭐ dynamic speed applied here
        self.root.after(self.get_speed(), self.loop)


root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
