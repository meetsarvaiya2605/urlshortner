from fastapi  import APIRouter,Depends ,HTTPException
from sqlalchemy.orm import Session
from urlshortner.database import get_db 
from urlshortner import schemas ,models
import string
import random


router = APIRouter(

)

def url_shortner(long_url:str ,lenth =6):
    characters = string.ascii_letters+string.digits
    shortt_url = ''.join(random.choices(characters,k=lenth))
    return shortt_url

@router.post("/shortner")
def url(long_url:schemas.URLSHORTCREATED,db:Session=Depends(get_db)):
    short_code =  url_shortner(long_url.long_url)
    db_query = models.URL_Short(short_url=short_code, long_url= long_url.long_url)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    
    return {"shorts_url":f"https://meet.ly/{short_code}"}



@router.get("/shortner/{shortss_url}")
def redirect_to_original(shortss_url: str , db: Session = Depends(get_db)):
    db_url = db.query(models.URL_Short).filter(models.URL_Short.short_url == shortss_url).first()
    if db_url:
        return {"long_url": db_url.long_url}
    raise HTTPException(status_code=404, detail="URL not found")
