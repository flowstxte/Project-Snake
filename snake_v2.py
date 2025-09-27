from tkinter import *
import random

# Game constants
GAME_WIDTH = 600
GAME_HEIGHT = 600
SPACE_SIZE = 20
BODY_PARTS = 4
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

class SnakeGame:
    def __init__(self, window):
        self.window = window
        self.window.title("Snake Game")
        self.window.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        # Game state variables
        self.score = 0
        self.direction = 'down'
        self.game_speed = 100  # Default speed (milliseconds)
        self.paused = False
        self.game_running = False
        
        # Create the start menu
        self.show_start_menu()
    
    def center_window(self):
        window_width = GAME_WIDTH
        window_height = GAME_HEIGHT + 60  # Extra space for score
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        
        self.window.geometry(f"{window_width}x{window_height}+{50}+{50}")
    
    def show_start_menu(self):
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Create menu frame
        menu_frame = Frame(self.window, bg="#333333", width=GAME_WIDTH, height=GAME_HEIGHT)
        menu_frame.pack(fill="both", expand=True)
        
        # Title
        title_label = Label(menu_frame, text="SNAKE GAME", font=('consolas', 40), bg="#333333", fg="white")
        title_label.pack(pady=50)
        
        # Speed selection with slider
        speed_frame = Frame(menu_frame, bg="#333333")
        speed_frame.pack(pady=20)
        
        speed_label = Label(speed_frame, text="Game Speed:", font=('consolas', 20), bg="#333333", fg="white")
        speed_label.pack(pady=10)
        
        # Speed slider
        self.speed_value = IntVar()
        self.speed_value.set(100)  # Default medium speed
        
        speed_slider = Scale(speed_frame, from_=200, to=20, 
                           orient=HORIZONTAL, length=400, 
                           variable=self.speed_value,
                           label="Slow ←→ Fast",
                           font=('consolas', 12),
                           bg="#333333", fg="white",
                           troughcolor="#555555", 
                           highlightthickness=0,
                           sliderlength=30,
                           command=self.update_speed_label)
        speed_slider.pack(pady=10)
        
        # Current speed display
        self.speed_display = Label(speed_frame, 
                                 text=f"Current Speed: {self.speed_value.get()} ms (lower = faster)", 
                                 font=('consolas', 14), 
                                 bg="#333333", fg="white")
        self.speed_display.pack(pady=10)
        
        # Buttons
        button_frame = Frame(menu_frame, bg="#333333")
        button_frame.pack(pady=40)
        
        start_button = Button(button_frame, text="Start Game", font=('consolas', 18), 
                             command=self.start_game, bg="#4CAF50", fg="white", padx=20, pady=10)
        start_button.grid(row=0, column=0, padx=20)
        
        quit_button = Button(button_frame, text="Quit", font=('consolas', 18), 
                            command=self.window.destroy, bg="#F44336", fg="white", padx=20, pady=10)
        quit_button.grid(row=0, column=1, padx=20)
        
        # Instructions
        instructions = Label(menu_frame, text="Use arrow keys to control the snake.\n"
                                             "Press 'P' to pause the game during play.",
                            font=('consolas', 14), bg="#333333", fg="white", justify="center")
        instructions.pack(pady=30)
    
    def update_speed_label(self, value):
        self.speed_display.config(text=f"Current Speed: {self.speed_value.get()} ms (lower = faster)")
    
    def start_game(self):
        # Get selected speed from slider
        self.game_speed = self.speed_value.get()
        
        # Clear window
        for widget in self.window.winfo_children():
            widget.destroy()
        
        # Create score label
        self.score_label = Label(self.window, text="Score: 0", font=('consolas', 40))
        self.score_label.pack()
        
        # Create canvas
        global canvas
        canvas = Canvas(self.window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        canvas.pack()
        
        # Set up key bindings
        self.window.bind('<Left>', lambda event: self.change_direction('left'))
        self.window.bind('<Right>', lambda event: self.change_direction('right'))
        self.window.bind('<Up>', lambda event: self.change_direction('up'))
        self.window.bind('<Down>', lambda event: self.change_direction('down'))
        self.window.bind('p', lambda event: self.toggle_pause())
        self.window.bind('P', lambda event: self.toggle_pause())
        
        # Reset game state
        self.score = 0
        self.direction = 'down'
        self.paused = False
        self.game_running = True
        
        # Start the game
        self.snake = Snake()
        self.food = Food()
        self.next_turn()
    
    def toggle_pause(self):
        if self.game_running:
            self.paused = not self.paused
            if self.paused:
                # Show pause message
                self.pause_text = canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2, 
                                                   text="PAUSED\nPress 'P' to continue", 
                                                   font=('consolas', 30), fill="white", justify="center")
            else:
                # Remove pause message and continue game
                canvas.delete(self.pause_text)
                self.next_turn()
    
    def change_direction(self, new_direction):
        if not self.paused:
            if new_direction == 'left' and self.direction != 'right':
                self.direction = new_direction
            elif new_direction == 'right' and self.direction != 'left':
                self.direction = new_direction
            elif new_direction == 'up' and self.direction != 'down':
                self.direction = new_direction
            elif new_direction == 'down' and self.direction != 'up':
                self.direction = new_direction
    
    def next_turn(self):
        if self.paused or not self.game_running:
            return
            
        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE

        self.snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        self.snake.squares.insert(0, square)

        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.score_label.config(text="Score:{}".format(self.score))
            canvas.delete("food")
            self.food = Food()
        else:
            del self.snake.coordinates[-1]
            canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collisions():
            self.game_over()
        else:
            self.window.after(self.game_speed, self.next_turn)
    
    def check_collisions(self):
        x, y = self.snake.coordinates[0]

        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False
    
    def game_over(self):
        self.game_running = False
        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                          font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")
        
        # Add buttons to return to menu or quit
        restart_button = Button(self.window, text="Return to Menu", font=('consolas', 16), 
                              command=self.show_start_menu, bg="#3498db", fg="white")
        restart_button.place(x=GAME_WIDTH/2 - 150, y=GAME_HEIGHT/2 + 100, width=200, height=50)
        
        quit_button = Button(self.window, text="Quit", font=('consolas', 16), 
                           command=self.window.destroy, bg="#F44336", fg="white")
        quit_button.place(x=GAME_WIDTH/2 + 50, y=GAME_HEIGHT/2 + 100, width=100, height=50)

if __name__ == "__main__":
    window = Tk()
    game = SnakeGame(window)
    window.mainloop()
