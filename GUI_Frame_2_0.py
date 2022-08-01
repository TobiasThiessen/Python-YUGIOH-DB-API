import tkinter
from tkinter import *
from tkinter import font
import sqlite3
from tkinter import ttk
from Database_YUGIOH import YUGIOH_Database_CardQuantity, YUGIOH_Database_MostValuable, YUGIOH_Database_LeastValuable, YUGIOH_Database_CommonValuable, YUGIOH_Database_QueryAll
from Database_YUGIOH import YUGIOH_Databased_TotalValueHigh, YUGIOH_Databased_TotalValueLow, YUGIOH_Databased_TotalValueAverage, YUGIOH_Database_CardUnique

#palette #F7EFE7 #BFB0A0 #312C38 #E73C37

BackgroundColor = "#312C38"
TextColor0 = "#BFB0A0"
TextColor1 = "#F7EFE7"

class Frame_2_0:
    def __init__(cls, MASTER, WIDTH, HEIGHT):
        global GUI_Frame
        GUI_Frame = tkinter.Frame(master = MASTER)
        GUI_Frame.config(width = WIDTH, height = HEIGHT)
        GUI_Frame.config(bg = BackgroundColor, relief = tkinter.RAISED)
        GUI_Frame.place(relx = 0.4)
        
        global GUI_Label_Title
        GUI_Label_TitleFont = font.Font(size = 16)
        GUI_Label_Title = tkinter.Label(master = GUI_Frame)
        GUI_Label_Title.config(text = "YUGIOH Card Database")
        GUI_Label_Title.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_TitleFont)
        GUI_Label_Title.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.05)
        
        global GUI_Label_Information
        GUI_Label_InformationFont = font.Font(size = 12)
        GUI_Label_Information = tkinter.Label(master = GUI_Frame)
        GUI_Label_Information.config(text = "Press a button to open database \n Larger databases might take longer to open")
        GUI_Label_Information.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_InformationFont)
        GUI_Label_Information.place(anchor = tkinter.CENTER, relx = 0.5, rely = 0.5)
        
        global GUI_Button_0
        GUI_Button_0 = tkinter.Button(master = GUI_Frame)
        GUI_Button_0.config(text = "STATS")
        GUI_Button_0.config(bg = BackgroundColor, fg = TextColor0)
        GUI_Button_0.config(command = GUI_Button_0_Function)
        GUI_Button_0.place(anchor = tkinter.CENTER, relx = 0.3, rely = 0.95, width = int(WIDTH / 8), height = int(HEIGHT / 20))
        
        global GUI_Button_1
        GUI_Button_1 = tkinter.Button(master = GUI_Frame)
        GUI_Button_1.config(text = "DATABASE")
        GUI_Button_1.config(bg = BackgroundColor, fg = TextColor0)
        GUI_Button_1.config(command = GUI_Button_1_Function)
        GUI_Button_1.place(anchor = tkinter.CENTER, relx = 0.7, rely = 0.95, width = int(WIDTH / 8), height = int(HEIGHT / 20))

        # All the text in the stats frame, updated and shown by pressing STATS button - controlled by GUI_Button_0_Function
        class Frame_2_1:
            global GUI_Frame_2_1
            GUI_Frame_2_1 = tkinter.Frame(master = GUI_Frame)
            GUI_Frame_2_1.config(width = int(WIDTH * 0.99), height = int(HEIGHT * 0.8))
            GUI_Frame_2_1.config(bg = BackgroundColor, relief = tkinter.RAISED, bd = 1)
            #GUI_Frame_2_1.place(relx = 0, rely = 0.1)
            
            RelY, RelYoffset = 0.05, 0.05
            global GUI_Label_Database_CardQuantity0
            GUI_Label_Database_CardQuantity0Font = font.Font(size = 8)
            GUI_Label_Database_CardQuantity0 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.LEFT)
            GUI_Label_Database_CardQuantity0.config(text = "Total Cards:")
            GUI_Label_Database_CardQuantity0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_Database_CardQuantity0Font)
            GUI_Label_Database_CardQuantity0.place(anchor = tkinter.E, relx = 0.2, rely = RelY)
            
            global GUI_Label_Database_CardQuantity1
            GUI_Label_Database_CardQuantity1Font = font.Font(size = 8)
            GUI_Label_Database_CardQuantity1 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.RIGHT)
            Total_Quantity = YUGIOH_Database_CardQuantity()
            GUI_Label_Database_CardQuantity1.config(text = Total_Quantity)
            GUI_Label_Database_CardQuantity1.config(bg = BackgroundColor, fg = TextColor1, bd = 0, font = GUI_Label_Database_CardQuantity1Font)
            GUI_Label_Database_CardQuantity1.place(anchor = tkinter.W, relx = 0.205, rely = RelY)
            
            RelY = RelY + RelYoffset
            global GUI_Label_Database_CardUnique0
            GUI_Label_Database_CardUnique0Font = font.Font(size = 8)
            GUI_Label_Database_CardUnique0 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.LEFT)
            GUI_Label_Database_CardUnique0.config(text = "Unique Cards:")
            GUI_Label_Database_CardUnique0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_Database_CardUnique0Font)
            GUI_Label_Database_CardUnique0.place(anchor = tkinter.E, relx = 0.2, rely = RelY)
            
            global GUI_Label_Database_CardUnique1
            GUI_Label_Database_CardUnique1Font = font.Font(size = 8)
            GUI_Label_Database_CardUnique1 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.RIGHT)
            UniqueCards = YUGIOH_Database_CardUnique()
            GUI_Label_Database_CardUnique1.config(text = UniqueCards)
            GUI_Label_Database_CardUnique1.config(bg = BackgroundColor, fg = TextColor1, bd = 0, font = GUI_Label_Database_CardUnique1Font)
            GUI_Label_Database_CardUnique1.place(anchor = tkinter.W, relx = 0.205, rely = RelY)
            
            RelY = RelY + RelYoffset
            global GUI_Label_Database_CardMostValuable0
            GUI_Label_Database_CardMostValuable0Font = font.Font(size = 8)
            GUI_Label_Database_CardMostValuable0 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.LEFT)
            GUI_Label_Database_CardMostValuable0.config(text = "Most Valuable Card:")
            GUI_Label_Database_CardMostValuable0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_Database_CardMostValuable0Font)
            GUI_Label_Database_CardMostValuable0.place(anchor = tkinter.E, relx = 0.2, rely = RelY)
            
            global GUI_Label_Database_CardMostValuable1
            GUI_Label_Database_CardMostValuable1Font = font.Font(size = 8)
            GUI_Label_Database_CardMostValuable1 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.RIGHT)
            MostValuable = YUGIOH_Database_MostValuable()
            GUI_Label_Database_CardMostValuable1.config(text = MostValuable)
            GUI_Label_Database_CardMostValuable1.config(bg = BackgroundColor, fg = TextColor1, bd = 0, font = GUI_Label_Database_CardMostValuable1Font)
            GUI_Label_Database_CardMostValuable1.place(anchor = tkinter.W, relx = 0.205, rely = RelY)
            
            RelY = RelY + RelYoffset
            global GUI_Label_Database_CardLeastValuable0
            GUI_Label_Database_CardLeastValuable0Font = font.Font(size = 8)
            GUI_Label_Database_CardLeastValuable0 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.LEFT)
            GUI_Label_Database_CardLeastValuable0.config(text = "Least Valuable Card:")
            GUI_Label_Database_CardLeastValuable0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_Database_CardLeastValuable0Font)
            GUI_Label_Database_CardLeastValuable0.place(anchor = tkinter.E, relx = 0.2, rely = RelY)
            
            global GUI_Label_Database_CardLeastValuable1
            GUI_Label_Database_CardLeastValuable1Font = font.Font(size = 8)
            GUI_Label_Database_CardLeastValuable1 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.RIGHT)
            LeastValuable = YUGIOH_Database_LeastValuable()
            GUI_Label_Database_CardLeastValuable1.config(text = LeastValuable)
            GUI_Label_Database_CardLeastValuable1.config(bg = BackgroundColor, fg = TextColor1, bd = 0, font = GUI_Label_Database_CardLeastValuable1Font)
            GUI_Label_Database_CardLeastValuable1.place(anchor = tkinter.W, relx = 0.205, rely = RelY)
            
            RelY = RelY + RelYoffset
            global GUI_Label_Database_CardCommon0
            GUI_Label_Database_CardCommon0Font = font.Font(size = 8)
            GUI_Label_Database_CardCommon0 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.LEFT)
            GUI_Label_Database_CardCommon0.config(text = "Most Common Card:")
            GUI_Label_Database_CardCommon0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_Database_CardCommon0Font)
            GUI_Label_Database_CardCommon0.place(anchor = tkinter.E, relx = 0.2, rely = RelY)
            
            global GUI_Label_Database_CardCommon1
            GUI_Label_Database_CardCommon1Font = font.Font(size = 8)
            GUI_Label_Database_CardCommon1 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.RIGHT)
            Common = YUGIOH_Database_CommonValuable()
            GUI_Label_Database_CardCommon1.config(text = Common)
            GUI_Label_Database_CardCommon1.config(bg = BackgroundColor, fg = TextColor1, bd = 0, font = GUI_Label_Database_CardCommon1Font)
            GUI_Label_Database_CardCommon1.place(anchor = tkinter.W, relx = 0.205, rely = RelY)
            
            RelY = RelY + RelYoffset
            global GUI_Label_Database_TotalValueHigh0
            GUI_Label_Database_TotalValueHigh0Font = font.Font(size = 8)
            GUI_Label_Database_TotalValueHigh0 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.LEFT)
            GUI_Label_Database_TotalValueHigh0.config(text = "Total Value High:")
            GUI_Label_Database_TotalValueHigh0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_Database_CardCommon0Font)
            GUI_Label_Database_TotalValueHigh0.place(anchor = tkinter.E, relx = 0.2, rely = RelY)
            
            global GUI_Label_Database_TotalValueHigh1
            GUI_Label_Database_TotalValueHigh1Font = font.Font(size = 8)
            GUI_Label_Database_TotalValueHigh1 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.RIGHT)
            TotalHigh = YUGIOH_Databased_TotalValueHigh()
            GUI_Label_Database_TotalValueHigh1.config(text = TotalHigh)
            GUI_Label_Database_TotalValueHigh1.config(bg = BackgroundColor, fg = TextColor1, bd = 0, font = GUI_Label_Database_CardCommon1Font)
            GUI_Label_Database_TotalValueHigh1.place(anchor = tkinter.W, relx = 0.205, rely = RelY)
            
            RelY = RelY + RelYoffset
            global GUI_Label_Database_TotalValueLow0
            GUI_Label_Database_TotalValueLow0Font = font.Font(size = 8)
            GUI_Label_Database_TotalValueLow0 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.LEFT)
            GUI_Label_Database_TotalValueLow0.config(text = "Total Value Low:")
            GUI_Label_Database_TotalValueLow0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_Database_CardCommon0Font)
            GUI_Label_Database_TotalValueLow0.place(anchor = tkinter.E, relx = 0.2, rely = RelY)
            
            global GUI_Label_Database_TotalValueLow1
            GUI_Label_Database_TotalValueLow1Font = font.Font(size = 8)
            GUI_Label_Database_TotalValueLow1 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.RIGHT)
            TotalLow = YUGIOH_Databased_TotalValueLow()
            GUI_Label_Database_TotalValueLow1.config(text = TotalLow)
            GUI_Label_Database_TotalValueLow1.config(bg = BackgroundColor, fg = TextColor1, bd = 0, font = GUI_Label_Database_CardCommon1Font)
            GUI_Label_Database_TotalValueLow1.place(anchor = tkinter.W, relx = 0.205, rely = RelY)
            
            RelY = RelY + RelYoffset
            global GUI_Label_Database_TotalValueAverage0
            GUI_Label_Database_TotalValueAverage0Font = font.Font(size = 8)
            GUI_Label_Database_TotalValueAverage0 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.LEFT)
            GUI_Label_Database_TotalValueAverage0.config(text = "Total Value Average:")
            GUI_Label_Database_TotalValueAverage0.config(bg = BackgroundColor, fg = TextColor0, bd = 0, font = GUI_Label_Database_CardCommon0Font)
            GUI_Label_Database_TotalValueAverage0.place(anchor = tkinter.E, relx = 0.2, rely = RelY)
            
            global GUI_Label_Database_TotalValueAverage1
            GUI_Label_Database_TotalValueAverage1Font = font.Font(size = 8)
            GUI_Label_Database_TotalValueAverage1 = tkinter.Label(master = GUI_Frame_2_1, justify = tkinter.RIGHT)
            TotalAverage = YUGIOH_Databased_TotalValueAverage()
            GUI_Label_Database_TotalValueAverage1.config(text = TotalAverage)
            GUI_Label_Database_TotalValueAverage1.config(bg = BackgroundColor, fg = TextColor1, bd = 0, font = GUI_Label_Database_CardCommon1Font)
            GUI_Label_Database_TotalValueAverage1.place(anchor = tkinter.W, relx = 0.205, rely = RelY)
            
        # All the text / table in the Database frame - updated / shown from GUI_Button_1_Function
        class Frame_2_2:
            GUI_Frame_2_2_Width = int(WIDTH * 0.99)
            GUI_Frame_2_2_Height = int(HEIGHT * 0.8)
            global GUI_Frame_2_2
            GUI_Frame_2_2 = tkinter.Frame(master = GUI_Frame)
            GUI_Frame_2_2.config(width = GUI_Frame_2_2_Width, height = GUI_Frame_2_2_Height)
            GUI_Frame_2_2.config(bg = BackgroundColor, relief = tkinter.RAISED, bd = 0)
            
            GUI_ScrollY = ttk.Scrollbar(master = GUI_Frame_2_2)
            GUI_ScrollX = ttk.Scrollbar(master = GUI_Frame_2_2, orient = HORIZONTAL)
            
            global GUI_Database
            GUI_Database = ttk.Treeview(master = GUI_Frame_2_2, yscrollcommand = GUI_ScrollY.set, xscrollcommand = GUI_ScrollX.set)
            GUI_Database.bind("<Double-1>", Treeview_Binding_Function)
            GUI_ScrollY.config(command = GUI_Database.yview)
            GUI_ScrollX.config(command = GUI_Database.xview)
            
            # Columns are taken from the Database Model (See Database_YUGIOH.py: class Database_Table_YUGIOH(CardDatabase.Model))
            GUI_Database['columns'] = ("Card_Number", "Card_Name", "Quantity", "Card_Set_Name", "Price_Low", "Price_High", "Price_Average", "Date_Added")
            
            GUI_Database.column("#0", width = 0,    stretch = NO)
            GUI_Database.column("Card_Number",      stretch = NO, anchor = tkinter.CENTER, width = 85,  minwidth = 0)
            GUI_Database.column("Card_Name",        stretch = NO, anchor = tkinter.CENTER, width = 150)
            GUI_Database.column("Quantity",         stretch = NO, anchor = tkinter.CENTER, width = 35)
            GUI_Database.column("Card_Set_Name",    stretch = NO, anchor = tkinter.CENTER, width = 150)
            GUI_Database.column("Price_Low",        stretch = NO, anchor = tkinter.CENTER, width = 65)
            GUI_Database.column("Price_High",       stretch = NO, anchor = tkinter.CENTER, width = 65)
            GUI_Database.column("Price_Average",    stretch = NO, anchor = tkinter.CENTER, width = 65)
            GUI_Database.column("Date_Added",       stretch = NO, anchor = tkinter.CENTER, width = 150)
            
            GUI_Database.heading("#0", )
            GUI_Database.heading("Card_Number", text = "Card Number", anchor = tkinter.CENTER)
            GUI_Database.heading("Card_Name", text = "Card Name", anchor = tkinter.CENTER)
            GUI_Database.heading("Quantity", text = "QTY", anchor = tkinter.CENTER)
            GUI_Database.heading("Card_Set_Name", text = "Card Set Name", anchor = tkinter.CENTER)
            GUI_Database.heading("Price_Low", text = "Price Low", anchor = tkinter.CENTER)
            GUI_Database.heading("Price_High", text = "Price High", anchor = tkinter.CENTER)
            GUI_Database.heading("Price_Average", text = "Price Average", anchor = tkinter.CENTER)
            GUI_Database.heading("Date_Added", text = "Date Added", anchor = tkinter.CENTER)
            
            
            # QUERIES database and inputs all values
            QUERY = YUGIOH_Database_QueryAll()
            for QUERY in QUERY:
                QueryValues = (QUERY.Card_Number, QUERY.Card_Name, QUERY.Quantity, QUERY.Card_Set_Name, 
                            QUERY.Price_Low, QUERY.Price_High, QUERY.Price_Average, QUERY.Date_Added)
                GUI_Database.insert(parent = "", index = "end",
                                    values = QueryValues)
                
            GUI_Database.place(relx = 0, rely = 0, width = int(GUI_Frame_2_2_Width * 0.96), height = int(GUI_Frame_2_2_Height * 0.95))
            GUI_ScrollY.place(relx = 1, rely = 0, height = int(GUI_Frame_2_2_Height * 0.95), anchor = NE)
            GUI_ScrollX.place(relx = 0, rely = 0.95, width = GUI_Frame_2_2_Width, height = int(GUI_Frame_2_2_Height * 0.05))


