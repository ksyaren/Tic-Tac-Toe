
import tkinter #* tk-interface (graphical user interface library)

#* game setup

playerX = "X"
playerO = "O"
current_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_yellow ="fac608"
color_gray ="343434"
color_light_turquoise ="14bdac"
color_turquoise ="#14ae9f"

#* window setup 
window = tkinter.TK()
window.title("Tic-Tac-toe")
window.resizable(False, False) #* user cant expand the window

window.mainloop()

