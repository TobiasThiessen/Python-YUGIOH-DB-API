import stat
import tkinter
from tkinter import *
from tkinter import font
from turtle import left
import win32api
from time import sleep
from API_YUGIOH import API_GetStatus

#palette #F7EFE7 #BFB0A0 #312C38 #E73C37

Frame_Width = int(win32api.GetSystemMetrics(0) / 5)
Frame_Height = int(win32api.GetSystemMetrics(1) / 3)
BackgroundColor = "#312C38"
TextColor0 = "#BFB0A0"
TextColor1 = "#F7EFE7"

class Frame_1_0:
    def __init__(cls, MASTER, WIDTH, HEIGHT):
        global GUI_Frame
        GUI_Frame = tkinter.Frame(master = MASTER)
        GUI_Frame.config(width = WIDTH, height = HEIGHT)
        GUI_Frame.config(bg = BackgroundColor, relief = tkinter.RAISED)
        GUI_Frame.place(relx = 0.2)
        
        global GUI_Label_APIStatus
        GUI_Label_APIStatusFont = font.Font(size = 8)
        GUI_Label_APIStatus = tkinter.Label(master = GUI_Frame, justify = tkinter.RIGHT)
        GUI_Label_APIStatus.config(text = "API Status:")
        GUI_Label_APIStatus.config(bg = BackgroundColor, fg = TextColor0, font = GUI_Label_APIStatusFont, bd = 0)
        GUI_Label_APIStatus.place(anchor = tkinter.E, relx = 0.5, rely = 0.03)
        
        
        global GUI_Label_APIState
        GUI_Label_APIStateFont = font.Font(size = 8)
        GUI_Label_APIState = tkinter.Label(master = GUI_Frame, justify = tkinter.LEFT)
        APIState, PRICERState = API_GetStatus()
        if APIState == "success":
            GUI_Label_APIState.config(bg = BackgroundColor, fg = "green", font = GUI_Label_APIStateFont, bd = 0)
            GUI_Label_APIState.config(text = APIState)
        else:
            GUI_Label_APIState.config(bg = BackgroundColor, fg = "red", font = GUI_Label_APIStateFont, bd = 0)
            GUI_Label_APIState.config(text = "ERROR")
        GUI_Label_APIState.place(anchor = tkinter.W, relx = 0.52, rely = 0.03)
        
        
        global GUI_Label_PRICERStatus
        GUI_Label_PRICERStatusFont = font.Font(size = 8)
        GUI_Label_PRICERStatus = tkinter.Label(master = GUI_Frame, justify = tkinter.RIGHT)
        GUI_Label_PRICERStatus.config(text = "PRICER Status:")
        GUI_Label_PRICERStatus.config(bg = BackgroundColor, fg = TextColor0, font = GUI_Label_PRICERStatusFont, bd = 0)
        GUI_Label_PRICERStatus.place(anchor = tkinter.E, relx = 0.5, rely = 0.07)
        
        global GUI_Label_PRICERState
        GUI_Label_PRICERStateFont = font.Font(size = 8)
        GUI_Label_PRICERState = tkinter.Label(master = GUI_Frame, justify = tkinter.LEFT)
        APIState, PRICERState = API_GetStatus()
        if PRICERState == "success":
            GUI_Label_PRICERState.config(bg = BackgroundColor, fg = "green", font = GUI_Label_APIStateFont, bd = 0)
            GUI_Label_PRICERState.config(text = APIState)
        else:
            GUI_Label_PRICERState.config(bg = BackgroundColor, fg = "red", font = GUI_Label_APIStateFont, bd = 0)
            GUI_Label_PRICERState.config(text = "ERROR")
        GUI_Label_PRICERState.place(anchor = tkinter.W, relx = 0.52, rely = 0.07)
        
        
        global GUI_Label_CardName0
        GUI_Label_CardName0Font = font.Font(size = 10)
        GUI_Label_CardName0 = tkinter.Label(master = GUI_Frame)
        GUI_Label_CardName0.config(text = "Card Name:")
        GUI_Label_CardName0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_CardName0Font)
        GUI_Label_CardName0.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.15)
        
        global GUI_Label_CardName1
        GUI_Label_CardName1 = tkinter.Label(master = GUI_Frame, wraplength = WIDTH)
        GUI_Label_CardName1.config(text = "Waiting")
        GUI_Label_CardName1.config(bg = BackgroundColor, fg = TextColor1, bd = 0,)
        GUI_Label_CardName1.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.225)
        
        global GUI_Label_CardSet0
        GUI_Label_CardSet0Font = font.Font(size = 10)
        GUI_Label_CardSet0 = tkinter.Label(master = GUI_Frame)
        GUI_Label_CardSet0.config(text = "Card Set:")
        GUI_Label_CardSet0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_CardSet0Font)
        GUI_Label_CardSet0.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.30)
        
        global GUI_Label_CardSet1
        GUI_Label_CardSet1 = tkinter.Label(master = GUI_Frame, wraplength = WIDTH)
        GUI_Label_CardSet1.config(text = "Waiting")
        GUI_Label_CardSet1.config(bg = BackgroundColor, fg = TextColor1, bd = 0)
        GUI_Label_CardSet1.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.40)
        
        global GUI_Label_CardNumber0
        GUI_Label_CardNumber0Font = font.Font(size = 10)
        GUI_Label_CardNumber0 = tkinter.Label(master = GUI_Frame)
        GUI_Label_CardNumber0.config(text = "Card Number:")
        GUI_Label_CardNumber0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_CardNumber0Font)
        GUI_Label_CardNumber0.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.5)
        
        global GUI_Label_CardNumber1
        GUI_Label_CardNumber1 = tkinter.Label(master = GUI_Frame, wraplength = WIDTH)
        GUI_Label_CardNumber1.config(text = "Waiting")
        GUI_Label_CardNumber1.config(bg = BackgroundColor, fg = TextColor1, bd = 0)
        GUI_Label_CardNumber1.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.55)
        
        global GUI_Label_CardPriceLow0
        GUI_Label_CardPriceLow0 = tkinter.Label(master = GUI_Frame, justify = tkinter.LEFT)
        GUI_Label_CardPriceLow0.config(text = "Low:")
        GUI_Label_CardPriceLow0.config(bg = BackgroundColor, fg = TextColor0, bd = 0)
        GUI_Label_CardPriceLow0.place(anchor = tkinter.E, relx = 0.5, rely = 0.6)
        
        global GUI_Label_CardPriceLow1
        GUI_Label_CardPriceLow1 = tkinter.Label(master = GUI_Frame, justify = tkinter.RIGHT)
        GUI_Label_CardPriceLow1.config(text = "Waiting")
        GUI_Label_CardPriceLow1.config(bg = BackgroundColor, fg = TextColor1, bd = 0)
        GUI_Label_CardPriceLow1.place(anchor = tkinter.W, relx = 0.52, rely = 0.6)
        
        global GUI_Label_CardPriceHigh0
        GUI_Label_CardPriceHigh0 = tkinter.Label(master = GUI_Frame, justify = tkinter.LEFT)
        GUI_Label_CardPriceHigh0.config(text = "High:")
        GUI_Label_CardPriceHigh0.config(bg = BackgroundColor, fg = TextColor0, bd = 0)
        GUI_Label_CardPriceHigh0.place(anchor = tkinter.E, relx = 0.5, rely = 0.65)
        
        global GUI_Label_CardPriceHigh1
        GUI_Label_CardPriceHigh1 = tkinter.Label(master = GUI_Frame, justify = tkinter.RIGHT)
        GUI_Label_CardPriceHigh1.config(text = "Waiting")
        GUI_Label_CardPriceHigh1.config(bg = BackgroundColor, fg = TextColor1, bd = 0)
        GUI_Label_CardPriceHigh1.place(anchor = tkinter.W, relx = 0.52, rely = 0.65)
        
        global GUI_Label_CardPriceAverage0
        GUI_Label_CardPriceAverage0 = tkinter.Label(master = GUI_Frame, justify = tkinter.LEFT)
        GUI_Label_CardPriceAverage0.config(text = "Average:")
        GUI_Label_CardPriceAverage0.config(bg = BackgroundColor, fg = TextColor0, bd = 0)
        GUI_Label_CardPriceAverage0.place(anchor = tkinter.E, relx = 0.5, rely = 0.7)
        
        global GUI_Label_CardPriceAverage1
        GUI_Label_CardPriceAverage1 = tkinter.Label(master = GUI_Frame, justify = tkinter.RIGHT)
        GUI_Label_CardPriceAverage1.config(text = "Waiting")
        GUI_Label_CardPriceAverage1.config(bg = BackgroundColor, fg = TextColor1, bd = 0)
        GUI_Label_CardPriceAverage1.place(anchor = tkinter.W, relx = 0.52, rely = 0.7)
        
        global GUI_Label_CommitQuantity
        GUI_Label_CommitQuantityFont = font.Font(size = 16)
        GUI_Label_CommitQuantity = tkinter.Label(master = GUI_Frame)
        GUI_Label_CommitQuantity.config(text = "")
        GUI_Label_CommitQuantity.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_CommitQuantityFont)
        GUI_Label_CommitQuantity.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.85)


