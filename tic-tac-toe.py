
import tkinter #* tk-interface (graphical user interface library)

def set_tile(row,column):
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

frame.pack()


window.mainloop()



