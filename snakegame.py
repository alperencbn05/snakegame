from tkinter import *
import random

# Constants
SQUARE_SIZE = 20
WIDTH = 400
HEIGHT = 400
FOOD_SIZE = 10
GAME_SPEED = 200  # milliseconds

# Game state
score = 0
snake = [[60, 100], [40, 100], [20, 100]]
direction = "Right"
food = [random.choice(range(0, WIDTH, SQUARE_SIZE)), 
        random.choice(range(0, HEIGHT, SQUARE_SIZE))]

# Initialize window
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

def change_direction(event):
    global direction
    if event.keysym == "Up" and direction != "Down":
        direction = "Up"
    elif event.keysym == "Down" and direction != "Up":
        direction = "Down"
    elif event.keysym == "Left" and direction != "Right":
        direction = "Left"
    elif event.keysym == "Right" and direction != "Left":
        direction = "Right"

def move():
    global food, snake, direction, score

    # Get current head position
    x, y = snake[0]
    
    # Calculate new head position
    if direction == "Up":
        y -= SQUARE_SIZE
    elif direction == "Down":
        y += SQUARE_SIZE
    elif direction == "Left":
        x -= SQUARE_SIZE
    elif direction == "Right":
        x += SQUARE_SIZE

    # Update snake
    new_head = [x, y]
    snake.insert(0, new_head)
    snake.pop()

    # Clear canvas
    canvas.delete("all")

    # Draw snake
    for part_x, part_y in snake:
        canvas.create_rectangle(part_x, part_y, 
                              part_x + SQUARE_SIZE, 
                              part_y + SQUARE_SIZE, 
                              fill="green")

    # Draw food
    canvas.create_rectangle(food[0], food[1], 
                          food[0] + FOOD_SIZE, 
                          food[1] + FOOD_SIZE, 
                          fill="red")

    # Check if food is eaten
    if snake[0] == food:
        score += 1
        snake.append(snake[-1])  # Add new segment
        food = [random.choice(range(0, WIDTH, SQUARE_SIZE)),
                random.choice(range(0, HEIGHT, SQUARE_SIZE))]

    # Draw score
    canvas.create_text(50, 10, text=f"Score: {score}", 
                      font=("Arial", 12), fill="black")

    if game_over():
        return
    canvas.after(GAME_SPEED, move)

def restart_game():
    global snake, food, score, direction, btn, final_score
    try: 
        btn.destroy()
    except:
        pass
    try:
        final_score.destroy()
    except:
        pass

    snake = [[60, 100], [40, 100], [20, 100]]
    direction = "Right"
    food = [random.choice(range(0, WIDTH, SQUARE_SIZE)),
            random.choice(range(0, HEIGHT, SQUARE_SIZE))]
    score = 0
    canvas.delete("all")
    move()

def game_over():
    global snake, btn, final_score, score

    # Check wall collision
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or 
        snake[0][1] < 0 or snake[0][1] >= HEIGHT or
        snake[0] in snake[1:]):  # Check self collision
        
        canvas.delete("all")
        canvas.create_text(WIDTH // 2, HEIGHT // 2, 
                          text="Game Over!", 
                          font=("Arial", 24), fill="red")

        btn = Button(window, text="Restart", 
                    command=restart_game)
        canvas.create_window(WIDTH//2, HEIGHT//2 + 40, 
                           window=btn)

        final_score = Label(window, text=f"Score: {score}", 
                           font=("Arial", 12))
        canvas.create_window(WIDTH//2, HEIGHT//2 + 70, 
                           window=final_score, anchor="center")
        return True
    
    return False

# Start game
window.bind("<KeyPress>", change_direction)
move()
window.mainloop()
