from app.database.db import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func


class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    role = Column(String, index=True, nullable=False)
    pass_hash = Column(String, nullable=False)
    create_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