def GUI_Button_0_Function(): # Queries a bunch of data from database and updates labels with new values
    GUI_Frame_2_2.place_forget()
    GUI_Label_Information.config(text = "Loading STATS")
    GUI_Label_Information.update()
    GUI_Frame_2_1.place(relx = 0, rely = 0.1)
    GUI_Button_0.config(text = "UPDATE")
    GUI_Button_1.config(text = "DATABASE")

    Total_Quantity = YUGIOH_Database_CardQuantity()
    GUI_Label_Database_CardQuantity1.config(text = Total_Quantity)
    GUI_Label_Database_CardQuantity1.update()
    
    UniqueCards = YUGIOH_Database_CardUnique()
    GUI_Label_Database_CardUnique1.config(text = UniqueCards)
    GUI_Label_Database_CardUnique1.update()
    
    MostValuable = YUGIOH_Database_MostValuable()
    GUI_Label_Database_CardMostValuable1.config(text = MostValuable)
    GUI_Label_Database_CardMostValuable1.update()
    
    LeastValuable = YUGIOH_Database_LeastValuable()
    GUI_Label_Database_CardLeastValuable1.config(text = LeastValuable)
    GUI_Label_Database_CardLeastValuable1.update()
    
    Common = YUGIOH_Database_CommonValuable()
    GUI_Label_Database_CardCommon1.config(text = Common)
    GUI_Label_Database_CardCommon1.update()
    
    TotalHigh = YUGIOH_Databased_TotalValueHigh()
    GUI_Label_Database_TotalValueHigh1.config(text = TotalHigh)
    GUI_Label_Database_TotalValueHigh1.update()
    
    TotalLow = YUGIOH_Databased_TotalValueLow()
    GUI_Label_Database_TotalValueLow1.config(text = TotalLow)
    GUI_Label_Database_TotalValueLow1.update()
    
    TotalAverage = YUGIOH_Databased_TotalValueAverage()
    GUI_Label_Database_TotalValueAverage1.config(text = TotalAverage)
    GUI_Label_Database_TotalValueAverage1.update()
    
    
