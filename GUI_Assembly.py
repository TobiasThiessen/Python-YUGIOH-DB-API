import tkinter as tk
from tkinter import *
import win32api
from GUI_Frame_0_0 import Frame_0_0
from GUI_Frame_1_0 import Frame_1_0
from GUI_Frame_2_0 import Frame_2_0

Screen_Width = win32api.GetSystemMetrics(0)
Screen_Height = win32api.GetSystemMetrics(1)

GUI_Window_Title = "YUGIOH-DATABASE"
GUI_Window_Width = int(win32api.GetSystemMetrics(0) / 2)
GUI_Window_Height = int(win32api.GetSystemMetrics(1) / 3)
GUI_Window = tk.Tk()
GUI_Window.title(GUI_Window_Title)
GUI_Window.geometry("{}x{}+{}+{}".format(GUI_Window_Width, GUI_Window_Height, 0, 0), )
GUI_Window.resizable(False, False)
#GUI_Window.overrideredirect(True)

Frame_Width = int(GUI_Window_Width / 5)
Frame_Width2 = int((GUI_Window_Width / 5) * 3)
Frame_0_0(GUI_Window, Frame_Width, GUI_Window_Height)
Frame_1_0(GUI_Window, Frame_Width, GUI_Window_Height)
Frame_2_0(GUI_Window, Frame_Width2, GUI_Window_Height)

GUI_Window.update()
GUI_Window.mainloop()