from datetime import datetime ,time
from pyexpat import model
from pydantic import BaseModel, EmailStr 
from typing import Optional , List


class URLSHORTCREATED(BaseModel):
    long_url :str
class  URLSHORTNERRESPONSE(BaseModel):
    id:int
    short_url:str
    long_url:str
    created_at:datetime
    class config:
        from_attribute:True