from pydantic import BaseModel

class BankNoteModel(BaseModel):
    variance:float
    skewness:float
    curtosis:float
    entropy:float