def GUI_Button_1_Function(): # Queries the database for all entries and lists them
    GUI_Frame_2_1.place_forget()
    GUI_Label_Information.config(text = "Loading DATABASE")
    GUI_Label_Information.update()
    GUI_Frame_2_2.place(relx = 0, rely = 0.1)
    GUI_Button_0.config(text = "STATS")
    GUI_Button_1.config(text = "UPDATE")
    
    for Card in GUI_Database.get_children():
        GUI_Database.delete(Card)
    
    
    QUERY = YUGIOH_Database_QueryAll()
    for QUERY in QUERY:
        QueryValues = (QUERY.Card_Number, QUERY.Card_Name, QUERY.Quantity, QUERY.Card_Set_Name, 
                    QUERY.Price_Low, QUERY.Price_High, QUERY.Price_Average, QUERY.Date_Added)
        GUI_Database.insert(parent = "", index = "end",
                            values = QueryValues)
        

# GUI_Database['columns'] = ("Card_Number", "Card_Name", "Quantity", "Card_Set_Name", "Price_Low", "Price_High", "Price_Average", "Date_Added")
def Treeview_Binding_Function(event): # Checks if the row returns nothing which means it's a heading, and then from column number one can deduce the location easily
    if GUI_Database.identify_row(event.y) == "":
        if GUI_Database.identify_column(event.x) == "#1":
            Treeview_Sort_CardNumbers()
        if GUI_Database.identify_column(event.x) == "#2":
            Treeview_Sort_CardName()
        if GUI_Database.identify_column(event.x) == "#3":
            Treeview_Sort_CardQuantity()
        if GUI_Database.identify_column(event.x) == "#4":
            Treeview_Sort_CardSetName()
        if GUI_Database.identify_column(event.x) == "#5":
            Treeview_Sort_CardPriceLow()
        if GUI_Database.identify_column(event.x) == "#6":
            Treeview_Sort_CardPriceHigh()
        if GUI_Database.identify_column(event.x) == "#7":
            Treeview_Sort_CardPriceAverage()
        if GUI_Database.identify_column(event.x) == "#8":
            Treeview_Sort_CardDateAdded()
        
        
