
import tkinter #* tk-interface (graphical user interface library)

def set_tile(row,column):
    pass

def new_game():
    pass

#* game setup

playerX = "X"
playerO = "O"
current_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_yellow ="#fac608"
color_gray ="#343434"
color_light_turquoise ="#14bdac"
color_turquoise ="#14ae9f"

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



