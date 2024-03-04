from app.database.db import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func


class Worker(Base):
    __tablename__ = "worker"

    worker_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    phone_number = Column(String, index=True, unique=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    pass_hash = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
