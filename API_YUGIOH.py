import requests, json
from PIL import Image
from io import StringIO

def API_GetStatus():
    API_URL = "http://yugiohprices.com/api/price_for_print_tag/MVP1-EN055"
    API_DATA = requests.get(API_URL).json()
    API_STATUS = API_DATA['status']
    PRICER_STATUS = API_DATA['data']['price_data']['price_data']['status']
    return API_STATUS, PRICER_STATUS

def API_SearchCardNumber(CARD_NUMBER):
    API_URL = f"http://yugiohprices.com/api/price_for_print_tag/{CARD_NUMBER}"
    API_DATA = requests.get(API_URL).json()
    
    return API_DATA