# All the sorting functions for when the user hits the headings
global CardNumbersReverse
CardNumbersReverse = False
def Treeview_Sort_CardNumbers():
    for Card in GUI_Database.get_children():
        GUI_Database.delete(Card)

    QueryList = []
    QUERY = YUGIOH_Database_QueryAll()
    for QUERY in QUERY:
        QueryValues = (QUERY.Card_Number, QUERY.Card_Name, QUERY.Quantity, QUERY.Card_Set_Name, 
            QUERY.Price_Low, QUERY.Price_High, QUERY.Price_Average, QUERY.Date_Added)
        QueryList.insert(0, QueryValues)

    def GetCardValue(QueryValues):
        return QueryValues[0]
    
    global CardNumbersReverse
    if CardNumbersReverse:
        CardNumbersReverse = False
        Sorted_QueryList = sorted(QueryList, key = GetCardValue)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()
    else:
        CardNumbersReverse = True
        Sorted_QueryList = sorted(QueryList, key = GetCardValue, reverse = True)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()


global CardNameReverse
CardNameReverse = False
def Treeview_Sort_CardName():
    for Card in GUI_Database.get_children():
        GUI_Database.delete(Card)

    QueryList = []
    QUERY = YUGIOH_Database_QueryAll()
    for QUERY in QUERY:
        QueryValues = (QUERY.Card_Number, QUERY.Card_Name, QUERY.Quantity, QUERY.Card_Set_Name, 
            QUERY.Price_Low, QUERY.Price_High, QUERY.Price_Average, QUERY.Date_Added)
        QueryList.insert(0, QueryValues)

    def GetCardValue(QueryValues):
        return QueryValues[1]
    
    global CardNameReverse
    if CardNameReverse:
        CardNameReverse = False
        Sorted_QueryList = sorted(QueryList, key = GetCardValue)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()
    else:
        CardNameReverse = True
        Sorted_QueryList = sorted(QueryList, key = GetCardValue, reverse = True)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()


