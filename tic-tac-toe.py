
import tkinter #* tk-interface (graphical user interface library)

def set_tile(row,column):
    global current_player

    if(game_over):
        return

    if board[row][column]["text"] != "":
        #*already taken spot
        return
    
    board[row][column]["text"] = current_player #*mark the board

    if current_player == playerO: #*switch player
        current_player = playerX
    else:
        current_player = playerO

    label["text"] = current_player+"'s turn"

    check_winner()

def check_winner():
    global turns, game_over
    turns +=1

    #horizontally check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
           and board[row][0]["text"] != ""):
             label.config(text=board[row][0]["text"]+ " is the winner", foreground=color_gray) 
             for column in range(3):
                 board[row][column].config(foreground=color_gray, background= color_light_turquoise)
             game_over = True
             return
        
    #vertically check 3 columns 
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"]!=""):
            label.config(text=board[0][column]["text"]+ " is the winner", foreground=color_gray)
            for row in range(3):
                 board[row][column].config(foreground=color_gray, background= color_light_turquoise)
            game_over = True
            return

    #diagonally check 2 lines
    if ( board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
       and board[0][0]["text"]!=""):
         label.config(text=board[0][0]["text"]+ " is the winner", foreground=color_gray)
         for i in range(3):
             board[i][i].config(foreground =color_gray, background=color_light_turquoise)
         game_over
         return
    
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] !=""):
        label.config(text=board[0][2]["text"]+ " is the winner", foreground=color_gray)
        board[0][2].config(foreground =color_gray, background=color_light_turquoise)
        board[1][1].config(foreground =color_gray, background=color_light_turquoise)
        board[2][0].config(foreground =color_gray, background=color_light_turquoise)
        game_over
        return

    #tie (draw)
    if(turns ==9):
        game_over = True
        label.config(text="It's a draw", foreground=color_gray)
       



def new_game():
    global turns, game_over
    turns = 0
    game_over = False

    label.config(text=current_player+"'s turn" , foreground=color_yellow, background=color_turquoise) 

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="" ,foreground= color_yellow, background=color_turquoise)


#* game setup

playerX = "X"
playerO = "O"
current_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_yellow ="#f4f2ef"
color_gray ="#e68c3a"
color_light_turquoise ="#94b6ef"
color_turquoise ="#213e60"

turns =0
game_over = False 

#* window setup 
window = tkinter.Tk()
window.title("Tic-Tac-toe")
window.resizable(False, False) #* user cant expand the window

frame = tkinter.Frame(window) 
label = tkinter.Label(frame,text =current_player+"'s turn", font =("Consolas", 20), background = color_turquoise, foreground ="white")

label.grid(row =0 , column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font= ("Consolas" , 50), background=color_turquoise,
                                             foreground=color_yellow, width=4, height=1, command=lambda row=row, column=column: set_tile(row, column))

        board[row][column].grid(row= row+1, column= column)


button = tkinter.Button(frame, text="Resart", font=("Consolas", 20),
                        background=color_turquoise, foreground="white", command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")


frame.pack()


#* center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#*format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()



