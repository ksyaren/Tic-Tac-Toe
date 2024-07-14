import tkinter as tk

def set_tile(row, column):
    global current_player

    if game_over:
        return

    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = current_player

    if current_player == playerO:
        board[row][column].config(foreground=o_color)
        current_player = playerX
    else:
        board[row][column].config(foreground=x_color)
        current_player = playerO

    label["text"] = current_player + "'s turn"

    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
           and board[row][0]["text"] != ""):
             label.config(text=board[row][0]["text"] + " is the winner", foreground=color_gray) 
             for column in range(3):
                 board[row][column].config(foreground=color_gray, background=color_light_turquoise)
             game_over = True
             return
        
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner", foreground=color_gray)
            for row in range(3):
                 board[row][column].config(foreground=color_gray, background=color_light_turquoise)
            game_over = True
            return

    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
       and board[0][0]["text"] != ""):
         label.config(text=board[0][0]["text"] + "  winner", foreground=color_gray)
         for i in range(3):
             board[i][i].config(foreground=color_gray, background=color_light_turquoise)
         game_over = True
         return
    
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + "  winner", foreground=color_gray)
        board[0][2].config(foreground=color_gray, background=color_light_turquoise)
        board[1][1].config(foreground=color_gray, background=color_light_turquoise)
        board[2][0].config(foreground=color_gray, background=color_light_turquoise)
        game_over = True
        return

    if turns == 9:
        game_over = True
        label.config(text="Draw", foreground=color_gray)

def new_game():
    global turns, game_over
    turns = 0
    game_over = False

    label.config(text=current_player + "'s turn", foreground=color_gray, background=color_turquoise) 

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_gray, background=color_turquoise)

# game setup
playerX = "X"
playerO = "O"
current_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_gray = "#32cd32"
color_light_turquoise = "#ffffff"
color_turquoise = "#ffffff"
x_color = "#ff2c2c"
o_color = "#1e97f3"

turns = 0
game_over = False

# window setup 
window = tk.Tk()
window.title("Tic-Tac-toe")
window.resizable(False, False)

frame = tk.Frame(window)
label = tk.Label(frame, text=current_player + "'s turn", font=("Arial Rounded MT ", 24, "bold"), background=color_turquoise, foreground="#282828")

label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font=("Arial Rounded MT ", 50, "bold"), background=color_turquoise,
                                       foreground=color_gray, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row + 1, column=column)

button = tk.Button(frame, text="Restart", font=("Arial Rounded MT ", 24, "bold"),
                   background=color_turquoise, foreground="#282828", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