global CardQuantityReverse
CardQuantityReverse = False
def Treeview_Sort_CardQuantity():
    for Card in GUI_Database.get_children():
        GUI_Database.delete(Card)

    QueryList = []
    QUERY = YUGIOH_Database_QueryAll()
    for QUERY in QUERY:
        QueryValues = (QUERY.Card_Number, QUERY.Card_Name, QUERY.Quantity, QUERY.Card_Set_Name, 
            QUERY.Price_Low, QUERY.Price_High, QUERY.Price_Average, QUERY.Date_Added)
        QueryList.insert(0, QueryValues)

    def GetCardValue(QueryValues):
        return QueryValues[2]
    
    global CardQuantityReverse
    if CardQuantityReverse:
        CardQuantityReverse = False
        Sorted_QueryList = sorted(QueryList, key = GetCardValue)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()
    else:
        CardQuantityReverse = True
        Sorted_QueryList = sorted(QueryList, key = GetCardValue, reverse = True)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()


global CardSetNameReverse
CardSetNameReverse = False
def Treeview_Sort_CardSetName():
    for Card in GUI_Database.get_children():
        GUI_Database.delete(Card)

    QueryList = []
    QUERY = YUGIOH_Database_QueryAll()
    for QUERY in QUERY:
        QueryValues = (QUERY.Card_Number, QUERY.Card_Name, QUERY.Quantity, QUERY.Card_Set_Name, 
            QUERY.Price_Low, QUERY.Price_High, QUERY.Price_Average, QUERY.Date_Added)
        QueryList.insert(0, QueryValues)

    def GetCardValue(QueryValues):
        return QueryValues[3]
    
    global CardSetNameReverse
    if CardSetNameReverse:
        CardSetNameReverse = False
        Sorted_QueryList = sorted(QueryList, key = GetCardValue)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()
    else:
        CardSetNameReverse = True
        Sorted_QueryList = sorted(QueryList, key = GetCardValue, reverse = True)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()


