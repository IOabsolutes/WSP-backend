from app.database.db import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func

class item(Base):
    __tablename__ = "item"
    
    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    
