import tkinter
from tkinter import *
import win32api
from GUI_Frame_1_0 import GUI_Label_CardName_Updater, GUI_Label_CardSet_Updater, GUI_Label_CardNumber_Updater, GUI_Label_CommitQuantity_Updater
from GUI_Frame_1_0 import GUI_Label_CardPriceLow_Updater, GUI_Label_CardPriceHigh_Updater, GUI_Label_CardPriceAverage_Updater
from API_YUGIOH import API_GetStatus, API_SearchCardNumber
from Database_YUGIOH import YUGIOH_DataBase_AddCard

#palette #F7EFE7 #BFB0A0 #312C38 #E73C37

BackgroundColor = "#312C38"
TextColor0 = "#BFB0A0"
TextColor1 = "#F7EFE7"

class Frame_0_0:
    def __init__(cls, MASTER, WIDTH, HEIGHT):
        global GUI_Frame
        GUI_Frame = tkinter.Frame(master = MASTER)
        GUI_Frame.config(width = WIDTH, height = HEIGHT)
        GUI_Frame.config(bg = BackgroundColor)
        GUI_Frame.place(relx = 0)
        
        global GUI_Label_Mode
        GUI_Label_Mode = tkinter.Label(master = GUI_Frame)
        GUI_Label_Mode.config(text = "MANUAL MODE")
        GUI_Label_Mode.config(bg = BackgroundColor, fg = TextColor0, bd = 0)
        GUI_Label_Mode.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.05)
        
        global GUI_Label_CardNumber
        GUI_Label_CardNumber = tkinter.Label(master = GUI_Frame)
        GUI_Label_CardNumber.config(text = "Enter C/N")
        GUI_Label_CardNumber.config(bg = BackgroundColor, fg = TextColor0, bd = 0)
        GUI_Label_CardNumber.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.15)
        
        global GUI_Entry_CardNumber
        GUI_Entry_CardNumber = tkinter.Entry(master = GUI_Frame, justify = tkinter.CENTER)
        GUI_Entry_CardNumber.insert(0, "Enter Card Number")
        #self.GUI_Entry_CardNumber.config(bg = "red", bd = 0)
        GUI_Entry_CardNumber.bind("<FocusIn>", GUI_Entry_CardNumber_ClearEntry)
        GUI_Entry_CardNumber.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.2)

        global GUI_Label_CardQuantity
        GUI_Label_CardQuantity = tkinter.Label(master = GUI_Frame)
        GUI_Label_CardQuantity.config(text = "Enter Quantity")
        GUI_Label_CardQuantity.config(bg = BackgroundColor, fg = TextColor0, bd = 0)
        GUI_Label_CardQuantity.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.3)
        
        global GUI_Entry_CardQuantity
        GUI_Entry_CardQuantity = tkinter.Entry(master = GUI_Frame, justify = tkinter.CENTER)
        GUI_Entry_CardQuantity.insert(0, "1")
        #self.GUI_Entry_CardNumber.config(bg = "red", bd = 0)
        GUI_Entry_CardQuantity.bind("<FocusIn>", GUI_Entry_CardQuantity_ClearEntry)
        GUI_Entry_CardQuantity.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.35)
        
        global GUI_Label_ButtonInformation
        GUI_Label_ButtonInformation = tkinter.Label(master = GUI_Frame)
        GUI_Label_ButtonInformation.config(text = "Press Search")
        GUI_Label_ButtonInformation.config(bg = BackgroundColor, fg = TextColor0, bd = 0)
        GUI_Label_ButtonInformation.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.85)
        
        global GUI_Button_0
        GUI_Button_0 = tkinter.Button(master = GUI_Frame)
        GUI_Button_0.config(text = "SEARCH")
        GUI_Button_0.config(bg = BackgroundColor, fg = TextColor0)
        GUI_Button_0.config(command = GUI_Button_0_Function)
        GUI_Button_0.place(anchor = tkinter.CENTER, relx = 0.3, rely = 0.95, width = int(WIDTH / 3), height = int(HEIGHT / 20))
        
        global GUI_Button_1
        GUI_Button_1 = tkinter.Button(master = GUI_Frame)
        GUI_Button_1.config(text = "COMMIT")
        GUI_Button_1.config(bg = BackgroundColor, fg = TextColor0)
        GUI_Button_1.config(command = GUI_Button_1_Function)
        GUI_Button_1.place(anchor = tkinter.CENTER, relx = 0.7, rely = 0.95, width = int(WIDTH / 3), height = int(HEIGHT / 20))
        

def GUI_Entry_CardNumber_ClearEntry(cls):
    GUI_Entry_CardNumber.delete(0, "end")
    GUI_Entry_CardNumber.update()
    GUI_Label_ButtonInformation.config(text = "Press SEARCH")
    GUI_Label_ButtonInformation.update()

def GUI_Entry_CardQuantity_ClearEntry(cls):
    GUI_Entry_CardQuantity.delete(0, "end")
    GUI_Entry_CardQuantity.update()


global ConfirmState
ConfirmState = False


def GUI_Button_0_Function():
    GUI_Label_CommitQuantity_Updater("")
    EntryText = GUI_Entry_CardNumber.get()
    global API_DATA
    API_DATA = API_SearchCardNumber(EntryText)
    API_STATUS = API_DATA['status']
    if API_STATUS == "fail":
        GUI_Label_ButtonInformation.config(text = "Wrong card number")
        GUI_Label_ButtonInformation.update()
    else:
        GUI_Label_ButtonInformation.config(text = "Press COMMIT to Add")
        GUI_Label_CardSet_Updater(API_DATA['data']['price_data']['name'])
        GUI_Label_CardName_Updater(API_DATA['data']['name'])
        GUI_Label_CardNumber_Updater(API_DATA['data']['price_data']['print_tag'])
        GUI_Label_CardPriceLow_Updater(API_DATA['data']['price_data']['price_data']['data']['prices']['low'])
        GUI_Label_CardPriceHigh_Updater(API_DATA['data']['price_data']['price_data']['data']['prices']['high'])
        GUI_Label_CardPriceAverage_Updater(API_DATA['data']['price_data']['price_data']['data']['prices']['average'])
        
        global ConfirmState
        ConfirmState = True

def GUI_Button_1_Function():
    global ConfirmState, API_DATA
    if ConfirmState == True:
        ConfirmState = False
        EntryQuantity = GUI_Entry_CardQuantity.get()
        New_Card = YUGIOH_DataBase_AddCard(API_DATA, EntryQuantity)
        if New_Card == "New":
            GUI_Label_CommitQuantity_Updater("New Addition!")
        else:
            GUI_Label_CommitQuantity_Updater("Owned QTY: {}".format(New_Card))
        
        
        GUI_Label_ButtonInformation.config(text = "Success! Card Added")
        
        GUI_Entry_CardNumber.delete(0, "end")
        GUI_Entry_CardNumber.update()
        GUI_Entry_CardNumber.focus_set()
        
        GUI_Entry_CardQuantity.delete(0, "end")
        GUI_Entry_CardQuantity.insert(0, "1")
        GUI_Entry_CardQuantity.update()
    else:
        pass