def GUI_Label_CardName_Updater(TEXT):
    GUI_Label_CardName1.config(text = TEXT)
    GUI_Label_CardName1.update()
    
def GUI_Label_CardSet_Updater(TEXT):
    GUI_Label_CardSet1.config(text = TEXT)
    GUI_Label_CardSet1.update()

def GUI_Label_CardNumber_Updater(TEXT):
    GUI_Label_CardNumber1.config(text = TEXT)
    GUI_Label_CardNumber1.update()
    
def GUI_Label_CardPriceLow_Updater(TEXT):
    GUI_Label_CardPriceLow1.config(text = f"{TEXT}$")
    GUI_Label_CardPriceLow1.update()    
    
def GUI_Label_CardPriceHigh_Updater(TEXT):
    GUI_Label_CardPriceHigh1.config(text = f"{TEXT}$")
    GUI_Label_CardPriceHigh1.update()
    
def GUI_Label_CardPriceAverage_Updater(TEXT):
    GUI_Label_CardPriceAverage1.config(text = f"{TEXT}$")
    GUI_Label_CardPriceAverage1.update()
    
def GUI_Label_CommitQuantity_Updater(TEXT):
    GUI_Label_CommitQuantity.config(text = TEXT)
    GUI_Label_CommitQuantity.update()