from ast import List
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

SQLALCHEMY_TRACK_MODIFICATIONS = False


CardDatabase = Flask(__name__)
CardDatabase.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Card Database.db'

global ProgramDatabase
CardDatabase = SQLAlchemy(CardDatabase)
CardDatabase.create_all()
#Creates the database and binds the engine to the database, if the database already exists it will not create a new instance.

CardDatabaseEngine = create_engine('sqlite:///Card Database.db')
if not database_exists(CardDatabaseEngine.url):
    create_database(CardDatabaseEngine.url)

class Database_Table_YUGIOH(CardDatabase.Model):
    __tablename__ = "YUGIOH"

    #COLUMN 1 - 7 in the Table
    Card_Number = CardDatabase.Column('CN', CardDatabase.String, primary_key=True, unique=True)
    Quantity = CardDatabase.Column('QTY', CardDatabase.Integer)
    Card_Set_Name = CardDatabase.Column('SET', CardDatabase.String)
    Card_Name = CardDatabase.Column('Name', CardDatabase.String)
    Price_Low = CardDatabase.Column('Low', CardDatabase.Float)
    Price_High = CardDatabase.Column('High', CardDatabase.Float)
    Price_Average = CardDatabase.Column('Average', CardDatabase.Float)
    Date_Added = CardDatabase.Column(CardDatabase.DateTime, default=datetime.now)

def YUGIOH_DataBase_AddCard(API_DATA, CARD_QUANTITY):
    CardDatabase.create_all()
    ADD_CARD = Database_Table_YUGIOH(
            Card_Number = API_DATA['data']['price_data']['print_tag'],
            Quantity = CARD_QUANTITY,
            Card_Set_Name = API_DATA['data']['price_data']['name'],
            Card_Name = API_DATA['data']['name'],
            Price_Low = API_DATA['data']['price_data']['price_data']['data']['prices']['low'],
            Price_High = API_DATA['data']['price_data']['price_data']['data']['prices']['high'],
            Price_Average = API_DATA['data']['price_data']['price_data']['data']['prices']['average']
            )

    QUERY = Database_Table_YUGIOH.query.filter_by(Card_Number = API_DATA['data']['price_data']['print_tag']).first()
    if QUERY: #If the query exists in the database, it will add the quantity to it - if the quantity is negative, and total qty reaches 0, it will delete the entry
        QUERY.Quantity = QUERY.Quantity + int(CARD_QUANTITY)
        Database_Table_YUGIOH.query.filter_by(Quantity = 0).delete()
        CardDatabase.session.commit()
        return QUERY.Quantity
    else: #If the query doesn't exist, it will be added to the database
        CardDatabase.session.add(ADD_CARD)
        CardDatabase.session.commit()
        return "New"
    
    
    
def YUGIOH_Database_CardQuantity():
    CardDatabase.create_all()
    QUERY = Database_Table_YUGIOH.query.all()
    Total_Quantity = 0
    for QUERY in QUERY:
        Total_Quantity = Total_Quantity + QUERY.Quantity
    
    return Total_Quantity

def YUGIOH_Database_CardUnique():
    CardDatabase.create_all()
    QUERY = Database_Table_YUGIOH.query.all()
    UniqueCards = 0
    for QUERY in QUERY:
        if QUERY.Quantity >= 1:
            UniqueCards = UniqueCards + 1
    
    return UniqueCards

def YUGIOH_Database_MostValuable():
    CardDatabase.create_all()
    QUERY = Database_Table_YUGIOH.query.all()
    PriceHighest = 0
    CardName = None
    CardNumber = None
    for QUERY in QUERY:
        PriceHigh = QUERY.Price_High
        if PriceHigh >= PriceHighest:
            PriceHighest = PriceHigh
            CardName = QUERY.Card_Name
            CardNumber = QUERY.Card_Number
    
    return "{}$ | {} | {}".format(PriceHighest, CardName, CardNumber)

def YUGIOH_Database_LeastValuable():
    CardDatabase.create_all()
    QUERY = Database_Table_YUGIOH.query.all()
    PriceLowest = 100000
    CardName = None
    CardNumber = None
    for QUERY in QUERY:
        PriceLow = QUERY.Price_Low
        if PriceLow <= PriceLowest:
            PriceLowest = PriceLow
            CardName = QUERY.Card_Name
            CardNumber = QUERY.Card_Number
    
    return "{}$ | {} | {}".format(PriceLowest, CardName, CardNumber)

def YUGIOH_Database_CommonValuable():
    CardDatabase.create_all()
    QUERY = Database_Table_YUGIOH.query.all()
    Quantity = 0
    CardName = None
    CardNumber = None
    for QUERY in QUERY:
        PriceQuantity = QUERY.Quantity
        if PriceQuantity >= Quantity:
            Quantity = PriceQuantity
            CardName = QUERY.Card_Name
            CardNumber = QUERY.Card_Number
    
    return "with {} cards | {} | {}".format(Quantity, CardName, CardNumber)

def YUGIOH_Databased_TotalValueHigh():
    CardDatabase.create_all()
    TotalValueHigh = 0
    QUERY = Database_Table_YUGIOH.query.all()
    for QUERY in QUERY:
        CardValueHigh = QUERY.Price_High
        CardQuantity = QUERY.Quantity
        CombinedValue = CardValueHigh * CardQuantity
        TotalValueHigh = TotalValueHigh + CombinedValue
        
    return "{:.2f}$".format(TotalValueHigh)

def YUGIOH_Databased_TotalValueLow():
    CardDatabase.create_all()
    TotalValueLow = 0
    QUERY = Database_Table_YUGIOH.query.all()
    for QUERY in QUERY:
        CardValueLow = QUERY.Price_Low
        CardQuantity = QUERY.Quantity
        CombinedValue = CardValueLow * CardQuantity
        TotalValueLow = TotalValueLow + CombinedValue
        
    return "{:.2f}$".format(TotalValueLow)

def YUGIOH_Databased_TotalValueAverage():
    CardDatabase.create_all()
    TotalValueAverage = 0
    QUERY = Database_Table_YUGIOH.query.all()
    for QUERY in QUERY:
        CardValueAverage = QUERY.Price_Average
        CardQuantity = QUERY.Quantity
        CombinedValue = CardValueAverage * CardQuantity
        TotalValueAverage = TotalValueAverage + CombinedValue
        
    return "{:.2f}$".format(TotalValueAverage)

def YUGIOH_Database_QueryAll():
    CardDatabase.create_all()
    QUERY = Database_Table_YUGIOH.query.all()
    
    return QUERY
