from .database import Base
from sqlalchemy import TIMESTAMP , Column, Integer, String,Boolean,Time,Float, ForeignKey, Table , DateTime
from pydoc import text
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship



class URL_Short(Base):
    __tablename__ = "url_shortner"
    id = Column(Integer,primary_key=True,autoincrement=True)
    long_url =Column(String,nullable=False)
    short_url = Column(String,unique=True,primary_key=True,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default= text('now()'))
    