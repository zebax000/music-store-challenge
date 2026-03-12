# Music Store
from datetime import datetime

class Transaction:
    SELL: int = 1
    SUPPLY: int = 2

    def __init__(self,type: int, copies: int ):
        self.type: int = type
        self.copies: int = copies
        self.date: datetime = datetime.now()

class Disc:
    def  __init__(self, sid:str, title:str, artist:str, sale_price:float ,purchase_price:float, quantity: int):
        self.sid: str = sid
        self.title: str = title
        self.artist: str = artist
        self.sale_price: float = sale_price
        self.purchase_price: float = purchase_price
        self.quantity: int = quantity
        self.song_list: list[str] = []
        self.transactions: list[Transaction]= []

    def add_song(self,song:str):
        ...
    def sell(self, copies:int) -> bool:
        ...
    def supply(self,copies: int) -> bool:
        ...
    def copies_sold(self) -> int:
        ...
    def __str__(self) -> str:
        ...