global CardPriceLowReverse
CardPriceLowReverse = False
def Treeview_Sort_CardPriceLow():
    for Card in GUI_Database.get_children():
        GUI_Database.delete(Card)

    QueryList = []
    QUERY = YUGIOH_Database_QueryAll()
    for QUERY in QUERY:
        QueryValues = (QUERY.Card_Number, QUERY.Card_Name, QUERY.Quantity, QUERY.Card_Set_Name, 
            QUERY.Price_Low, QUERY.Price_High, QUERY.Price_Average, QUERY.Date_Added)
        QueryList.insert(0, QueryValues)

    def GetCardValue(QueryValues):
        return QueryValues[4]
    
    global CardPriceLowReverse
    if CardPriceLowReverse:
        CardPriceLowReverse = False
        Sorted_QueryList = sorted(QueryList, key = GetCardValue)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()
    else:
        CardPriceLowReverse = True
        Sorted_QueryList = sorted(QueryList, key = GetCardValue, reverse = True)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()


global CardPriceHighReverse
CardPriceHighReverse = False
def Treeview_Sort_CardPriceHigh():
    for Card in GUI_Database.get_children():
        GUI_Database.delete(Card)

    QueryList = []
    QUERY = YUGIOH_Database_QueryAll()
    for QUERY in QUERY:
        QueryValues = (QUERY.Card_Number, QUERY.Card_Name, QUERY.Quantity, QUERY.Card_Set_Name, 
            QUERY.Price_Low, QUERY.Price_High, QUERY.Price_Average, QUERY.Date_Added)
        QueryList.insert(0, QueryValues)

    def GetCardValue(QueryValues):
        return QueryValues[5]
    
    global CardPriceHighReverse
    if CardPriceHighReverse:
        CardPriceHighReverse = False
        Sorted_QueryList = sorted(QueryList, key = GetCardValue)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()
    else:
        CardPriceHighReverse = True
        Sorted_QueryList = sorted(QueryList, key = GetCardValue, reverse = True)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()
            

global CardPriceAverageReverse
CardPriceAverageReverse = False
def Treeview_Sort_CardPriceAverage():
    for Card in GUI_Database.get_children():
        GUI_Database.delete(Card)

    QueryList = []
    QUERY = YUGIOH_Database_QueryAll()
    for QUERY in QUERY:
        QueryValues = (QUERY.Card_Number, QUERY.Card_Name, QUERY.Quantity, QUERY.Card_Set_Name, 
            QUERY.Price_Low, QUERY.Price_High, QUERY.Price_Average, QUERY.Date_Added)
        QueryList.insert(0, QueryValues)

    def GetCardValue(QueryValues):
        return QueryValues[6]
    
    global CardPriceAverageReverse
    if CardPriceAverageReverse:
        CardPriceAverageReverse = False
        Sorted_QueryList = sorted(QueryList, key = GetCardValue)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()
    else:
        CardPriceAverageReverse = True
        Sorted_QueryList = sorted(QueryList, key = GetCardValue, reverse = True)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()


global CardDateAddedReverse
CardDateAddedReverse = False
def Treeview_Sort_CardDateAdded():
    for Card in GUI_Database.get_children():
        GUI_Database.delete(Card)

    QueryList = []
    QUERY = YUGIOH_Database_QueryAll()
    for QUERY in QUERY:
        QueryValues = (QUERY.Card_Number, QUERY.Card_Name, QUERY.Quantity, QUERY.Card_Set_Name, 
            QUERY.Price_Low, QUERY.Price_High, QUERY.Price_Average, QUERY.Date_Added)
        QueryList.insert(0, QueryValues)

    def GetCardValue(QueryValues):
        return QueryValues[7]
    
    global CardDateAddedReverse
    if CardDateAddedReverse:
        CardDateAddedReverse = False
        Sorted_QueryList = sorted(QueryList, key = GetCardValue)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()
    else:
        CardDateAddedReverse = True
        Sorted_QueryList = sorted(QueryList, key = GetCardValue, reverse = True)
        
        for Sorted_QueryList in Sorted_QueryList:
            GUI_Database.insert(parent = "", index = "end",
                        values = Sorted_QueryList)
            GUI_Database.update()